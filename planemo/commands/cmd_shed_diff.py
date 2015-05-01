"""
"""
import os
import shutil
import tempfile
import sys

import click

from planemo.cli import pass_context
from planemo.io import shell
from planemo import options
from planemo import shed


@click.command("shed_diff")
@options.optional_project_arg(exists=True)
@options.shed_owner_option()
@options.shed_name_option()
@options.shed_target_option()
@click.option(
    "-o", "--output",
    type=click.Path(file_okay=True, resolve_path=True),
    help="Send diff output to specified file.",
    default=None,
)
@click.option(
    '--shed_target_source',
    help="Source Tool Shed to diff against (will ignore local project info"
         " specified). To compare the main Tool Shed against the test, set"
         " this to testtoolshed.",
    default=None,
)
@options.recursive_shed_option()
@pass_context
def cli(ctx, path, **kwds):
    """Produce diff between local repository and Tool Shed contents.

    By default, this will produce a diff between this repository and what
    would be uploaded to the Tool Shed with the `shed_upload` command - but
    this command can be made to compare other combinations of repositories.
    Here are some examples::

        % # diff for this repository and the main Tool Shed
        % planemo shed_diff
        % # diff for this repository and the test Tool Shed
        % planemo shed_diff --shed_target testtoolshed
        % # diff for the test Tool Shed and main Tool Shed
        % planemo shed_diff --shed_target_source testtoolshed
        % # diff for two an explicitly specified repositories (ignores
        % # current project's shed YAML file.)
        % planemo shed_diff --owner peterjc --name blast_rbh
            --shed_target_source testtoolshed
    """
    def diff(realized_repository):
        working = tempfile.mkdtemp(prefix="tool_shed_diff_")
        try:
            diff_in(ctx, working, realized_repository, **kwds)
        finally:
            shutil.rmtree(working)

    exit_code = shed.for_each_repository(diff, path, **kwds)
    sys.exit(exit_code)


def diff_in(ctx, working, realized_repository, **kwds):
    path = realized_repository.path
    shed_target_source = kwds.get("shed_target_source", None)

    label_a = "_%s_" % (shed_target_source if shed_target_source else "local")
    shed_target = kwds.get("shed_target", "B")
    if "/" in shed_target:
        shed_target = "custom_shed"
    label_b = "_%s_" % shed_target

    mine = os.path.join(working, label_a)
    other = os.path.join(working, label_b)

    tsi = shed.tool_shed_client(ctx, read_only=True, **kwds)
    shed.download_tarball(
        ctx,
        tsi,
        realized_repository,
        destination=other,
        clean=True,
        **kwds
    )
    if shed_target_source:
        new_kwds = kwds.copy()
        new_kwds["shed_target"] = shed_target_source
        tsi = shed.tool_shed_client(ctx, read_only=True, **new_kwds)
        shed.download_tarball(
            ctx,
            tsi,
            realized_repository,
            destination=mine,
            clean=True,
            **new_kwds
        )
    else:
        tar_path = shed.build_tarball(path)
        cmd_template = 'mkdir "%s"; tar -xzf "%s" -C "%s"; rm -rf %s'
        shell(cmd_template % (mine, tar_path, mine, tar_path))

    cmd = 'cd "%s"; diff -r %s %s' % (working, label_a, label_b)
    if kwds["output"]:
        cmd += "> '%s'" % kwds["output"]
    shell(cmd)
