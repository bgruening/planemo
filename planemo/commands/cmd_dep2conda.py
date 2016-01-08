from __future__ import print_function
import os
import sys
import yaml
import tempfile
import subprocess

import click
from xml.etree import ElementTree as ET

from planemo.io import info, error
from planemo.cli import pass_context
from planemo import options

from planemo.shed2tap.base import BasePackage, Dependency


# We're using strict bash mode for dep_install.sh:
preamble_dep_install = """#!/bin/bash
#set -euo pipefail
set -eo pipefail
if [[ ! -d $INSTALL_DIR ]]
then
    echo "ERROR: Environment variable INSTALL_DIR not a directory!"
    exit 1
fi
# Set full strict mode now, side stepping case $INSTALL_DIR not setup.
set -euo pipefail
export DOWNLOAD_CACHE=`(cd "$DOWNLOAD_CACHE"; pwd)`
if [[ ! -d $DOWNLOAD_CACHE ]]
then
    mkdir -p $DOWNLOAD_CACHE
fi
echo "Using $DOWNLOAD_CACHE for cached downloads."
export INSTALL_DIR=`(cd "$INSTALL_DIR"; pwd)`
echo "Using $INSTALL_DIR for the installed files."
# Create a randomly named temp folder for working in
dep_install_tmp=${TMPDIR-/tmp}/dep_install.$RANDOM.$RANDOM.$RANDOM.$$
(umask 077 && mkdir $dep_install_tmp) || exit 1
"""

final_dep_install = """echo "Cleaning up..."
rm -rf $dep_install_tmp
echo "======================"
echo "Installation complete."
echo "======================"
"""

# Expect user to "source env.sh" so don't set strict mode,
# and don't use the exit command!
preamble_env_sh = """#!/bin/bash
if [[ ! -d $INSTALL_DIR ]]
then
    echo "ERROR: Environment variable INSTALL_DIR not a directory!"
fi
export INSTALL_DIR=${INSTALL_DIR:-$PWD}
export INSTALL_DIR=`(cd "$INSTALL_DIR"; pwd)`
"""

R_TEST_FILE = """#!/bin/bash

if [ "$(uname)" == "Darwin" ]; then

    $R -e "library('$1')"

elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then

    $R -e "library('$1')"

else
    %R% -e "library('$1')"
fi
"""



def conda_meta_template():
    package = {'name': '', 'version': ''}
    source = {'fn': '', 'url': '', 'sha256': ''}
    build = {'number': 0}

    requirements_build = []
    requirements_run = []
    requirements = {'build': requirements_build, 'run': requirements_run}

    test = {'commands': []}
    about = {'home': '', 'license': '', 'summary': ''}

    meta = {'package': package,
            'source': source,
            'build': build,
            'requirements': requirements,
            'test': test,
            'about': about}
    return meta

def pp( d ):
    print(yaml.dump(d), end='')


def find_tool_dependencis_xml(path, recursive):
    """Iterator function, quick & dirty tree walking."""
    if os.path.isfile(path):
        if os.path.basename(path) == "tool_dependencies.xml":
            yield path
    elif os.path.isdir(path):
        p = os.path.join(path, "tool_dependencies.xml")
        if os.path.isfile(p):
            yield p
        if recursive:
            for f in sorted(os.listdir(path)):
                p = os.path.join(path, f)
                if os.path.isdir(p):
                    # TODO: yield from
                    for x in find_tool_dependencis_xml(p, recursive):
                        yield x

def _dependency_exists(name, version):
    cmd = 'conda search %s=%s -c r -c bioconda --spec ; ' % (name, version)
    cmd += 'conda search %s=%s.0 -c r -c bioconda --spec ; ' % (name, version)
    cmd += 'conda search %s=%s -c r -c bioconda --spec ; ' % (name.replace('_','-'), version)
    cmd += 'conda search %s=%s.0 -c r -c bioconda --spec ' % (name.replace('_','-'), version)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, stderr=open(os.devnull, 'w'))
    out = str(process.communicate()[0])
    return out.find(name) != -1 or out.find(name.replace('_','-')) != -1




def convert_tool_dep(dependencies_file):
    """Parse a tool_dependencies.xml into install.sh and env.sh commands.

    Returns two lists of strings, commands to add to install.sh and
    env.sh respectively.
    """
    meta = conda_meta_template()
    build = []
    found_deps = 0

    root = ET.parse(dependencies_file).getroot()
    package_els = root.findall("package")

    packages = []
    dependencies = []
    for package_el in package_els:
        install_els = package_el.findall("install")

        name = package_el.attrib["name"].lower()
        version = package_el.attrib["version"]
        meta['package']['name'] = name
        meta['package']['version'] = version
        assert len(install_els) in (0, 1)

        repository_el = package_el.find("repository")

        if _dependency_exists(name, version) == True or name in ['atlas','libpng', 'python_pillow', 'cython', 'tiff']:
            info("\tPackage (%s == %s) already exists, skipping %s" % (name, version, dependencies_file))
            found_deps += 1

        #if dependencies_file.find('package_python_') != -1:
        #    info('\tPython dependency (%s) will not be converted. Please use a native Conda package.' % tool_dep)
        #    continue

        if len(install_els) == 0:
            assert repository_el is not None, "no repository in %s" % repository_el
            dependencies.append(Dependency(None, package_el, repository_el))
            if name != 'python':
                meta['requirements']['build'].append( '%s ==%s' % (name, version) )
                meta['requirements']['run'].append( '%s ==%s' % (name, version) )
        else:
            install_el = install_els[0]
            packages.append(BasePackage(None, package_el, install_el, readme=None))

    if found_deps == len(package_els):
        return [],[],'All dependencies already in Conda'

    if not packages:
        info("No packages in %s" % dependencies_file)
        return [], [], 'No packages'

    assert len(packages) == 1, packages
    package = packages[0]
    name = package_el.attrib["name"]
    version = package_el.attrib["version"]

    for action in package.all_actions:
        action.to_conda(meta, build)

    return meta, build, 'ok'

def process_tool_dependencies_xml(tool_dep, shed_info):
    """Writes to handles, returns success as a boolean."""
    if not os.path.isfile(tool_dep):
        error('Missing file %s' % tool_dep)
        return False
    if not os.stat(tool_dep).st_size:
        error('Empty file %s' % tool_dep)
        return False

    try:
        meta, build, status = convert_tool_dep(tool_dep)
        if status == "All dependencies already in Conda":
            with open(os.path.join(os.path.expanduser('~'),'migration.blastlist.txt'), 'a+') as migrate:
                migrate.write('%s\t%s' % (tool_dep, 'Already in Conda\n'))
            info('\tPackage available in Conda.')
            return True
    except Exception as err:
        # TODO - pass in ctx for logging?
        error('Error processing %s - %s' %
              (click.format_filename(tool_dep), err))
        if not isinstance(err, (NotImplementedError, RuntimeError)):
            # This is an unexpected error, traceback is useful
            import traceback
            error(traceback.format_exc() + "\n")
        return False
    # Worked...

    # Fill in information from shed.yml
    meta['about']['home'] = shed_info.get('homepage_url', '')
    meta['about']['summary'] = shed_info.get('long_description', shed_info.get('description', '')).replace('\n', ' ')

    recipe_dir = './recipes/%s/%s' % (meta['package']['name'], meta['package']['version'])
    if not os.path.exists(recipe_dir):
        os.makedirs(recipe_dir)
    else:
        pass#info('\tRecipe already exists: %s' % recipe_dir)

    # Write the meta.yaml file
    with open(os.path.join(recipe_dir, 'meta.yaml'), 'w+') as meta_handle:
        yaml.dump(meta, meta_handle, allow_unicode=True, default_flow_style=False)

    # Write the build.sh file
    with open(os.path.join(recipe_dir, 'build.sh'), 'w+') as build_handle:
        build = ['#!/bin/sh'] + build
        for command in build:
            build_handle.write(command + '\n')

    if meta['package']['name'].startswith('r-'):
        with open(os.path.join(recipe_dir, 'test.sh'), 'w+') as test_handle:
            test_handle.write(R_TEST_FILE)

    return True


@click.command('dependency_script')
@options.shed_realization_options()
@options.dependencies_script_options()
@pass_context
def cli(ctx, paths, recursive=False, fail_fast=True, download_cache=None):
    """Prepare a bash shell script to install tool requirements (**Experimental**)

    An experimental approach parsing tool_dependencies.xml files into
    bash shell scripts, intended initially for use within Continuous
    Integration testing setups like TravisCI.

    Parses the specified ``tool_dependencies.xml`` files, and converts them into
    an installation bash script (default ``dep_install.sh``), and a shell script
    (default ``env.sh``) defining any new/edited environment variables.

    These are intended to be used via ``bash dep_install.sh`` (once), and as
    ``source env.sh`` prior to running any of the dependencies to set the
    environment variable within the current shell session.

    Both ``dep_install.sh`` and ``env.sh`` require ``$INSTALL_DIR`` be defined
    before running them, set to an existing directory with write permissions.
    Beware than if run on multiple tools, they can over-write each other (for
    example if you have packages for different versions of the same tool). Icythonn
    this case make separate calls to ``planemo dependency_script`` and call
    the scripts with different installation directories.

    This command will download (and cache) any URLs specified via Galaxy
    download actions. This is in order to decompress them and determine the
    relevant sub-folder to change into as per the Tool Shed install mechanism,
    so that this can be recorded as a ``cd`` comand in the bash script.

    The download cache used by ``planemo dependency_script`` and the resulting
    output script ``dep_install.sh`` defaults to ``./download_cache`` (under
    the current working directory), and can be set with ``$DOWNLOAD_CACHE``.

    This is experimental, and is initially intended for use within continuous
    integration testing setups like TravisCI to both verify the dependency
    installation receipe works, and to use this to run functional tests.
    """
    # TODO: Command line API for bash output filanames & install dir, cache.
    if download_cache:
        assert os.path.isdir(download_cache), download_cache
        # Effectively using this as a global variable, refactor this
        # once using a visitor pattern instead of action.to_bash()
        os.environ["DOWNLOAD_CACHE"] = os.path.abspath(download_cache)
        print("Using $DOWNLOAD_CACHE=%r" % os.environ["DOWNLOAD_CACHE"])
    elif not "DOWNLOAD_CACHE" in os.environ:
        temp = tempfile.mkdtemp()
        os.environ["DOWNLOAD_CACHE"] = temp
    failed = False
    with open("env.sh", "w") as env_sh_handle:
        with open("dep_install.sh", "w") as install_handle:
            #install_handle.write(preamble_dep_install)
            #env_sh_handle.write(preamble_env_sh)

            for path in paths:
                #ctx.log("Checking: %r" % path)
                if failed and fail_fast:
                    break
                for tool_dep in find_tool_dependencis_xml(path, recursive):
                    need_conversion = True
                    with open(os.path.join(os.path.expanduser('~'),'migration.blastlist.txt'), 'r') as handle:
                        for line in handle:
                            if line.split('\t')[0].strip() == tool_dep:
                                need_conversion = False
                                break
                    if not need_conversion:
                        continue

                    info('Start convertion of %s' % tool_dep)

                    shed_yaml = os.path.join( os.path.dirname(tool_dep), '.shed.yml' )
                    if os.path.exists(shed_yaml):
                        with open(shed_yaml, 'r') as handle:
                            shed_info = yaml.load(handle)
                    else:
                        shed_info = {}


                    passed = process_tool_dependencies_xml(tool_dep, shed_info)
                    if passed:
                        pass#info('\tDone: %s' % tool_dep)
                    else:
                        failed = True
                        if fail_fast:
                            for line in [
                                    '#' + '*' * 60,
                                    'echo "WARNING: Skipping %s"' % tool_dep,
                                    '#' + '*' * 60]:
                                install_handle.write(line + "\n")
                            break
                        # error("%s failed" % tool_dep)
            install_handle.write(final_dep_install)
    ctx.log("The End")
    if failed:
        error('Error processing one or more tool_dependencies.xml files.')
        sys.exit(1)
