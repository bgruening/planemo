.. :changelog:

History
-------

.. to_doc

---------------------
0.75.32.dev0
---------------------

---------------------
0.75.31 (2025-06-23)
---------------------

* Don't pollute working directory with tools.yaml file (thanks to
  `@mvdbeek`_). `Pull Request 1554`_
* Add ruff and isort to `make format` and tox, add pre-commit config (thanks
  to `@mvdbeek`_). `Pull Request 1552`_
* Make ``no_dependency_resolution`` and ``simultaneous_upload`` global options
  (thanks to `@mvdbeek`_). `Pull Request 1553`_
* Add flag to export invocation from run command (thanks to `@mvdbeek`_).
  `Pull Request 1551`_
* Load default job metrics (thanks to `@mvdbeek`_). `Pull Request 1548`_
* Drop unnecessary autogen in cmd_slurm_init (thanks to `@mvdbeek`_). `Pull
  Request 1549`_
* Terminate polling if we can't advance invocation (thanks to `@mvdbeek`_).
  `Pull Request 1547`_
* Don't do preload in managed instance (thanks to `@mvdbeek`_). `Pull Request
  1546`_
* Add a slurm_init command (thanks to `@jmchilton`_). `Pull Request 1543`_
* Add missing module to pyproject.toml (thanks to `@mvdbeek`_). `Pull Request
  1545`_
* Add the option to download the outputs of a completed workflow run (thanks
  to `@Smeds`_). `Pull Request 1532`_
* update shed categories (thanks to `@bgruening`_). `Pull Request 1539`_
* cmd to export an existing invocations as an archive for storage or later
  import (thanks to `@Smeds`_). `Pull Request 1534`_
* Bump requirements for galaxy packages to 25.0 (thanks to
  `@ahmedhamidawan`_). `Pull Request 1542`_
* Print job errors in workflow invocation as they occur (thanks to
  `@mvdbeek`_). `Pull Request 1540`_
* Enable celery tasks (thanks to `@mvdbeek`_). `Pull Request 1541`_
* add file extension to downloaded output (thanks to `@Smeds`_). `Pull Request
  1531`_
* Workflow progress bar (thanks to `@jmchilton`_). `Pull Request 1510`_
* Fix job handler setup (thanks to `@mvdbeek`_). `Pull Request 1538`_
* Overhaul Galaxy job config handling (thanks to `@jmchilton`_). `Pull Request
  1506`_
* create provided output_directory if it doesn't exist (thanks to `@Smeds`_).
  `Pull Request 1526`_

---------------------
0.75.30 (2025-05-07)
---------------------
* fix lint_shed_version if there are no installable revisions (thanks to
  `@bernt-matthias`_). `Pull Request 1509`_
* Fix bumping of dev versions (thanks to `@mvdbeek`_). `Pull Request 1514`_
* Don't escape non-ascii unicode characters in json.dumps (thanks to
  `@mvdbeek`_). `Pull Request 1523`_
* Fix version linter for new repos (thanks to `@bernt-matthias`_). `Pull
  Request 1519`_
* Add switch to prevent early termination of workflow runs (thanks to
  `@kostrykin`_). `Pull Request 1518`_
* Add missing collection operation tools (thanks to `@mvdbeek`_). `Pull
  Request 1524`_

---------------------
0.75.29 (2025-03-27)
---------------------
* Fix dependency specification (thanks to `@mvdbeek`_). `Pull Request 1507`_

---------------------
0.75.28 (2025-03-27)
---------------------
* Print stdout stderr if install command fails (thanks to `@mvdbeek`_). `Pull
  Request 1505`_
* fix: removes that spaces that aren't allowed in the singularity instance
  name (thanks to `@Smeds`_). `Pull Request 1504`_
* Build Modernization (thanks to `@jmchilton`_). `Pull Request 1503`_
* Add linter to check if tool versions are bumped (thanks to `@bernt-matthias`_).
  `Pull Request 1502`_
* Fix make quick-test (thanks to `@jmchilton`_). `Pull Request 1501`_
* Migrate mypy settings to pyproject.toml (thanks to `@jmchilton`_). `Pull
  Request 1500`_
* Add support for Python 3.12 (thanks to `@nsoranzo`_). `Pull Request 1496`_
* Add postgres singularity option (thanks to `@Smeds`_). `Pull Request 1492`_
* Loosen test assertions (thanks to `@bernt-matthias`_). `Pull Request 1494`_
* Update browser user agent string (thanks to `@nsoranzo`_). `Pull Request
  1495`_

---------------------
0.75.27 (2025-03-03)
---------------------
* Remove usage of `defaults` conda channel (thanks to `@bernt-matthias`_).
  `Pull Request 1487`_
* Add category "Geo Science" (thanks to `@bernt-matthias`_). `Pull Request 1483`_
* Bump requirements for galaxy packages to 24.2 (thanks to `@jdavcs`_). `Pull
  Request 1491`_
* Use python 3.13 for deploymen (thanks to `@bernt-matthias`_). `Pull Request 1488`_
* Fix repository category update (thanks to `@mvdbeek`_). `Pull Request 1481`_

---------------------
0.75.26 (2024-09-24)
---------------------
* Fix up autopygen type annotation (thanks to `@mvdbeek`_). `Pull Request
  1474`_
* Fix autoupdate for workflows with overlapping tool updates (thanks to
  `@bernt-matthias`_). `Pull Request 1452`_
* Display last lines of logs (thanks to `@mvdbeek`_). `Pull Request 1473`_

---------------------
0.75.25 (2024-08-11)
---------------------
* Add a new single cell category (thanks to `@pavanvidem`_). `Pull Request
  1457`_
* Add extended-assertions requirements (thanks to `@bernt-matthias`_). `Pull
  Request 1471`_

---------------------
0.75.24 (2024-07-04)
---------------------
* Workflow best practices: check that creator identifiers are URIs (thanks to
  `@elichad`_). `Pull Request 1458`_
* Update pinning for Galaxy 24.1 (thanks to `@bernt-matthias`_). `Pull Request
  1460`_
* Add option to create a minimal markdown test report (thanks to
  `@bernt-matthias`_). `Pull Request 1462`_
* Increase worflow linting (thanks to `@lldelisle`_). `Pull Request 1463`_
* Run CI tests against newer Galaxy versions (thanks to `@bernt-matthias`_).
  `Pull Request 1466`_
* Add the option to provide a history id to run the workflow in (thanks to
  `@Delphine-L`_). `Pull Request 1461`_
* Make sure that skip list does not get `['']` (if no skip is given) (thanks
  to `@bernt-matthias`_). `Pull Request 1453`_
* Tool linting add `--skip_file` and remove lxml schema validation (thanks to
  `@bernt-matthias`_). `Pull Request 1420`_

---------------------
0.75.23 (2024-05-08)
---------------------
* Implement run/test/workflow_edit/autoupdate from non default tool sheds
  (thanks to `@mvdbeek`_). `Pull Request 1445`_
* Install prebuilt client by default (thanks to `@mvdbeek`_). `Pull Request
  1450`_
* Bump galaxy packages to allow for 24.0 (thanks to `@bernt-matthias`_). `Pull
  Request 1441`_
* replace dead link in conclusions (thanks to `@martenson`_). `Pull Request
  1447`_
* Add text to autopygen exceptions (thanks to `@bernt-matthias`_). `Pull
  Request 1444`_
* Drop circleci config (thanks to `@mvdbeek`_). `Pull Request 1443`_
* Fix linting of asserts with children (thanks to `@bernt-matthias`_). `Pull
  Request 1442`_

---------------------
0.75.22 (2024-04-04)
---------------------
* Fix parsing of training ``metadata.yaml`` files (thanks to `@nsoranzo`_).
  `Pull Request 1439`_
* Fix markdown template: add missing closing details tag (thanks to `@bernt-matthias`_). `Pull Request 1440`_
* Misc workflow linting improvements (thanks to `@bernt-matthias`_). `Pull
  Request 1437`_
* Don't skip requirements with an environment marker (thanks to `@nsoranzo`_).
  `Pull Request 1433`_
* Add `--host` parameter to allow listening on non-default hosts (thanks to
  `@selten`_). `Pull Request 1430`_

---------------------
0.75.21 (2024-02-01)
---------------------
* Add option to pass extra arguments to `docker run` (thanks to `@bernt-matthias`_). `Pull Request 1428`_
* Fix workflow_edit (thanks to `@mvdbeek`_). `Pull Request 1427`_
* Update to black 2024 stable style (thanks to `@nsoranzo`_). `Pull Request
  1425`_

---------------------
0.75.20 (2024-01-30)
---------------------
* Fix use of `package_name` attribute on `CondaTarget` objects (thanks to
  `@nsoranzo`_). `Pull Request 1424`_
* Don't crash autoupdate on non-PEP440-compliant tool versions (thanks to
  `@nsoranzo`_). `Pull Request 1422`_
* Add now mandatory readthedocs config files (thanks to `@nsoranzo`_). `Pull
  Request 1419`_
* Update action versions (thanks to `@nsoranzo`_). `Pull Request 1416`_

---------------------
0.75.19 (2023-12-06)
---------------------

* Update upper bound for galaxy packages to < 23.2 (thanks to `@bernt-matthias`_). `Pull Request 1388`_
* Fix workflow download when using instance id (thanks to `@mvdbeek`_). `Pull
  Request 1412`_
* Remove introduction header from training init (thanks to `@hexylena`_).
  `Pull Request 1410`_

---------------------
0.75.18 (2023-11-16)
---------------------

* Pretty-print workflow and use correct version of linked workflow in
  ``workflow_test_init`` (thanks to `@mvdbeek`_). `Pull Request 1408`_
* Fix running workflow tests when there are multiple tests (thanks to
  `@mvdbeek`_). `Pull Request 1407`_
* Fix matching of tool ids to autoupdate (thanks to `@nsoranzo`_). `Pull
  Request 1406`_

---------------------
0.75.17 (2023-11-01)
---------------------
* Implement running tests against existing invocation (thanks to `@mvdbeek`_).
  `Pull Request 1401`_
* Fix test result download (thanks to `@mvdbeek`_). `Pull Request 1402`_

---------------------
0.75.16 (2023-11-01)
---------------------
* No changes

---------------------
0.75.15 (2023-10-29)
---------------------
* Change info message for markdown readme in repo
  (thanks to `@bernt-matthias`_). `Pull Request 1398`_
* Make test reports more resilient to failing invocations (thanks to
  `@mvdbeek`_). `Pull Request 1400`_
* Fix zenodo test, drop explicit datatype mapping (thanks to `@mvdbeek`_).
  `Pull Request 1399`_
* Fix linting rule selection (thanks to `@bernt-matthias`_). `Pull Request
  1396`_
* Add missing ``Astronomy``, ``CLIP-seq`` and ``Materials science`` TS
  categories (thanks to `@bernt-matthias`_). `Pull Request 1397`_

---------------------
0.75.14 (2023-10-19)
---------------------
* Fix workflow_lint for json output values (thanks to `@mvdbeek`_). `Pull
  Request 1395`_

---------------------
0.75.13 (2023-10-18)
---------------------
* Add --skip to shed_lint (thanks to `@bernt-matthias`_). `Pull Request 1394`_
* Remove API key requirement from training_init (thanks to `@hexylena`_).
  `Pull Request 1393`_
* Try to fix planemo test workflow when output is collection with identical
  name (thanks to `@lldelisle`_). `Pull Request 1391`_

---------------------
0.75.12 (2023-09-18)
---------------------
* Track subworkflow invocations after main invocation is scheduled (thanks to
  `@mvdbeek`_). `Pull Request 1389`_

---------------------
0.75.11 (2023-09-14)
---------------------

* Implement automatic tool generation based on the source code of the tool
  (thanks to `@Kulivox`_). `Pull Request 1263`_
* Support for testing workflows with conditional steps (thanks to
  `@mvdbeek`_). `Pull Request 1387`_

---------------------
0.75.10 (2023-09-01)
---------------------

* Add pick_value to distro_tools (thanks to `@mvdbeek`_). `Pull Request 1385`_
* Allow missing conda_exec (thanks to `@mstabrin`_). `Pull Request 1384`_
* Fix profile version test (thanks to `@bernt-matthias`_). `Pull Request
  1383`_
* Fix type comparisons (thanks to `@bernt-matthias`_). `Pull Request 1382`_
* Added a note that docker is required for docker and biocontainers option
  (thanks to `@paulzierep`_). `Pull Request 1355`_
* Optimize disk space usage for `planemo test` (thanks to `@bernt-matthias`_).
  `Pull Request 1378`_
* Fix for change of base_url in BioBlend 1.2.0 (thanks to `@nsoranzo`_). `Pull
  Request 1379`_

---------------------
0.75.9 (2023-06-29)
---------------------

* Update collection operation tool list (thanks to `@mvdbeek`_). `Pull Request
  1377`_
* Officially support Python 3.10 and 3.11 (thanks to `@nsoranzo`_). `Pull
  Request 1375`_
* Fix links (thanks to `@nsoranzo`_). `Pull Request 1374`_
* Fix ``test_run_gxtool_randomlines`` test on Galaxy dev branch (thanks to
  `@nsoranzo`_). `Pull Request 1373`_

---------------------
0.75.8 (2023-06-09)
---------------------

* Bump galaxy package requirements to allow for 23.0 (thanks to `@bernt-matthias`_). `Pull Request 1372`_
* Sanitize and make output names unique (thanks to `@mvdbeek`_). `Pull Request 1371`_
* Increase bioblend retries for bad networks (thanks to `@hexylena`_). `Pull Request 1369`_
* Add ``--biocontainers`` option to shed_lint (thanks to `@mvdbeek`_). `Pull Request 1370`_
* fix regex of orcid + add test (thanks to `@lldelisle`_). `Pull Request 1364`_
* Drop `allow_none` for finding repository (thanks to `@mvdbeek`_). `Pull Request 1358`_

---------------------
0.75.7 (2023-03-01)
---------------------
* Drop call to ``escape_non_unicode_symbols`` (thanks to `@nsoranzo`_). `Pull
  Request 1357`_

---------------------
0.75.6 (2023-02-22)
---------------------
* Allow running autoupdate against external server (thanks to `@mvdbeek`_).
  `Pull Request 1265`_
* Fix extraction of orcid identifiers for .dockstore.yml (thanks to
  `@lldelisle`_). `Pull Request 1350`_

---------------------
0.75.5 (2023-02-10)
---------------------
* Bump galaxy packages to 22.05 (thanks to `@bernt-matthias`_). `Pull Request
  1275`_

---------------------
0.75.4 (2023-02-09)
---------------------

* Store datasets by UUID (thanks to `@bernt-matthias`_). `Pull Request 1347`_
* Fix orcid regex for dockstore_init (thanks to `@lldelisle`_). `Pull Request
  1348`_
* Fix virtualenv dir bookkeeping (thanks to `@wm75`_). `Pull Request 1346`_
* Deprecate introduction slides folder (thanks to `@hexylena`_). `Pull Request
  1344`_
* Remove note recommending installing dev versions from `planemo run` tutorial
  (thanks to `@simonbray`_). `Pull Request 1338`_
* Rename configuration option removed in tox 4.0 (thanks to `@nsoranzo`_).
  `Pull Request 1337`_
* Remove travis-ci.org badge from README.rst (thanks to `@SimonWaldherr`_).
  `Pull Request 1334`_

---------------------
0.75.3 (2022-11-30)
---------------------

* Mount test data dir read-only in docker (thanks to `@mvdbeek`_). `Pull
  Request 1327`_
* Add traceback to report template (thanks to `@bernt-matthias`_). `Pull
  Request 1332`_
* Add indent and sort_keys to tool_test_json (thanks to `@simonbray`_). `Pull
  Request 1330`_
* Fix ``planemo shed_test`` (thanks to `@mvdbeek`_). `Pull Request 1329`_
* Add h5py dependency, required for comparing h5 files (thanks to
  `@mvdbeek`_). `Pull Request 1326`_
* Update GitHub action versions (thanks to `@nsoranzo`_). `Pull Request 1322`_
* Fix "glone" typo in error message (thanks to `@bernt-matthias`_). `Pull
  Request 1325`_
* Type annotation for input staging-related code (thanks to `@nsoranzo`_).
  `Pull Request 1320`_
* Add creator dockstore (thanks to `@lldelisle`_). `Pull Request 1314`_

---------------------
0.75.2 (2022-11-02)
---------------------

* Compare versions, not tool ids to find latest tool ids (thanks to
  `@mvdbeek`_). `Pull Request 1313`_
* Fix ``for_paths`` when path is directory of tools (thanks to `@mvdbeek`_).
  `Pull Request 1312`_
* Fix workflow_lint with list + check elements in collection (thanks to
  `@lldelisle`_). `Pull Request 1310`_
* Drop copy_tree workaround for tool sources (thanks to `@mvdbeek`_). `Pull
  Request 1308`_

---------------------
0.75.1 (2022-10-31)
---------------------

* Use `pytest.raises()` instead of ad-hoc `assert_raises_regexp()` context
  manager (thanks to `@nsoranzo`_). `Pull Request 1302`_
* Add planemo_ci_setup command (thanks to `@mvdbeek`_). `Pull Request 1304`_
* Don't fail planemo autoupdate if tool version not found in tool shed (thanks
  to `@lldelisle`_). `Pull Request 1305`_
* workflow_lint: ensure that tool shed tool ids are valid (thanks to
  `@lldelisle`_). `Pull Request 1306`_
* Fix recording of virtual_env_dir (thanks to `@mvdbeek`_). `Pull Request
  1307`_

---------------------
0.75.0 (2022-10-28)
---------------------

* Restore running tool tests against directory (thanks to `@mvdbeek`_). `Pull
  Request 1303`_
* Update outdated cuffmerge url (thanks to `@martenson`_). `Pull Request
  1247`_
* Set upstream branch when pushing workflows to GitHub (thanks to
  `@simonbray`_). `Pull Request 1249`_
* restore --no_cleanup to set cleanup_job to never (thanks to `@bernt-matthias`_). `Pull Request 1255`_
* Drop support for Python 3.6 (thanks to `@simonbray`_). `Pull Request 1257`_
* Replace CoC with link to GalaxyProject's one (thanks to `@nsoranzo`_). `Pull
  Request 1259`_
* Mains resource selector must be skipped (thanks to `@hexylena`_). `Pull
  Request 1260`_
* Ignore cloudflare 503 status when checking links (thanks to `@bernt-matthias`_). `Pull Request 1262`_
* Document the use of mandatory macro parameters and add named macro tokens
  (thanks to `@bernt-matthias`_). `Pull Request 1212`_
* Bump galaxy package requirements to 22.01 (thanks to `@bernt-matthias`_).
  `Pull Request 1264`_
* Run local galaxy via gravity (thanks to `@mvdbeek`_). `Pull Request 1232`_
* Lint randomlines.xml file (thanks to `@simonbray`_). `Pull Request 1270`_
* Check if main requirement is `None` (thanks to `@bernt-matthias`_). `Pull
  Request 1274`_
* Planemo type annotation: module planemo.commands.cmd_autoupdate (thanks to
  `@gallardoalba`_). `Pull Request 1278`_
* Planemo type annotation: module planemo.cli (thanks to `@gallardoalba`_).
  `Pull Request 1277`_
* Planemo type annotation: module cmd_clone (thanks to `@gallardoalba`_).
  `Pull Request 1279`_
* Planemo type annotation: module cmd_tool_init (thanks to `@gallardoalba`_).
  `Pull Request 1281`_
* Add type annotations to ``planemo.autoupdate`` module (thanks to
  `@nsoranzo`_). `Pull Request 1283`_
* Planemo type annotation: module cmd_normalize (thanks to `@gallardoalba`_).
  `Pull Request 1280`_
* Planemo type annotation: module planemo.conda (thanks to `@gallardoalba`_).
  `Pull Request 1284`_
* Add type annotations to ``planemo.glob`` and ``planemo.virtualenv`` (thanks
  to `@nsoranzo`_). `Pull Request 1287`_
* Drop ``conda_lint`` command (thanks to `@nsoranzo`_). `Pull Request 1288`_
* Type annotations for planemo.bioblend, planemo.git, and planemo.cwl.run
  (thanks to `@adRn-s`_). `Pull Request 1285`_
* Add FAQ page to docs (thanks to `@simonbray`_). `Pull Request 1271`_
* Add type annotations to ``planemo.runnable`` and ``planemo.workflow_lint``
  (thanks to `@nsoranzo`_). `Pull Request 1291`_
* Make `--channels` also affect mulled channels and update/extend howto use
  bioconda artifacts (thanks to `@bernt-matthias`_). `Pull Request 1227`_
* Planemo type annotation: config, context and factory (thanks to
  `@gallardoalba`_). `Pull Request 1292`_
* [Training] update templates to use new, more accessible box style (thanks to
  `@shiltemann`_). `Pull Request 1293`_
* Pre-create expected output file on disk (thanks to `@mvdbeek`_). `Pull
  Request 1276`_
* Control publish setting in .dockstore.yml, fix first release not appearing
  on dockstore (thanks to `@mvdbeek`_). `Pull Request 1295`_
* Fix disclosure css for summary elements (thanks to `@mvdbeek`_). `Pull
  Request 1294`_
* Enable providing multiple `--tool_data_table` options (thanks to
  `@mvdbeek`_). `Pull Request 1296`_
* Make startup timeout configurable (thanks to `@mvdbeek`_). `Pull Request
  1298`_
* Fix printing planemo test logs (thanks to `@mvdbeek`_). `Pull Request 1299`_
* Fix workflow test when input is optional but also workflow output (thanks to
  `@mvdbeek`_). `Pull Request 1297`_

---------------------
0.74.11 (2022-06-08)
---------------------

* Removing broken link, update it to current doc (thanks to `@profgiuseppe`_).
  `Pull Request 1244`_
* Implement nested collection inputs and outputs in workflow_test_init `Pull
  Request 1242`_
* More fixes for auto-generating workflow tests `Pull Request 1241`_
* Fix workflow_test_init for collection outputs `Pull Request 1239`_

---------------------
0.74.10 (2022-05-31)
---------------------
* Allow specifying URL and API key with workflow autoupdate and docs
  improvements (thanks to `@simonbray`_). `Pull Request 1237`_
* Pin planemo to last known working major galaxy version `Pull Request 1230`_
* Drop unused Python dependencies and upgrade syntax to Python 3.6 `Pull Request 1228`_
* Update `best_practice_search()` for changes in galaxy-tool-util `Pull Request 1224`_
* Make galaxy config `cleanup_job` depend on `--no_cleanup`
  (thanks to `@bernt-matthias`_). `Pull Request 1226`_
* Tool builder: add profile and suffix version
  (thanks to `@gallardoalba`_). `Pull Request 1222`_
* training-init: add the FAQ index page to tutorial folder
  (thanks to `@shiltemann`_). `Pull Request 1217`_
* Adding best practices and assertion checks to workflow_lint
  (thanks to `@simonbray`_). `Pull Request 1213`_
* Updates to workflow autoupdate required for IWC bot
  (thanks to `@simonbray`_). `Pull Request 1214`_
* Add test and fix for failing docker_galaxy engine
  (thanks to `@simonbray`_). `Pull Request 1215`_
* Generate workflow test from invocation id
  (thanks to `@simonbray`_). `Pull Request 1209`_
* Fixed minor typo in documentation
  (thanks to `@stain`_). `Pull Request 1206`_
* Add missing ToolShed categories `Pull Request 1207`_
* Use WorkflowId rather than StoredWorkflowId when autoupdating subworkflows
  (thanks to `@simonbray`_). `Pull Request 1205`_
* Always use random id_secret for testing (thanks to `@bernt-matthias`_). `Pull Request 1198`_
* Add rerun subcommand for rerunning jobs (thanks to `@simonbray`_). `Pull Request 1140`_

---------------------
0.74.9 (2021-11-03)
---------------------
* Fix rendering of subworkflow steps for workflow testing report (thanks to
  `@simonbray`_). `Pull Request 1200`_
* Replace Galaxy interactor galaxy_requests_post with make_post_request from
  BioBlend (thanks to `@simonbray`_). `Pull Request 1201`_

---------------------
0.74.8 (2021-10-10)
---------------------

* Exclude click 8.0.2. `Pull Request 1196`_
* Add tool version numbers to autoupdate logging (thanks to `@simonbray`_).
  `Pull Request 1188`_
* Allow tool autoupdate without conda installation (thanks to `@simonbray`_).
  `Pull Request 1193`_
* use correct key execution_problem in template (thanks to `@bernt-matthias`_).
  `Pull Request 1195`_

---------------------
0.74.7 (2021-09-21)
---------------------

* Fix documentation to include ``--download_outputs`` flag (thanks to
  `@simonbray`_). `Pull Request 1184`_
* Select refgenie config based on Galaxy version `Pull Request 1187`_
* Extend autoupdate subcommand to workflows (thanks to `@simonbray`_). `Pull
  Request 1151`_

---------------------
0.74.6 (2021-07-23)
---------------------

* Add JSON report for planemo run invocations (thanks to `@simonbray`_). `Pull
  Request 1153`_
* Ignore failure to download output datasets `Pull Request 1179`_
* Allow location to point to url for outputs `Pull Request 1180`_
* Fix --shed_install for gxformat2 workflows `Pull Request 1182`_
    
---------------------    
0.74.5 (2021-06-25)
---------------------

* Remove iuc from default channels `Pull Request 1170`_
* Fix parsing of changelog for git release `Pull Request 1171`_
* Remove legacy commands, egg handling `Pull Request 1172`_
* Use bioblend's invoke_workflow `Pull Request 1173`_
* Create more useful output for failed invocations `Pull Request 1174`_
* Improve dockstore_init `Pull Request 1177`_

---------------------
0.74.4 (2021-06-01)
---------------------

* Relicense under the MIT license `Pull Request 1169`_
* Revise log levels (thanks to `@bernt-matthias`_). `Pull Request 1165`_
* Create upload_data subcommand (thanks to `@simonbray`_). `Pull Request
  1164`_
* Create ``--download_outputs`` flag for the ``run`` command
  (thanks to `@simonbray`_).
  `Pull Request 1157`_
* Make simultaneous file upload configurable for the run and test commands
  (thanks to `@simonbray`_).
  `Pull Request 1156`_
* Add option to add tags to a history with the ``run`` command
  (thanks to `@simonbray`_). `Pull Request 1154`_
* Revise Allure_ reporting experience for workflows. `Pull Request 1152`_

---------------------
0.74.3 (2021-02-25)
---------------------

* Load both cat1 versions when testing workflows `Pull Request 1146`_
* Fix isolated virtualenv not getting activated `Pull Request 1145`_
* Use bioblend's make_get_request for authenticated request `Pull Request 1144`_
* Display live logs when Galaxy is run in background `Pull Request 1142`_

---------------------
0.74.2 (2021-02-21)
---------------------

* Allow testing dir of workflows `Pull Request 1095`_
* Fix container register for gh workflow `Pull Request 1135`_, `Pull Request 1133`_
* Don't fail URL linting if blocked by CloudFlare `Pull Request 1134`_
  1133`_
* Allow planemo run to stage exisiting datasets and relative paths (thanks to `@simonbray`_).
  `Pull Request 1128`_

---------------------
0.74.1 (2021-01-03)
---------------------

* Fix ``ci_find_tools`` and ``ci_find_repos`` commands. `Pull Request 1127`_

---------------------
0.74.0 (2020-12-30)
---------------------

* Allow running Galaxy workflow tests against externally defined workflows.
  `Pull Request 1126`_, `Pull Request 1125`_,
  `Pull Request 1123`_
* Require Python ``tabulate`` package for the ``list_invocations`` command.
  `Pull Request 1124`_

---------------------
0.73.0 (2020-12-28)
---------------------

* Integrate important features from gxwf_ for running workflows - including
  building up profile commands for creating aliases, allowing referencing workflows
  by external IDs, and listing invocations (thanks to `@simonbray`_).
  `Pull Request 1076`_
* Documentation for using ``planemo run`` to execute workflows (thanks to `@simonbray`_).
  `Pull Request 1102`_
* Add ``workflow_upload`` command for publishing each workflow of a repository with many
  workflows to their own standalone repository.
  `Pull Request 1091`_
* Update github commands to authenticate with a token rather than
  username/password (thanks to `@simonbray`_).
  `Pull Request 1083`_
* Document "advanced" tool test debugging (thanks to `@bernt-matthias`_).
  `Pull Request 1108`_
* Various fixes for workflow commands - including ``workflow_convert``, 
  ``workflow_lint``, ``workflow_job_init``, and ``workflow_test_init``
  (thanks to `@simonbray`_).
  `Pull Request 1101`_, `Pull Request 1118`_, `Pull Request 1121`_,
  `Pull Request 1116`_, `Pull Request 1064`_
* Allow outputting test results as Allure_ framework results.
  `Pull Request 1115`_
* Fix ``run_tests.sh`` invocation `Pull Request 1099`_
* Tiny typo in debugging output (thanks to `@abretaud`_). `Pull Request 1066`_
* Fix typo in 'planemo test' help text for --skip_venv (thanks to
  `@peterjc`_).
  `Pull Request 1068`_
* Fixes for CLI when ``external_galaxy`` is used as the engine (thanks to
  `@simonbray`_).
  `Pull Request 1072`_
* Updating base image to 20.05 for training topics
  (thanks to `@bedroesb`_).
  `Pull Request 1074`_
* Changes to update_test_data testing mode (thanks to `@simonbray`_).
  `Pull Request 1079`_
* Fix docker options when filling ``job_conf.xml`` template.
  `Pull Request 1086`_
* Explicit tests for Galaxy 20.09. `Pull Request 1093`_
* Minor fix for ``ci_find_repos`` command. `Pull Request 1094`_
* Fix a couple of Cheetah_ urls in Galaxy tool documentation (thanks to `@martenson`_).
  `Pull Request 1096`_
* Fix doc link from a redirect loop to a section (thanks to `@martenson`_).
  `Pull Request 1110`_
* Clarify ``tutorial.md`` usage of citations (thanks to `@blankenberg`_).
  `Pull Request 1114`_
* Fix ``ZeroDivisionError`` when no tests are executed (thanks to `@simonbray`_).
  `Pull Request 1120`_

---------------------
0.72.0 (2020-08-04)
---------------------

* More documentation/support around running workflows including new command
  to initialize workflow jobs ``workflow_init_job``.
  `Pull Request 1052`_
* Workflow tests and documentation for tagging inputs. `Pull Request 1058`_
* Various documentation improvements.
  `Pull Request 1061`_, `Pull Request 1062`_
* Add mypy type checking. `Pull Request 1060`_
* Progress decoupling Planemo's core from click & CLI interactions.
  `Pull Request 1059`_
* Tests for workflow testing script. `Pull Request 821`_

---------------------
0.71.0 (2020-08-03)
---------------------

* Drop Python 2 support. `Pull Request 1026`_
* Rev Galaxy dependencies - including bumping bioblend to 0.14.0, galaxy-tool-util,
  and unpinning cwltool (last of these thanks to thanks to `@TMiguelT`_).
  `Pull Request 1038`_, `Pull Request 1034`_
* Workflow linting, best practices, and tooling to assist in following them.
  `Pull Request 1028`_, `Pull Request 1049`_, `Pull Request 1051`_
  `Pull Request 1044`_
* Substantial rewrites to Galaxy workflow input staging - including allow nested
  collection and composite inputs to Galaxy for ``run`` and ``test``.
  `Pull Request 900`_, `Pull Request 1029`_
* Remove assorted older, likely unused commands. `Pull Request 1043`_
* Update installation.rst (thanks to `@mblue9`_). `Pull Request 1032`_
* Automatic PyPI upload on tag using GitHub Actions.
  `Pull Request 994`_
* Fix quay repository presence check for single target builds.
  `Pull Request 993`_
* More fine grained options for ``--shed_install`` (thanks to `@AndreasSko`_).
  `Pull Request 1001`_
* Change default Python version for Galaxy (thanks to `@bernt-matthias`_).
  `Pull Request 1021`_
* Sort tests by id when merging (thanks to `@bernt-matthias`_).
  `Pull Request 1022`_
* Add ``--group_tools`` option to ``ci_find_tools``
  (thanks to `@bernt-matthias`_).
  `Pull Request 1008`_
* Add shared data library path to the data upload box for training material
  (thanks to `@shiltemann`_).
  `Pull Request 1013`_
* Add support for tool versions to tutorial template generator (thanks to
  `@shiltemann`_). `Pull Request 1041`_
* Only copy test files if they don't exist. `Pull Request 1037`_
* Improvements to loading stock tools for workflow testing and serving (
  add new stock tools to list and check subworkflows).
  `Pull Request 1031`_
* Fix link for composite data type docs (thanks to `@bernt-matthias`_).
  `Pull Request 1020`_
* Do not use ``gi._make_url()`` internal BioBlend method.
* Switch CWL examples to use https://schema.org/version/latest/schema.rdf
  (thanks to `@mr-c`_).
  `Pull Request 1015`_
* Fix docs not to claim Galaxy can't run on Python 3.
  `Pull Request 1023`_
* Improved abstractions around target Galaxy instance. `Pull Request 1046`_
* Add empty refgenie config for tests (thanks to `@blankenberg`_).
  `Pull Request 1025`_
* Substantial reworking of testing infrastructure.
  `Pull Request 1024`_, `Pull Request 1003`_,
  `Pull Request 1011`_, `Pull Request 1006`_,
  `Pull Request 1040`_, `Pull Request 1036`_,
  `Pull Request 1042`_

---------------------
0.70.0 (2020-01-29)
---------------------

* Temporarily add galaxy-util requirement `Pull Request 991`_
* Make symlinks in tool tree work for planemo test `Pull Request 988`_
* Reduce use of ``shell=True`` in subprocesses `Pull Request 989`_
* Drop planemo database seed option `Pull Request 985`_
* Don't execute ``untar_to()`` subprocesses through the shell `Pull Request  984`_
* Allow setting database_connection for planemo test runs `Pull Request 986`_
* Fix copy-paste mistakes `Pull Request 983`_
* Add planemo list_repos command `Pull Request 982`_
* Make container_register build files with headers and include base_image `Pull Request 980`_
* Replace deprecated galaxy-lib requirement with galaxy-tool-util `Pull  Request 978`_
* Close all opened files (thanks to `@bernt-matthias`_). `Pull Request 979`_
* Build single requirement container, log if requirement not in best-practice channels `Pull Request 977`_
* Use tojson jinja2 filter instead of json.dumps `Pull Request 975`_
* Add merge_test_reports command `Pull Request 974`_
* Implement github workflow and fix profile commands if psql unavailable `Pull Request 976`_
* Fix planemo lint --biocontainers if no build number in container `Pull Request 972`_
* Update a training command (thanks to `@hexylena`_). `Pull Request 973`_
* Allow passing through GALAXY_VIRTUAL_ENV variable to venv setup `Pull Request 971`_
* Correct help text (thanks to `@hexylena`_). `Pull Request 970`_
* Remove unneeded html5lib requirement `Pull Request 968`_

---------------------
0.62.1 (2019-10-14)
---------------------

* Init & update submodules when installing and creating packages. Stop
  distributing eggs (thanks to `@nsoranzo`_). 1ab8530_

---------------------
0.62.0 (2019-10-11)
---------------------

* Use ``unicodify()`` on exceptions and subprocess outputs (thanks to
  `@nsoranzo`_) `Pull Request 944`_
* Do not override ``None`` with empty string (thanks to `@ic4f`_). `Pull Request
  950`_
* Update Docker template for training material generation (thanks to
  `@bedroesb`_). `Pull Request 958`_
* Add support for suite of repos with different owners (thanks to `@nsoranzo`_).
  `Pull Request 959`_
* Link for collection details updated in the docs (thanks to `@martin-raden`_).
  `Pull Request 963`_
* Move most tests to Python 3.7, drop Python 3.4 (thanks to `@nsoranzo`_).
  `Pull Request 964`_
* Remove confusing warning `Pull Request 966`_

---------------------
0.61.0 (2019-07-08)
---------------------

* Training - fix empty repeat + some formatting (thanks to `@bebatut`_). `Pull
  Request 926`_
* Training - add bibliography to tutorial template (thanks to `@shiltemann`_).
  `Pull Request 938`_
* Training - support new class definition for input in workflow step (thanks to
  `@bebatut`_). `Pull Request 943`_
* Various tool tutorial fixes ahead of GCC 2019 (thanks to `@nsoranzo`_).
  `Pull Request 940`_
* Return validation error if doi is empty (thanks to `@nsoranzo`_).
  `Pull Request 937`_

---------------------
0.60.0 (2019-05-31)
---------------------

* Return validation error if doi is empty `Pull Request 937`_
* Add junit as test reporter (thanks to `@selten`_). `Pull Request 935`_
* Update galaxy.xsd for new python 3 compatibility attribute (thanks to `@martenson`_). `Pull Request
  931`_
* Documentation: add a little warning for <param ... multiple="true"> (thanks to
  `@bernt-matthias`_). `Pull Request 930`_

---------------------
0.59.0 (2019-05-09)
---------------------

* Add ability to test data manager tools (thanks to `@mvdbeek`_).
  `Pull Request 912`_
* Update Training for new requirement definition (thanks to `@bebatut`_).
  `Pull Request 913`_
* Drop amqp workaround (thanks to `@mvdbeek`_). `Pull Request 917`_
* Use ``yaml.safe_load()`` instead of deprecated ``load()`` (thanks to `@nsoranzo`_).
  `Pull Request 921`_
* Allow converting ``tool_test_report.json`` to xunit (thanks to `@mvdbeek`_).
  `Pull Request 918`_
* Fix error if testcase.data.job does not exist (thanks to `@mvdbeek`_).
  `Pull Request 924`_
* Fix deprecated ``getchildren()`` (thanks to `@nsoranzo`_).
  `Pull Request 925`_

---------------------
0.58.2 (2019-03-01)
---------------------

* Fix display of tool ids in planemo html report (thanks to `@mvdbeek`_).
  `Pull Request 908`_
* Single quotes for file names (thanks to `@bernt-matthias`_). `Pull Request
  909`_
* Fix doc linting (thanks to `@mvdbeek`_). `Pull Request 910`_
* Update TS categories (thanks to `@nsoranzo`_). 07dc6e0_
* Close tag in doc help, to help with copy&paste (thanks to `@blankenberg`_).
  `Pull Request 914`_
* Update the tool XSD file (thanks to `@bgruening`_). `Pull Request 915`_

---------------------
0.58.1 (2019-01-03)
---------------------

* Update galaxy-lib requirement to 18.9.2 to add Python 3.7 support (thanks to
  `@nsoranzo`_). `Pull Request 906`_
* Fix command run by `planemo test --skip_venv` (thanks to `@nsoranzo`_).
  `Pull Request 907`_

---------------------
0.58.0 (2019-01-01)
---------------------

* Remove deprecated ``sudo: false`` from .travis.yml (thanks to `@nsoranzo`_).
  `Pull Request 902`_
* Do not skip Galaxy client build for ``planemo serve``. Install Galaxy when the
  directory specified with ``--galaxy_root`` does not exist or is empty. (thanks
  to `@nsoranzo`_). `Pull Request 895`_, `Issue 845`_

---------------------
0.57.1 (2018-11-23)
---------------------

* Fix username validation for shed linting (thanks to `@martenson`_).
  `Pull Request 899`_, `Issue 898`_

---------------------
0.57.0 (2018-11-19)
---------------------

* Allow ``workflow_convert`` to convert a native ``.ga`` workflows to format 2 (yaml).
  `Pull Request 896`_
* New command (``workflow_edit``) to open workflow in a synchronized graphical editor.
  `Pull Request 894`_
* Conda tutorial fixes (thanks to `@nsoranzo`_). `Pull Request 876`_
* Enable ``--conda_use_local`` option for ``planemo test`` (thanks to
  `@nsoranzo`_). `Pull Request 876`_
* When testing, skip workflow outputs that do not have a `label` set (thanks to
  `@bgruening`_). `Pull Request 893`_
* Add ``__repr__`` for ``TestCase`` to improve debugging Planemo
  (thanks to `@bgruening`_). `Pull Request 892`_
* Increase IO polling interval over time (thanks to `@martenson`_).
  `Pull Request 891`_
* Sync galaxy xsd and fix tests (thanks to `@mvdbeek`_).
  `Pull Request 889`_
* Linting fix for ``W605`` (thanks to `@martenson`_). `Pull Request 888`_
* Add icon for repeat parameters in training (thanks to `@bebatut`_).
  `Pull Request 887`_

---------------------
0.56.0 (2018-10-30)
---------------------

* Allow selection of Python version when starting managed Galaxy
  (thanks to `@mvdbeek`_). `Pull Request 874`_
* Change the channel priority of conda (again). (thanks to `@bgruening`_).
  `Pull Request 867`_
* Some small english corrections (thanks to `@hexylena`_). `Pull Request 868`_
* Print the list of excluded paths when running ``ci_find_repos``
  (thanks to `@nsoranzo`_). `Pull Request 877`_
* Improved XSD lint reporting. `Pull Request 871`_
* Fix Planemo writing a file called ``gx_venv_None``. `Pull Request 870`_
* Update cwltool and galaxy-lib dependencies for Python 3.7 (thanks to
  `@nsoranzo`_). `Pull Request 864`_
* Fix to make workflow testing more robust.
  `Pull Request 882`_

---------------------
0.55.0 (2018-09-12)
---------------------

* Add commands to create Galaxy training materials (thanks to `@bebatut`_).
  `Pull Request 861`_
* Fix `planemo test` when TEMP env variable contain spaces (thanks to
  `@nsoranzo`_).
  `Pull Request 851`_
* Support testing a completely remote galaxy instance (thanks to `@hexylena`_).
  `Pull Request 856`_
* Allow naming history from command line (thanks to `@hexylena`_).
  `Pull Request 860`_
* Sync galaxy.xsd from galaxy repo (thanks to `@nsoranzo`_).
  `Pull Request 866`_
* Fix ServeTestCase.test_shed_serve test (thanks to `@nsoranzo`). bad810a_

---------------------
0.54.0 (2018-06-06)
---------------------

* Better support for testings against different versions of Galaxy efficiently and robustly.
  `Pull Request 849`_
* New database version (thanks to `@bgruening`_).
  `Pull Request 847`_
* Hyperlink DOIs against preferred resolver (thanks to `@katrinleinweber`_).
  `Pull Request 850`_
* Tests for collection inputs to workflows. `Pull Request 843`_
* Bring in Ephemeris sleep function - hopefully makes serve tests a bit more robust.
  b12b117_
* More tutorial testing, tutorial updates.
  016b923_, 324c776_, 2002b49_
* More isolated ``test_shed_upload.py`` tests. 72d2ca7_
* Add filetype support for workflow test inputs (thanks to `@bgruening`_).
  `Pull Request 842`_
* Add ``--no_shed_install`` option, to prevent shed installs as part of workflow testing.
  `Pull Request 841`_
* Small docs fix (thanks to `@hexylena`_). `Pull Request 848`_

---------------------
0.53.0 (2018-05-22)
---------------------

* Make Planemo testing easier for CWL tools and workflows in various ways and update
  tutorials to reflect these simplifications. `Pull Request 837`_
* Test and fix running workflow tests against externally managed Galaxy servers.
  `Pull Request 833`_, `Pull Request 836`_
* Allow using URIs for inputs of workflow test. `Pull Request 840`_
* Slide Galaxy testing window to include 18.05 and drop 17.09. `Pull Request 838`_

---------------------
0.52.0 (2018-05-20)
---------------------

* Allow optional disabling of Galaxy single user mode. `Pull Request 835`_
* Fix for path pasting options during workflow testing. `Pull Request 834`_

---------------------
0.51.0 (2018-05-19)
---------------------

* Fix essentially all Conda_ and BioContainers_ related functionality to allow parity between
  CWL_ and existing Galaxy functionality - fixes and enhances many commands including ``lint``,
  ``conda_install``, ``conda_env``, ``test``, ``run``, and ``mull``.
  `Pull Request 828`_
* Add two new tutorials for `Conda
  <http://planemo.readthedocs.io/en/latest/writing_advanced_cwl.html#dependencies-and-conda>`__
  and `Container
  <http://planemo.readthedocs.io/en/latest/writing_advanced_cwl.html#dependencies-and-containers>`__
  development with CWL tools that mirrors the existing tutorials for Galaxy tools - including new
  CWL exercises, answers, and example project templates.
  347c622_
* Improve the CWL generated by the ``tool_init`` command to properly deal with
  ``SoftwareRequirement`` s and generate more idiomatic CWL.
  `Pull Request 820`_, a5c72e3_
* Add new engine type (``--engine toil``) for testing and running CWL_ tools (requires
  manually installing Toil_ with ``pip install toil`` in Planemo's environment).
  `Pull Request 831`_
* Add `documentation <http://planemo.readthedocs.io/en/latest/test_format.html>`__
  for the Galaxy Workflow and CWL_ test format files (includes information on configuring
  various test engines).
  `Pull Request 832`_
* Better default logging config for CWL development. `Pull Request 830`_
* Various fixes for the ``conda_search`` command. `Pull Request 826`_
* Fix test coverage configuration. `Pull Request 822`_
* Reorganize .travis.yml for clarity. `Pull Request 829`_
* More isolated, robust unit tests that use git_.
  `Pull Request 827`_, `Pull Request 818`_
* Fix default list of best-practice Conda channels. `Pull Request 825`_
* Refactor tests to speed up quick tests - fewer buggy URLs fetched in "quick" mode.
  `Pull Request 823`_
* Fix upload configuration of workflow testing to default (overrideable) external Galaxies
  to not use path pasting.
  `Pull Request 816`_
* Fix test number parsing for workflow tests. `Pull Request 817`_

---------------------
0.50.1 (2018-05-11)
---------------------

* Fix the process of waiting on Galaxy to boot up for the Docker Galaxy container ``--engine``.

---------------------
0.50.0 (2018-05-10)
---------------------

* Fixes and small CLI tweaks to get the Docker Galaxy container working as an ``--engine`` for the
  run, serve, and test commands.

---------------------
0.49.2 (2018-05-09)
---------------------

* Various small fixes for new external Galaxy engine type.

---------------------
0.49.1 (2018-05-06)
---------------------

* Fix PyPI_ README rendering for 0.49.0 release changes.

---------------------
0.49.0 (2018-05-06)
---------------------

* Implement external Galaxy engine. `Pull Request 781`_
* Restructure serve testing code for reuse. `Pull Request 795`_
* Improve test report handling for JSON generated via galaxy-lib testing
  script. `Pull Request 799`_
* Improve how various branches of Galaxy are tested. `Pull Request 800`_
* Added documentation for ``GALAXY_MEMORY_MB`` (thanks to `@bernt-matthias`_).
  `Pull Request 801`_
* Log tool config in verbose logging mode. `Pull Request 802`_
* Replace ``r`` channel with ``conda-forge`` (thanks to `@bgruening`_).
  `Pull Request 805`_
* Sync ``galaxy.xsd`` with latest Galaxy updates (thanks to `@nsoranzo`_).
  `Pull Request 806`_
* Use ``requests.get()`` when validating http URLs (thanks to `@nsoranzo`_).
  `Pull Request 809`_
* Do not consider tools with "deprecated" in the path (thanks to
  `@bgruening`_). `Pull Request 810`_
* Automatically load tools shipped with Galaxy when testing, running, or serving
  workflows that reference these tools. `Pull Request 790`_
* Revise README and touch up documentation in general. `Pull Request 787`_
* Various small changes to testing and test framework. `Pull Request 792`_
* Various Python 3 fixes. 8cfe9e9_, 41f7df1_
* Fixes for Galaxy 18.0X releases.
  `Pull Request 803`_, dc443d6_

---------------------
0.48.0 (2018-02-28)
---------------------

* Run all CI tests against Python 3 (thanks to `@nsoranzo`_).
  `Pull Request 768`_ and `Pull Request 774`_
* Python 3 fix - subprocess with ``universal_newlines=True``
  (thanks to `@peterjc`_).
  `Pull Request 764`_
* Record CWL_ conformance test results using JUnit xml
  (thanks to `@mr-c`_).
  `Pull Request 756`_
* Restore run test case for simple Galaxy tools.
  `Pull Request 769`_
* Enhancements to Galaxy profiles and workflow testing.
  `Pull Request 773`_
* Fix resolving & installing shed repositories from workflows for ``test``
  and ``run`` commands.
  `Pull Request 776`_
* Implement planemo command to convert format 2 workflows into .ga workflows.
  `Pull Request 771`_
* Add a native Galaxy workflow (.ga) testing test.
  `Pull Request 770`_
* Drop Brew support but add more detailed install instructions.
  `Pull Request 761`_
* Clean up CWL_ conformance test execution. `Pull Request 753`_
* Assorted small CWL_ and deamon serve fixes. `Pull Request 759`_


---------------------
0.47.0 (2017-11-18)
---------------------

* Update to the latest Galaxy tool XSD  (thanks to `@nsoranzo`_).
  `Pull Request 747`_
* Re-fix problem when shed_update would fail if nothing to update
  (thanks to `@nsoranzo`_). `Pull Request 747`_
* Update instructions for installation via conda (thanks to `@nsoranzo`_) .
  `Pull Request 743`_
* Bug fix for MacOS `chmod` doesn't support `--recursive` flag.
  (thanks to `@dfornika`_). `Pull Request 739`_
* Bug fix to also `socket.error` when linting URLs
  (thanks to `@nsoranzo`_). `Pull Request 738`_
* Disable broken tests. `Pull Request 745`_

---------------------
0.46.1 (2017-09-26)
---------------------

* Rev to latest versions of bioblend_ and `galaxy-lib`_ for various fixes
  related to CWL_.

---------------------
0.46.0 (2017-09-15)
---------------------

* Change behavior of ``--docker`` flag, for a few releases it would require
  Galaxy use a container for every non-upload tool. This breaks various
  conversion tools for instance and so was reverted.
  `Pull Request 733`_
* Add 'Accept' header when linting doc URLs (thanks to `@nsoranzo`_).
  `Pull Request 725`_
* Fix `--conda_auto_install` help (thanks to `@nsoranzo`_).
  `Pull Request 727`_
* Incremental progress toward CWL support via Galaxy.
  `Pull Request 729`_, `Pull Request 732`_
* Update galaxy-lib to latest version to fix various issues.
  `Pull Request 730`_
* Fix lint detected problems with documentation.
  `Pull Request 731`_

---------------------
0.45.0 (2017-09-06)
---------------------

* Update to the latest `galaxy-lib`_ for Conda fixes. (thanks `@nsoranzo`_)
  and updated CWL_ utilities.  `Pull Request 716`_, `Pull Request 723`_
* Update Conda_ channel order to sync with Bioconda_
  (thanks to `@nsoranzo`_). `Pull Request 715`_
* Experimental support running CWL_ workflows through the CWL_ fork of Galaxy.
* Mention ``planemo command --help`` in main help
  (thanks to `@peterjc`_). `Pull Request 709`_
* Bugfix handle ``None`` requirement versions when registering containers
  (thanks to `@bgruening`_). `Pull Request 704`_
* Bugfix for dependencies by pinning ruamel.yaml version
  (thanks to `@mvdbeek`_). `Pull Request 720`_

---------------------
0.44.0 (2017-06-22)
---------------------

* Fix and improve Galaxy root option specification options.
  `Pull Request 701`_, 8a608e0_
* Update `planemo mull` to use a default action of `build-and-test` since
  `build` no longer cleans up itself. ecc1bc2_
* Add a command to pre-install Involucro_.
  `Pull Request 702`_

---------------------
0.43.0 (2017-06-22)
---------------------

* Remove stdio from generated tools - just use exit_code for everything.
  91b6fa0_
* Implement some ad-hoc documentation tests. `Pull Request 699`_
* A large number of small enhancements and fixes for the documentation and
  example projects.

---------------------
0.42.1 (2017-06-16)
---------------------

* Fix Readme typos (thanks to `@manabuishii`_) 904d77a_
* Fix `container_register` to create pull requests against the newly finalized home of the
  multi-package-containers registry repository.
  9636682_
* Fix `use_global_config` and `use_env_var` for options with unspecified defaults.
  475104c_


---------------------
0.42.0 (2017-06-15)
---------------------

* Conda/Container documentation and option naming improvements. `Pull Request
  684`_
* Sync `galaxy.xsd` with latest upstream Galaxy updates (thanks to `@nsoranzo`_).
  `Pull Request 687`_
* Fix `ci_find_repos` command to not filter repos whose only modifications where
  in subdirs (thanks to `@nsoranzo`_).
  `Pull Request 688`_
* Update `container_register` for mulled version 2 and repository name changes.
  `Pull Request 689`_
* Better pull request messages for the `container_register` command.
  `Pull Request 690`_

---------------------
0.41.0 (2017-06-05)
---------------------

* Fix ``shed_update`` not fail if there is nothing to update
  (thanks to `@nsoranzo`_). `Issue 494`_, `Pull Request 680`_
* Conda documentation and option naming improvements.
  `Pull Request 683`_
* Implement ``container_register`` for tool repositories.
  `Pull Request 675`_
* Fix ``hub`` binary installation for Mac OS X.
  `Pull Request 682`_

---------------------
0.40.1 (2017-05-03)
---------------------

* Fix data manager configuration to not conflict with original Galaxy at
  ``galaxy_root`` (thanks to `@nsoranzo`_). `Pull Request 662`_
* Fix ``filter_paths()`` to not partial match paths when filtering shed repositories
  (thanks to `@nsoranzo`_). `Pull Request 665`_
* Fix description when creating ``.shed.yml`` files (thanks to `@RJMW`_).
  `Pull Request 664`_

---------------------
0.40.0 (2017-03-16)
---------------------

* Implement instructions and project template for GA4GH Tool Execution
  Challenge Phase 1. 84c4a73_
* Eliminate Conda hack forcing ``/tmp`` as temp directory. b4ae44d_
* Run dependency script tests in isolated directories. 32f41c9_
* Fix OS X bug in ``planemo run`` by reworking it to wait using urllib instead of sockets.
  3129216_

---------------------
0.39.0 (2017-03-15)
---------------------

* Implement documentation and examples for Conda-based dependency development (under
  "Advanced" topics).
  `Pull Request 642`_, `Pull Request 643`_
* Implement documentation and examples for container-based dependency development (under
  "Advanced" topics).
  0a1abfe_
* Implement a ``planemo conda_search`` command for searching best practice channels
  from the command line.
  `Pull Request 642`_
* Allow Planemo to work with locally built Conda packages using the ``--conda_use_local``
  command.
  `Pull Request 643`_, `Issue 620`_
* Implement an ``open`` (or just ``o``) command to quickly open the last test results
  (or any file if supplied). `Pull Request 641`_
* Linting improvements and fixes due to `galaxy-lib`_ update.
  * WARN on test output names not found or not matching.
  * INFO correct information about stdio if profile version is found.
  * WARN if profile version is incorrect.
  * INFO profile version
  * Fix ``assert_command`` not detected as a valid test (fixes  `Issue 260`_).
* Have ``lint --conda_requirements`` check that at least one actual requirement is found.
  6638caa_
* Allow ``conda_install`` to work with packages as well as just tools.
  8faf661_
* Add ``--global`` option to conda_install to install requirements into global Conda setup
  instead of using an environment.
  8faf661_
* Implement ``planemo lint --biocontainer`` that checks that a tool has an available BioContainer
  registered.
  0a1abfe_
* Add more options and more documentation to the ``planemo mull`` command.
  0a1abfe_
* Hack around a bug in Conda 4.2 that makes it so ``planemo mull`` doesn't work out of the box on
  Mac OS X.
  0a1abfe_
* Allow URIs to be used instead of paths for a couple operations. ce0dc4e_
* Implement non-strict CWL parsing option. 4c0f100_
* Fixes for changes to cwltool_ and general CWL-relate functionality.
  3c95b7b_, 06bcf19_, 525de8f_, 9867e56_, 9ab4a0d_
* Eliminate deprecated XML-based abstraction from ``planemo.tools``. 04238d3_
* Fix ``MANIFEST.in`` entry that was migrated to galaxy-lib. ced5ce2_
* Various fixes for the command ``conda_env``. `Pull Request 640`_
* Improved command help - both formatting and content. `Pull Request 639`_
* Implement a ``--no_dependency_resolution`` option disabling conda dependency
  resolver.
  `Pull Request 635`_, `Issue 633`_
* Tests for new linting logic. `Pull Request 638`_
* Fix bug where tool IDs needs to be lowercase for the shed (thanks to
  `@bgruening`_).
  `Pull Request 649`_
* Update seqtk version targetted by intro docs. e343b67_
* Various other Conda usability improvements. `Pull Request 634`_

---------------------
0.38.1 (2017-02-06)
---------------------

* Fix bug with ``shed_lint --urls`` introduced in 0.38.0.
  84ebc1f_

---------------------
0.38.0 (2017-02-06)
---------------------

* Trim down the default amount of logging during testing.
  `Pull Request 629`_, `Issue 515`_
* Improved log messages during shed operations. 08c067c_
* Update tool XSD against latest Galaxy.
  fca4183_, 03c9658_
* Fix bug where ``shed_lint --tools`` for a suite lints the same tools multiple
  times.
  `Issue 564`_, `Pull Request 628`_

---------------------
0.37.0 (2017-01-25)
---------------------

* Update to the latest `galaxy-lib`_ release. This means new installs start with
  Miniconda 3 instead of Minicoda 2 and at a newer version. This fixes many
  Conda_ related bugs.
* Change defaults so that Conda automatically initializes and performs tool installs
  by default from within the spawned Galaxy server. The trio of flags
  ``--conda_dependency_resolution``, ``--conda_auto_install``, and ``--conda_auto_init``
  are effectively enabled by default now. 4595953_
* Use the Galaxy cached dependency manager by default (thanks to `@abretaud`_).
  `Pull Request 612`_
* Test Conda dependency resolution for more versions of Galaxy including the forthcoming
  release of 17.01.
* Update to the latest Galaxy tool XSD for various tool linting fixes. 32acd68_
* Fix pip ignores for ``bioconda_scripts`` (thanks to `@nturaga`_)
  `Pull Request 614`_

---------------------
0.36.1 (2016-12-12)
---------------------

* Fix move error when using ``project_init``.
  `Issue 388`_, `Pull Request 610`_
* Improved integration testing for ``test`` command. `Pull Request 609`_
* Update CWL links to v1.0 (thanks to `@mr-c`_).
  `Pull Request 608`_

---------------------
0.36.0 (2016-12-11)
---------------------

* Bring in latest tool XSD file from Galaxy (thanks to `@peterjc`_).
  `Pull Request 605`_
* PEP8 fixes for various linting problems
  (thanks to `@peterjc`_).
  `Pull Request 606`_
* Update tool syntax URL to new URL (thanks to `@mvdbeek`_).
  `Pull Request 602`_

---------------------
0.35.0 (2016-11-14)
---------------------

* Native support for building bioconductor tools and recipes
  (thanks to `@nturaga`_). `Pull Request 570`_
* Fixes for running Galaxy via docker-galaxy-stable (thanks to
  `@bgruening`_). 50d3c4a_
* Import order linting fixes (thanks to `@bgruening`_).

---------------------
0.34.1 (2016-10-12)
---------------------

* Mimic web browser to validate user help URLs fixing `Issue 578`_
  (thanks to `@peterjc`_). `Pull Request 591`_
* Fix for Bioconda recipes depending on ``conda-forge`` (thanks to `@nsoranzo`_).
  `Pull Request 590`_


---------------------
0.34.0 (2016-10-05)
---------------------

* Implement ``mull`` command to build containers for tools based on Conda_
  recipes matching requirement definitions. 08cef54_
* Implement ``--mulled_containers`` flag on ``test``, ``serve``, and ``run``
  commands to run tools in "mulled" containers. Galaxy will first search
  locally cache containers (such as ones built with ``mull``), then search
  the mulled namespace of `quay.io`_, and finally build one on-demand if
  needed using `galaxy-lib`_ and Involucro_ developed by `@thriqon`_.
* Implement ``--conda_requirements`` flag on ``lint`` command to ensure requirements
  can be resolved in best practice channels. 9da8387_
* Allow ``conda_install`` command over multiple tool paths. 2e4e5fc_
* Update pip_ as part of setting virtual environment in ``Makefile`` target.
  19b2ee9_
* Add script to auto-update Bioconda_ recipe for Planemo and open a pull request.
  f0da66f_

---------------------
0.33.2 (2016-09-28)
---------------------

* Fix HISTORY.rst link problem that prevented correct display of content on PyPI_.

---------------------
0.33.1 (2016-09-28)
---------------------

* Fix ``lint --urls`` false positives by being more restrictive with what is considered a URL
  (fixed by `@hexylena`_ after detailed report from `@peterjc`_).
  `Issue 573`_, `Pull Request 579`_

---------------------
0.33.0 (2016-09-23)
---------------------

* Enable XSD validation of tools by default (restore old behavior with
  ``planemo lint --no_xsd``). 1ef05d2_
* Implement a ``conda_lint`` command to lint Conda_ recipes based
  on `anaconda-verify`_. 6a6f164_
* Implement ``clone`` and ``pull_request`` commands to ease PRs
  (with documentation fixes from `@martenson`_).
  e925ba1_, ea5324f_
* Update `galaxy.xsd`_ to allow version_command's to have an interpreter
  attribute. 7cca2e4_
* Apply improvement from `@nsoranzo`_ for Planemo's use of
  `git diff <https://git-scm.com/docs/git-diff>`__.
  6f91719_
* Pull in downstream refactoring of ``tool_init`` code from `@nturaga`_'s
  Bioconductor_ work. ccdd2d5_
* Update to latest `Tool Factory`_ code from `tools-iuc`_. ca88b0c_
* Small code cleanups. b6d8294_, d6da3a8_
* Fixup docs in ``planemo.xml.validation``.
* Allow skipping newly required lxml_ dependency in `setup.py`_. 34538de_

---------------------
0.32.0 (2016-09-16)
---------------------

* Enhance ``planemo lint --xsd`` to use a fairly complete and newly official XSD
  definition. `Pull Request 566`_
* Migrate and update documentation related to tool XML macros and handling
  multiple outputs from the Galaxy wiki (with help from `@bgruening`_, `@mvdbeek`_,
  and `@nsoranzo`_). `Pull Request 559`_
* Documentation fixes (thanks to `@ramezrawas`_). `Pull Request 561`_
* Do not fail URL linting in case of too many requests (thanks to `@nsoranzo`_).
  `Pull Request 565`_

---------------------
0.31.0 (2016-09-06)
---------------------

* Implement new commands to ``ci_find_repos`` and ``ci_find_tools`` to ease
  CI scripting.
  `Pull Request 555`_

---------------------
0.30.2 (2016-09-01)
---------------------

* Fix another problem with Conda_ prefix handling when using
  ``--conda_dependency_resolution``. f7b6c7e_

---------------------
0.30.1 (2016-09-01)
---------------------

* Fix a problem with Conda_ prefix handling when using
  ``--conda_dependency_resolution``. f7b6c7e_
* Fix for quote problem in ``update_planemo_recipe.bash``. 6c03de8_
* Fix to restore linting of ``tests/`` directory and fix import order throughout
  module. ef4b9f4_

---------------------
0.30.0 (2016-09-01)
---------------------

* Update to the latest `galaxy-lib`_ release and change Conda_ semantics to match
  recent updates to Galaxy. For the most robust Conda_ usage - use planemo 0.30+
  with Galaxy 16.07 or master.
  07d94bd_
* Implement the ``--conda_auto_init`` flag for ``conda_install``. ca19910_
* Allow the environment variable ``PLANEMO_CONDA_PREFIX`` to set a default
  for ``--conda_prefix``.
  24008ab_
* Fixup documentation regarding installs and Conda_. ce44e87_
* Fix and lint Python module import order throughout project.
  `Pull Request 550`_
* Use ``cp`` rather than symlink to ``$DOWNLOAD_CACHE`` in the
  ``dependency_script`` command (thanks to `@peterjc`_).  c2204b3_
* Fixes for the Homebrew recipe updater. c262b6d_

---------------------
0.29.1 (2016-08-19)
---------------------

* Improved handling of Python 2.7 specific dependencies.

---------------------
0.29.0 (2016-08-19)
---------------------

* Look for sha256sum checksums during shed_lint (thanks to `@peterjc`_).
  `Pull Request 539`_
* An assortment fixes and enhancements to the ``dependency_script`` command
  (thanks to `@peterjc`_). `Pull Request 541`_, `Pull Request 545`_
* Fix shed_build to respect exclude: in .shed.yml (thanks to `@nsoranzo`_).
  `Pull Request 540`_
* Fix linting of tool URLs (thanks to `@nsoranzo`_). `Pull Request 546`_

---------------------
0.28.0 (2016-08-17)
---------------------

* Fixes for bioblend_ v0.8.0 (thanks to `@nsoranzo`_). 9fdf490_
* Enable shed repo type update (thanks to `@nsoranzo`_). 3ceaa40_
* Create suite repositories with repository_suite_definition type by default
  (thanks to `@nsoranzo`_).
  057f4f0_
* Include ``shed_lint`` in script run by ``travis_init`` (thanks to `@peterjc`_).
  `Pull Request 528`_
* Minor polish to the ``travis_init`` command (thanks to `@peterjc`_).
  `Pull Request 512`_
* Update pip_ and setuptools on TravisCI; fix travis_init (thanks to `@peterjc`_).
  `Pull Request 521`_
* Shorten command one line descriptions for main help (thanks to `@peterjc`_).
  `Pull Request 510`_
* Use ``planemo test --no_cache_galaxy`` under TravisCI (thanks to `@peterjc`_).
  `Pull Request 513`_
* Improve and fix docs ahead of GCC 2016 (thanks to `@martenson`_).
  `Pull Request 498`_, 725b232_
* Add description of ``expect_num_outputs`` to planemo FAQ. a066afb_
* Revise planemo tools docs to be more explicit about collection identifiers.
  a811e65_
* Add more docs on existing dynamic tool output features. `Pull Request 526`_
* Fix serve command doc (thanks to `@nsoranzo`_). 8c088c6_
* Fix `make lint-readme` (RST link errors) (thanks to `@peterjc`_).
  `Pull Request 525`_
* Add union bedgraph example to project templates (for GCC demo example).
  d53bcd6_
* Add Flow Cytometry Analysis, Data Export, and Constructive Solid Geometry as
  shed categories (thanks to `@bgruening`_, `@gregvonkuster`_, and `@nsoranzo`_).
  e890ab5_, 08bb354_, e2398fb_
* Remove duplicated attribute in docs/writing/bwa-mem_v5.xml (thanks to
  Paul Stewart `@pstew`_).
  `Pull Request 507`_

---------------------
0.27.0 (2016-06-22)
---------------------

* Use ephemeris to handle syncing shed tools for workflow actions.
  1c6cfbb_
* More planemo testing enhancements for testing artifacts that aren't
  Galaxy tools. `Pull Request 491`_
* Implement ``docker_galaxy`` engine type. eb039c0_, `Issue 15`_
* Enhance profiles to be Dockerized Galaxy-aware. `Pull Request 488`_
* Add linter for DOI type citation - thanks to `@mvdbeek`_.
  `Pull Request 484`_

---------------------
0.26.0 (2016-05-20)
---------------------

* Implement ``Engine`` and ``Runnable`` abstractions - Planemo now has
  beta support for testing Galaxy workflows and CWL_ tools with Galaxy and
  any CWL_ artifact with cwltool_.
  `Pull Request 454`_, 7be1bf5_
* Fix missing command_line in test output json. e38c436_
* More explicit Galaxy ``job_conf.xml`` handling, fixes bugs caused by
  ``galaxy_root`` having existing and incompatible ``job_conf.xml`` files
  and makes it possible to specify defaults with fixed server name. c4dfd55_
* Introduce profile commands (``profile_create``, ``profile_delete``, and
  ``profile_list``) and profile improvements (automatic postgres database
  creation support). `Pull Request 480`_, a87899b_
* Rework Galaxy test reporting to use structured data instead of XUnit
  data. 4d29bf1_
* Refactor Galaxy configuration toward support for running Galaxy in
  docker-galaxy-stable. `Pull Request 479`_

---------------------
0.25.1 (2016-05-11)
---------------------

* Tweak dependencies to try to fix cwltool_ related issues - such
  as `Issue 475`_.

---------------------
0.25.0 (2016-05-11)
---------------------

* Implement Galaxy "profiles" - the ability to configure
  perisistent, named environments for ``serve`` and ``test``.
  5d08b67_
* Greatly improved ``serve`` command - make ``test-data``
  available as an FTP folder, (on 16.07) automatically log
  in an admin user, and many more options (such as those
  required for "profiles" and a ``--daemon`` mode).
* Two fixes to ensure more consistent, dependable ``test`` output.
  `Pull Request 472`_, f3c6917_
* Add code and documentation for linting (``lint``) and
  building (``tool_init``) CWL_ tools. a4e6958_, b0b867e_,
  4cd571c_
* If needed for Conda_ workaround, shorten ``config_directory``
  path (thanks to `@mvdbeek`_). efc5f30_
* Fix ``--no_cache_galaxy`` option (thanks to Gildas Le
  Corguillé). d8f2038_
* Target draft 3 of CWL_ instead of draft 2. 775bf49_
* Fix ``cwltool`` dependency version - upstream changes broke
  compatibility. `65b999d`_
* Add documentation section and slides about recent Galaxy
  tool framework changes (with fix from `@remimarenco`_). 069e7ba_
* Add IUC standards to Planemo docs. 2ae2b49_
* Improve collection-related contents in documentation
  (thanks in part to `@martenson`_).
  fea51fc_, 13a5ae7_
* Add documentation on ``GALAXY_SLOTS`` and running planemo
  on a cluster. 45135ff_, e0acf91_
* Revise command-line handling framework for consistency and
  extension - allow extra options to be configured as
  defaults ``~/.planemo.yml`` including ``--job_config_file``
  and Conda_ configuration options. e769118_, 26e378e_
* Fix ``tool_init`` commans options typos (thanks to
  Nitesh Turaga). 826d371_
* Refactor galaxy-related modules into submodules of a new
  ``planemo.galaxy`` package. 8e96864_
* Fix error message typo (thanks to `@blankenberg`_). b1c8f1d_
* Update documentation for recent command additions. 3f4ab44_
* Rename option ``--galaxy_sqlite_database`` option to
  ``--galaxy_database_seed`` and fix it so it actually works.
  f7554d1_
* Add ``--extra_tools`` option to ``serve`` command. 02a08a0_
* Update project testing to include linting documentation
  (``docs/``), Python import order, and docstrings.
  a13a120_, 6e1e726_, 95d5cba_


---------------------
0.24.2 (2016-04-25)
---------------------

* Revert "check ``.shed.yml`` owner against credentials during shed
  creation", test was incorrect and preventing uploads.
  `Pull Request 425`_, `Issue 246`_

---------------------
0.24.1 (2016-04-08)
---------------------

* Fix test summary report. `Pull Request 429`_
* Improve error reporting when running ``shed_test``. ce8e1be_
* Improved code comments and tests for shed related functionality.
  89674cb_
* Rev `galaxy-lib`_ dependency to 16.4.1 to fix wget usage in
  newer versions of wget. d76b489_

---------------------
0.24.0 (2016-03-29)
---------------------

* Drop support for Python 2.6. 93b7bda_
* A variety of fixes for ``shed_update``.
  `Pull Request 428`_, `Issue 416`_
* Fix reporting of metadata updates for invalid shed updates.
  `Pull Request 426`_, `Issue 420`_
* Check ``.shed.yml`` owner against credentials during shed creation.
  `Pull Request 425`_, `Issue 246`_
* Fix logic error if there is a problem with ``shed_create``. 358a42c_
* Tool documentation improvements. 0298510_, a58a3b8_

---------------------
0.23.0 (2016-02-15)
---------------------

* Fix duplicated attributes with Conda_ resolver (thanks
  to Björn Grüning). `Pull Request 403`_
* Upgrade to latest version of `galaxy-lib`_ for more linting.
* Attempt to better handle conditional dependency on cwltool.

---------------------
0.22.2 (2016-01-14)
---------------------

* Fixed bug targetting forthcoming release of Galaxy 16.01.

---------------------
0.22.1 (2016-01-14)
---------------------

* Fixed problem with PyPI_ build artifacts due to submodule's not
  being initialized during previous release.

---------------------
0.22.0 (2016-01-13)
---------------------

* Add ``--skip_venv`` to support running Galaxy 16.01 inside of
  conda environments. 9f3957d_
* Implement conda support. f99f6c1_, ad3b2f0_, 5e0b6d1_
* Update LICENSE for Planemo to match Galaxy. 15d33c7_
* Depend on new `galaxy-lib`_ on PyPI_ instead of previous hacks....
  `Pull Request 394`_
* Fix egg caching against master/15.10. 6d0f502_
* Fix bug causing shed publishing of ``.svn`` directories.
  `Issue 391`_
* Bug fixes for Conda_ support thanks to `@bgruening`_. 63e456c_
* Fix document issues thanks to `@einon`_.
  `Pull Request 390`_
* Improve client for shed publishing to support newer shed backend
  being developed by `@hexylena`_. `Pull Request 394`_
* Tool Shed ``repo_id`` change, `@hexylena`_. `Pull Request 398`_
* Various other small changes to testing, project structure, and
  Python 3 support.

---------------------
0.21.1 (2015-11-29)
---------------------

* Fix serious regression to ``test`` command. 94097c7_
* Small fixes to release process. 4e1377c_, 94645ed_

---------------------
0.21.0 (2015-11-29)
---------------------

* If ``virtualenv`` not on ``PATH``, have Planemo create one for Galaxy.
  5b97f2e_
* Add documentation section on testing tools installed in an existing
  Galaxy instance. 1927168_
* When creating a virtualenv for Galaxy, prefer Python 2.7.
  e0577e7_
* Documentation fixes and improvements thanks to `@martenson`_.
  0f8cb10_, 01584c5_, b757791_
* Specify a minimum ``six`` version requirement. 1c7ee5b_
* Add script to test a planemo as a wheel. 6514ff5_, `Issue 184`_
* Fix empty macro loading. `Issue 362`_
* Fix an issue when you run ``shed_diff --shed_target local`` thanks
  to Gwendoline Andres and Gildas Le Corguillé at ABiMS Roscoff.
  `Pull Request 375`_
* Fix ``shed_diff`` printing to stdout if ``-o`` isn't specified.
  f3394e7_
* Small ``shed_diff`` improvements to XML diffing and XUnit reporting.
  af7448c_, 83e227a_
* More logging of ``shed_diff`` results if ``--verbose`` flagged.
  9427b47_
* Add ``test_report`` command for rebuilding reports from structured JSON.
  99ee51a_
* Fix option bug with Click 6.0 thanks to `@bgruening`_. 2a7c792_
* Improved error messages for test commands. fdce74c_
* Various fixes for Python 3. 2f66fc3_, 7572e99_, 8eda729_, 764ce01_
* Use newer travis container infrastructure for testing. 6d81a94_
* Test case fixes. 98fdc8c_, 0e4f70a_

---------------------
0.20.0 (2015-11-11)
---------------------

* More complete I/O capturing for XUnit. 6409449_
* Check for select parameter without options when linting tools.
  `Issue 373`_
* Add ``--cwl_engine`` argument to ``cwl_run`` command. dd94ddc_
* Fixes for select parameter linting. 8b31850_
* Fix to demultiplexing repositories after tool uploads. `Issue 361`_
* Fix to update planemo for Galaxy wheels. 25ef0d5_
* Various fixes for Python 2.6 and Python 3.
  c1713d2_, 916f610_, c444855_

---------------------
0.19.0 (2015-11-03)
---------------------

* Initial implementation of ``cwl_run`` command that runs a
  CWL tool and job file through Galaxy. 49c5c1e_
* Add ``--cwl`` flag to ``serve`` to experimentally serve CWL tools
  in Galaxy.
  `Pull Request 339`_
* Implement highly experimental ``cwl_script`` command to convert
  a CWL job to a bash script. 508dce7_
* Add name to all XUnit reports (thanks to `@hexylena`_).
  `Pull Request 343`_
* Capture stdout and stderr for ``shed_diff`` and ``shed_update``
  XUnit reports. `Pull Request 344`_
* More tool linting (conditionals) thanks to `@hexylena`_.
  `Pull Request 350`_
* UTF-8 fixes when handling XUnit reports. `Pull Request 345`_
* Add `Epigenetics` as Tool Shed category. `Pull Request 351`_
* Merge changes to common modules shared between Galaxy, Planemo, and Pulsar (thanks to `@natefoo`_).
  `Pull Request 356`_
* Add ``--cite_url`` to ``tool_init``. fdb1b51_
* ``tool_init`` bug fix. f854138_
* Fix `setup.py`_ for cwltool and bioblend_ changes. 1a157d4_
* Add option to specify template sqlite database locally. c23569f_
* Add example IPython notebooks to docs. c8640b6_

---------------------
0.18.1 (2015-10-22)
---------------------

* Fix issue with test reporting not being populated. 19900a6_

---------------------
0.18.0 (2015-10-20)
---------------------

* Improvements to ``docker_shell`` usability (thanks to `@kellrott`_).
  `Pull Request 334`_
* Add docker pull attempt when missing Dockerfile (thanks to `@kellrott`_).
  `Pull Request 333`_
* Fix bug inferring which files are tool files (thanks to `@hexylena`_).
  `Pull Request 335`_, `Issue 313`_
* Initial work toward automating brew recipe update. 4d6f7d9_, `Issue 329`_

---------------------
0.17.0 (2015-10-19)
---------------------

* Implement basic XUnit report option for ``shed_update`` (thanks to `@martenson`_).
  `Pull Request 322`_
* Fix issues with producing test outputs. 572e754_
* Xunit reporting improvements - refactoring, times, diff output (thanks to `@hexylena`_).
  `Pull Request 330`_
* Implement project governance policy and update developer code of conduct to
  match that of the Galaxy project. `Pull Request 316`_
* Update filters for account for new ``.txt`` and ``.md`` test outputs
  (thanks to `@hexylena`_). `Pull Request 327`_
* Add verbose logging to galaxy test output handling problems. 5d7db92_
* Flake8 fixes (thanks to `@martenson`_). 949a36d_
* Remove uses of deprecated ``mktemp`` Python standard library function
  (thanks to `@hexylena`_). `Pull Request 330`_

---------------------
0.16.0 (2015-10-07)
---------------------

* Adding new command ``dependency_script`` to convert Tool Shed dependencies
  into shell scripts - thanks to `@peterjc`_.
  `Pull Request 310`_, f798c7e_, `Issue 303`_
* Implement profiles in sheds section of the ``~/.planemo.yml``.
  `Pull Request 314`_

---------------------
0.15.0 (2015-10-01)
---------------------

* Template framework for reporting including new markdown and plain
  text reporting options for testing - thanks to `@hexylena`_.
  `Pull Request 304`_
* XUnit style reporting for ``shed_diff`` command - thanks to
  `@hexylena`_. `Pull Request 305`_
* Add new ``shed_build`` command for building repository tarballs -
  thanks to `@kellrott`_. `Pull Request 297`_
* Fix exit code handling for ``lint`` commands - thanks to `@mvdbeek`_.
  `Pull Request 292`_
* Improved documentation for ``serve`` command - thanks to `@lparsons`_.
  `Pull Request 312`_
* Tiny backward compatible Python 3 tweaks for `Tool Factory`_ - thanks
  to `@peterjc`_. dad2d9d_
* Fixed detection of virtual environment in ``Makefile`` - thanks to
  `@lparsons`_. `Pull Request 311`_
* Updates to Galaxy XSD - thanks to `@mr-c`_. `Pull Request 309`_
* Allow reading shed key option from an environment variable.
  `Pull Request 307`_
* Allow specifying host to serve Galaxy using ``-host`` - thanks in
  part to `@chambm`_. `Pull Request 301`_
* Allow specifying defaults for ``-host`` and ``--port`` in
  ``~/.planemo.yml``. `Pull Request 301`_
* Improve ``~/.planemo.yml`` sample comments - thanks to `@martenson`_.
  `Pull Request 287`_
* Update tool shed categories - thanks to `@bgruening`_. `Pull Request 285`_
* Improved output readibility for ``diff`` command - thanks to `@martenson`_. `Pull Request 284`_

---------------------
0.14.0 (2015-08-06)
---------------------

* Allow ``-t`` as shorthand for ``--shed_target`` (thanks to Peter Cock).
  `Pull Request 278`_
* Fix ``tool_init`` command to use ``from_work_dir`` only if file in command
  (thanks to bug report and initial fix outline by Gildas Le Corguillé).
  `Pull Request 277`_
* Various documentation fixes (thanks in part to Peter Cock and Daniel
  Blankenberg). `Pull Request 256`_, `Pull Request 253`_, `Pull Request 254`_,
  `Pull Request 255`_, `Pull Request 251`_, `Issue 272`_

---------------------
0.13.2 (2015-07-06)
---------------------

* Fix project_init for missing files. cb5b906_
* Various documentation improvements.

---------------------
0.13.1 (2015-07-01)
---------------------

* Fix for ``shed_init`` producing non-standard type hints. `Issue 243`_,
  f0610d7_
* Fix tool linting for parameters that define an ``argument`` but not a
  ``name``. `Issue 245`_, aad1eed_
* Many doc updates including a tutorial for developing tools in a test-driven
  fashion and instructions for using the planemo appliance through Kitematic
  (with Kitematic screenshots from E. Rasche).

---------------------
0.13.0 (2015-06-28)
---------------------

* If planemo cannot find a Galaxy root, it will now automatically fetch
  one (specifing ``--galaxy_install`` will still force a fetch).
  `Pull Request 235`_
* `Docuementation <http://planemo.readthedocs.org/en/latest/appliance.html>`__
  has been updated to reflect new and vastly improved Docker and Vagrant
  virtual appliances are now available, as well as a new VirtualBox OVA
  variant.
* Update linting for new tool XML features (including ``detect_errors``
  and output collections). `Issue 233`_, 334f2d4_
* Fix ``shed_test`` help text. `Issue 223`_
* Fix code typo (thanks to Nicola Soranzo). `Pull Request 230`_
* Improvements to algorithm used to guess if an XML file is a tool XML file.
  `Issue 231`_
* Fix configuration file handling bug. `Issue 240`_

---------------------
0.12.2 (2015-05-23)
---------------------

* Fix ``shed_test`` and ``shed_serve`` for test and local tool sheds.
  f3cafaa_

---------------------
0.12.1 (2015-05-21)
---------------------

* Fix to ensure the tab completion script is in the Python source tarball
  (required for setting up tab-completion for Homebrew). 6b4e7a6_

---------------------
0.12.0 (2015-05-21)
---------------------

* Implement a ``--failed`` flag for the ``test`` command to rerun
  previously faied tests. `Pull Request 210`_
* Implement ``shed_update`` to upload contents and update repository
  metadata. `Pull Request 216`_
* Implement ``shed_test`` and ``shed_serve`` commands to test and view
  published artifacts in the Tool Shed. `Pull Request 213`_, `Issue 176`_
* Add shell tab-completion script. 37dcc07_
* Many more commands allow specifing multiple tool and/or repository targets.
  `Issue 150`_
* Add -m as alias for --message in planemo shed_upload (thanks to
  Peter Cock). `Pull Request 200`_
* Add ``--ensure_metadata`` option to ``shed_lint`` to ensure ``.shed.yml``
  files contain many repository. `Pull Request 215`_
* More developer documentation, additional ``make`` targets including ones
  for setting up git pre-commit hooks. cc8abb6_, `Issue 209`_
* Small README improvement (thanks to Martin Čech) b53006d_
* Fixes for shed operation error handling (thanks to Martin Čech).
  `Pull Request 203`_,  `Pull Request 206`_
* Fix for "smart" ``shed_diff`` not in the repository root directory
  (thanks to Peter Cock). `Pull Request 207`_, `Issue 205`_
* Recursive ``shed_diff`` with directories not yet in Tool Shed.
  `Pull Request 208`_
* Improve error handling and reporting for problematic ``--shed_target``
  values. `Issue 217`_
* Fix typos in lint messages. `Issue 211`_


---------------------
0.11.1 (2015-05-12)
---------------------

* Fix default behavior for ``planemo lint`` to use current directory if
  explicit paths are not supplied. 1e3668a_

---------------------
0.11.0 (2015-05-12)
---------------------

* More compact syntax for defining multiple custom inclusions in ``.shed.yml``
  files - thanks to Peter Cock. `Issue 180`_, `Pull Request 185`_,
  `Pull Request 196`_
* Prevent ambigous destinations when defining custom inclusions in
  ``.shed.yml``- thanks to Peter Cock. `Pull Request 186`_
* ``lint`` now warns if tool ids contain whitespace. `Pull Request 190`_
* Handle empty tar-balls gracefully on older Python versions - thanks
  to Peter Cock. `Pull Request 187`_
* Tweak quoting in ``cp`` command - thanks to Peter Cock. 6bcf699_
* Fix regression causing testing to no longer produce "pretty" test
  results under certain circumstances. `Issue 188`_
* Fix for recursive ``shed_diff`` folder naming. `Issue 192`_
* Fix output definitions to ``tool_init`` command. `Issue 189`_

---------------------
0.10.0 (2015-05-06)
---------------------

* Extend ``shed_lint`` to check for valid actions in tool_dependencies.xml
  files. 8117e03_
* Extend ``shed_lint`` to check for required files based on repository type.
  `Issue 156`_
* Ignore common editor backup files during ``shed_upload``. `Issue 179`_
* Fix missing file when installing from source via PyPI_. `Issue 181`_
* Fix ``lint`` to verify ``data`` inputs specify a ``format`` attribute.
  8117e03_
* Docstring fix thanks to `@peterjc`_. fe7ad46_


---------------------
0.9.0 (2015-05-03)
---------------------

* Add new logo to the README thanks to `@petrkadlec`_ from `puradesign.cz
  <http://puradesign.cz/en>`__ and `@carlfeberhard`_ from the Galaxy Project.
  `Issue 108`_
* Implement smarter ``shed_diff`` command - it now produces a meaningful
  exit codes and doesn't report differences if these correspond to attributes
  that will be automatically populated by the Tool Shed. `Issue 167`_
* Use new smarter ``shed_diff`` code to implement a new ``--check_diff``
  option for ``shed_upload`` - to check for meaningful differences before
  updating repositories. `Issue 168`_
* Record git commit hash during ``shed_upload`` if the ``.shed.yml`` is
  located in a git repository. `Issue 170`_
* Allow ``shed_`` operations to operate on git URLs directly. `Issue 169`_
* Fail if missing file inclusion statements encountered during ``.shed.yml``
  repository resolution - bug reported by `@peterjc`_. `Issue 158`_
* Improved exception handling for tool shed operations including new
  ``--fail_fast`` command-line option. * `Issue 114`_, `Pull Request 173`_
* Implement more validation when using the ``shed_init`` command. 1cd0e2d_
* Add ``-r/--recursive`` option to ``shed_download`` and ``shed_diff``
  commands and allow these commands to work with ``.shed.yml`` files defining
  multipe repositories. 40a1f57_
* Add ``--port`` option to the ``serve`` and ``tool_factory`` commands.
  15804be_
* Fix problem introduced with `setup.py`_ during the 0.9.0 development cycle
  - thanks to `@peterjc`_. `Pull Request 171`_
* Fix clone bug introduced during 0.9.0 development cycle - thanks to
  `@bgruening`_. `Pull Request 175`_

---------------------
0.8.4 (2015-04-30)
---------------------

* Fix for Travis CI testing picking up invalid tests (reported by `@takadonet`_). `Issue 161`_
* Fix tar ordering for consistency (always sort by name) - thanks to `@peterjc`_.  `Pull Request 164`_, `Issue 159`_
* Fix exception handling related to tool shed operations - thanks to `@peterjc`_. `Pull Request 155`_, b86fe1f_

---------------------
0.8.3 (2015-04-29)
---------------------

* Fix bug where ``shed_lint`` was not respecting the ``-r/--recursive`` flag.
  9ff0d2d_
* Fix bug where planemo was producing tar files incompatible with the Tool
  Shed for package and suite repositories. a2ee135_

---------------------
0.8.2 (2015-04-29)
---------------------

* Fix bug with ``config_init`` command thanks to `@bgruening`_. `Pull Request 151`_
* Fix unnessecary ``lint`` warning about ``parallelism`` tag reported by
  `@peterjc`_. 9bf1eab_

---------------------
0.8.1 (2015-04-28)
---------------------

* Fixes for the source distribution to allow installation of 0.8.0 via Homebrew.

---------------------
0.8.0 (2015-04-27)
---------------------

* Implement the new ``shed_lint`` command that verifies various aspects of tool
  shed repositories - including XSD_ validation of ``repository_dependencies.xml``
  and ``tool_dependencies.xml`` files, best practices for README files, and the
  contents of ``.shed.yml`` files. This requires the lxml_ library to be available
  to Planemo or the application xmllint_ to be on its ``PATH``. `Pull Request 130`_
  `Issue 89`_ `Issue 91`_ 912df02_ d26929e_ 36ac6d8_
* Option to enable experimental XSD_ based validation of tools when ``lint``
  is executed with the new ``--xsd`` flag. This validation occurs against the
  unofficial `Galaxy Tool XSD project <https://github.com/JeanFred/Galaxy-XSD>`__
  maintained by `@JeanFred`_. This requires the lxml_ library to be
  available to Planemo or the application xmllint_ to be on its ``PATH``.
  `Pull Request 130`_ 912df02_
* Allow skipping specific linters when using the ``lint`` command using the new
  ``--skip`` option. 26e3cdb_
* Implement sophisticated options in ``.shed.yml`` to map a directory to many,
  custom Tool Shed repositories during shed operaitons such ``shed_upload``
  including automatically mapping tools to their own directories and automatically
  building suites repositories. `Pull Request 143`_
* Make ``shed_upload`` more intelligent when building tar files so that package
  and suite repositories may have README files in source control and they will
  just be filtered out during upload. 53edd99_
* Implement a new ``shed_init`` command that will help bootstrap ``.shed.yml``
  files in the specified directory. cc1a447_
* Extend ``shed_init`` to automatically build a ``repository_rependencies.xml``
  file corresponding to a Galaxy workflow (``.ga`` file). `Issue 118`_ 988de1d_
* In addition to a single file or directory, allow ``lint`` to be passed multiple
  files. 343902d_ `Issue 139`_
* Add ``-r/--recursive`` option to ``shed_create`` and ``lint`` commands. 63cd431_
  01f2af9_
* Improved output formatting and option to write diffs to a file for the
  ``shed_diff`` command. 965511d_
* Fix lint problem when using new Galaxy testing features such as expecting
  job failures and verifing job output. `Issue 138`_
* Fix typo in ``test`` help thanks to first time contributor `@pvanheus`_.
  `Pull Request 129`_ 1982076_
* Fix NPE on empty ``help`` element when linting tools. `Issue 124`_
* Fix ``lint`` warnings when ``configfiles`` are defined in a tool. 1a85493_
* Fix for empty ``.shed.yml`` files. b7d9e96_
* Fix the ``test`` command for newer versions of nose_. 33294d2_
* Update help content and documentation to be clear ``normalize`` should not
  be used to update the contents of tool files at this time. 08de8de_
* Warn on unknown ``command`` attributes when linting tools (anything but
  ``interpreter``). 4f61025_
* Various design, documentation (including new documentation on Tool Shed
  `publishing <http://planemo.readthedocs.org/en/latest/publishing.html>`__),
  and testing related improvements (test coverage has risen from 65% to over
  80% during this release cycle).

---------------------
0.7.0 (2015-04-13)
---------------------

* Implement `shed_create` command to create Tool Shed repositories from
  ``.shed.yml`` files (thanks to E. Rasche). `Pull Request 101`_
* Allow automatic creation of missing repositories  during ``shed_upload``
  with the new ``--force_repository_creation`` flag (thanks to E. Rasche).
  `Pull Request 102`_
* Allow specifying files to exclude in ``.shed.yml`` when creating tar files
  for ``shed_upload`` (thanks to Björn Grüning). `Pull Request 99`_
* Resolve symbolic links when building Tool Shed tar files with
  ``shed_upload`` (thanks to Dave Bouvier). `Pull Request 104`_
* Add a `Contributor Code of Conduct
  <https://planemo.readthedocs.org/en/latest/conduct.html>`__.
  `Pull Request 113`_
* Omit ``tool_test_output.json`` from Tool Shed tar file created with
  ``shed_upload`` (thanks to Dave Bouvier). `Pull Request 111`_
* Update required version of bioblend_ to ``0.5.3``. Fixed `Issue 88`_.
* Initial work on implementing tests cases for Tool Shed functionality.
  182fe57_
* Fix incorrect link in HTML test report (thanks to Martin Čech). 4c71299_
* Download Galaxy from the new, official Github repository. 7c69bf6_
* Update travis_test to install stable planemo from PyPI_. 39fedd2_
* Enable caching on ``--install_galaxy`` by default (disable with
  ``--no_cache_galaxy``). d755fe7_

---------------------
0.6.0 (2015-03-16)
---------------------

* Many enhancements to the tool building documentation - descriptions of macros, collections, simple and conditional parameters, etc...
* Fix ``tool_init`` to quote file names (thanks to Peter Cock).  `Pull Request 98`_.
* Allow ignoring file patterns in ``.shed.yml`` (thanks to Björn Grüning). `Pull Request 99`_
* Add ``--macros`` flag to ``tool_init`` command to generate a macro file as part of tool generation. ec6e30f_
* Add linting of tag order for tool XML files. 4823c5e_
* Add linting of ``stdio`` tags in tool XML files. 8207026_
* More tests, much higher test coverage. 0bd4ff0_

---------------------
0.5.0 (2015-02-22)
---------------------

* Implement ``--version`` option. `Issue 78`_
* Implement ``--no_cleanup`` option for ``test`` and ``serve`` commands to
  persist temp files. 2e41e0a_
* Fix bug that left temp files undeleted. `Issue 80`_
* More improvements to release process. fba3874_

---------------------
0.4.2 (2015-02-21)
---------------------

* Fix `setup.py`_ for installing non-Python data from PyPI_ (required newer
  for ``tool_factory`` command and reStructuredText linting). Thanks to
  Damion Dooley for the bug report. `Issue 83`_

---------------------
0.4.1 (2015-02-16)
---------------------

* Fix README.rst so it renders properly on PyPI_.

---------------------
0.4.0 (2015-02-16)
---------------------

* Implement ``tool_init`` command for bootstrapping creation of new
  tools (with `tutorial <http://planemo.readthedocs.org/en/latest/writing.html>`_.) 78f8274_
* Implement ``normalize`` command for reorganizing tool XML and macro
  debugging. e8c1d45_
* Implement ``tool_factory`` command to spin up Galaxy pre-configured the
  `Tool Factory`_. 9e746b4_
* Added basic linting of ``command`` blocks. b8d90ab_
* Improved linting of ``help`` blocks, including verifying valid
  `reStructuredText`. 411a8da_
* Fix bug related to ``serve`` command not killing Galaxy properly when complete. 53a6766_
* Have ``serve`` command display tools at the top level instead of in shallow sections. badc25f_
* Add additional dependencies to ``setup.py`` more functionality works out
  of the box. 85b9614_
* Fix terrible error message related to bioblend_ being unavailable.
  `Issue 70`_
* Various smaller documentation and project structure improvements.

---------------------
0.3.1 (2015-02-15)
---------------------

* Fixes to get PyPI_ workflow working properly.

---------------------
0.3.0 (2015-02-13)
---------------------

* Add option (``-r``) to the ``shed_upload`` command to recursively upload
  subdirectories (thanks to E. Rasche). `Pull Request 68`_
* Fix diff formatting in test reports (thanks to E. Rasche).
  `Pull Request 63`_
* Grab updated test database to speed up testing (thanks to approach from
  E. Rasche and Dannon Baker). `Issue 61`_, dff4f33_
* Fix test data command-line argument name (was ``test-data`` now it is
  ``test_data``). 834bfb2_
* Use ``tool_data_table_conf.xml.sample`` file if
  ``tool_data_table_conf.xml.test`` is unavailable. Should allow some
  new tools to be tested without modifying Galaxy's global
  ``tool_data_table_conf.xml`` file. ac4f828_

---------------------
0.2.0 (2015-01-13)
---------------------

* Improvements to way Planemo loads its own copy of Galaxy modules to prevent
  various conflicts when launching Galaxy from Planemo. `Pull Request 56`_
* Allow setting various test output options in ``~/.planemo.yml`` and disabling
  JSON output. 21bb463_
* More experimental Brew and Tool Shed options that should not be considered
  part of Planemo's stable API. See bit.ly/gxbrew1 for more details.
* Fix ``project_init`` for BSD tar (thanks to Nitesh Turaga for the bug
  report.) a4110a8_
* Documentation fixes for tool linting command (thanks to Nicola Soranzo).
  `Pull Request 51`_

---------------------
0.1.0 (2014-12-16)
---------------------

* Moved repository URL to https://github.com/galaxyproject/planemo.
* Support for publishing to the Tool Shed. `Pull Request 6`_
* Support for producing diffs (``shed_diff``) between local repositories and
  the Tool Shed (based on scripts by Peter Cock). `Pull Request 33`_
* Use tool's local test data when available - add option for configuring
  ``test-data`` target. `Pull Request 1`_
* Support for testing tool features dependent on cached data. 44de95c_
* Support for generating XUnit tool test reports. 82e8b1f_
* Prettier HTML reports for tool tests. 05cc9f4_
* Implement ``share_test`` command for embedding test result links in pull
  requests. `Pull Request 40`_
* Fix for properly resolving links during Tool Shed publishing (thanks to Dave
  Bouvier). `Pull Request 29`_
* Fix for citation linter (thanks to Michael Crusoe for the bug report). af39061_
* Fix tool scanning for tool files with fewer than 10 lines (thanks to Dan
  Blankenberg). a2c13e4_
* Automate more of Travis CI testing so the scripts added to tool repository
  can be smaller. 20a8680_
* Documentation fixes for Travis CI (thanks to Peter Cock). `Pull Request 22`_,
  `Pull Request 23`_
* Various documentation fixes (thanks to Martin Čech). 36f7cb1_, b9232e5_
* Various smaller fixes for Docker support, tool linting, and documentation.

---------------------
0.0.1 (2014-10-04)
---------------------

* Initial work on the project - commands for testing, linting, serving Galaxy
  tools - and more experimental features involving Docker and Homebrew. 7d07782_

.. github_links
.. _Pull Request 1554: https://github.com/galaxyproject/planemo/pull/1554
.. _Pull Request 1552: https://github.com/galaxyproject/planemo/pull/1552
.. _Pull Request 1553: https://github.com/galaxyproject/planemo/pull/1553
.. _Pull Request 1551: https://github.com/galaxyproject/planemo/pull/1551
.. _Pull Request 1548: https://github.com/galaxyproject/planemo/pull/1548
.. _Pull Request 1549: https://github.com/galaxyproject/planemo/pull/1549
.. _Pull Request 1547: https://github.com/galaxyproject/planemo/pull/1547
.. _Pull Request 1546: https://github.com/galaxyproject/planemo/pull/1546
.. _Pull Request 1543: https://github.com/galaxyproject/planemo/pull/1543
.. _Pull Request 1545: https://github.com/galaxyproject/planemo/pull/1545
.. _Pull Request 1532: https://github.com/galaxyproject/planemo/pull/1532
.. _Pull Request 1539: https://github.com/galaxyproject/planemo/pull/1539
.. _Pull Request 1534: https://github.com/galaxyproject/planemo/pull/1534
.. _Pull Request 1542: https://github.com/galaxyproject/planemo/pull/1542
.. _Pull Request 1540: https://github.com/galaxyproject/planemo/pull/1540
.. _Pull Request 1541: https://github.com/galaxyproject/planemo/pull/1541
.. _Pull Request 1531: https://github.com/galaxyproject/planemo/pull/1531
.. _Pull Request 1510: https://github.com/galaxyproject/planemo/pull/1510
.. _Pull Request 1538: https://github.com/galaxyproject/planemo/pull/1538
.. _Pull Request 1506: https://github.com/galaxyproject/planemo/pull/1506
.. _Pull Request 1526: https://github.com/galaxyproject/planemo/pull/1526
.. _Pull Request 1509: https://github.com/galaxyproject/planemo/pull/1509
.. _Pull Request 1514: https://github.com/galaxyproject/planemo/pull/1514
.. _Pull Request 1523: https://github.com/galaxyproject/planemo/pull/1523
.. _Pull Request 1519: https://github.com/galaxyproject/planemo/pull/1519
.. _Pull Request 1518: https://github.com/galaxyproject/planemo/pull/1518
.. _Pull Request 1524: https://github.com/galaxyproject/planemo/pull/1524
.. _Pull Request 1507: https://github.com/galaxyproject/planemo/pull/1507
.. _Pull Request 1505: https://github.com/galaxyproject/planemo/pull/1505
.. _Pull Request 1504: https://github.com/galaxyproject/planemo/pull/1504
.. _Pull Request 1503: https://github.com/galaxyproject/planemo/pull/1503
.. _Pull Request 1502: https://github.com/galaxyproject/planemo/pull/1502
.. _Pull Request 1501: https://github.com/galaxyproject/planemo/pull/1501
.. _Pull Request 1500: https://github.com/galaxyproject/planemo/pull/1500
.. _Pull Request 1496: https://github.com/galaxyproject/planemo/pull/1496
.. _Pull Request 1492: https://github.com/galaxyproject/planemo/pull/1492
.. _Pull Request 1494: https://github.com/galaxyproject/planemo/pull/1494
.. _Pull Request 1495: https://github.com/galaxyproject/planemo/pull/1495
.. _Pull Request 1487: https://github.com/galaxyproject/planemo/pull/1487
.. _Pull Request 1483: https://github.com/galaxyproject/planemo/pull/1483
.. _Pull Request 1491: https://github.com/galaxyproject/planemo/pull/1491
.. _Pull Request 1488: https://github.com/galaxyproject/planemo/pull/1488
.. _Pull Request 1481: https://github.com/galaxyproject/planemo/pull/1481
.. _Pull Request 1474: https://github.com/galaxyproject/planemo/pull/1474
.. _Pull Request 1452: https://github.com/galaxyproject/planemo/pull/1452
.. _Pull Request 1473: https://github.com/galaxyproject/planemo/pull/1473
.. _Pull Request 1457: https://github.com/galaxyproject/planemo/pull/1457
.. _Pull Request 1471: https://github.com/galaxyproject/planemo/pull/1471
.. _Pull Request 1458: https://github.com/galaxyproject/planemo/pull/1458
.. _Pull Request 1460: https://github.com/galaxyproject/planemo/pull/1460
.. _Pull Request 1462: https://github.com/galaxyproject/planemo/pull/1462
.. _Pull Request 1463: https://github.com/galaxyproject/planemo/pull/1463
.. _Pull Request 1466: https://github.com/galaxyproject/planemo/pull/1466
.. _Pull Request 1461: https://github.com/galaxyproject/planemo/pull/1461
.. _Pull Request 1453: https://github.com/galaxyproject/planemo/pull/1453
.. _Pull Request 1420: https://github.com/galaxyproject/planemo/pull/1420
.. _Pull Request 1445: https://github.com/galaxyproject/planemo/pull/1445
.. _Pull Request 1450: https://github.com/galaxyproject/planemo/pull/1450
.. _Pull Request 1441: https://github.com/galaxyproject/planemo/pull/1441
.. _Pull Request 1447: https://github.com/galaxyproject/planemo/pull/1447
.. _Pull Request 1444: https://github.com/galaxyproject/planemo/pull/1444
.. _Pull Request 1443: https://github.com/galaxyproject/planemo/pull/1443
.. _Pull Request 1442: https://github.com/galaxyproject/planemo/pull/1442
.. _Pull Request 1439: https://github.com/galaxyproject/planemo/pull/1439
.. _Pull Request 1440: https://github.com/galaxyproject/planemo/pull/1440
.. _Pull Request 1437: https://github.com/galaxyproject/planemo/pull/1437
.. _Pull Request 1433: https://github.com/galaxyproject/planemo/pull/1433
.. _Pull Request 1430: https://github.com/galaxyproject/planemo/pull/1430
.. _Pull Request 1428: https://github.com/galaxyproject/planemo/pull/1428
.. _Pull Request 1427: https://github.com/galaxyproject/planemo/pull/1427
.. _Pull Request 1425: https://github.com/galaxyproject/planemo/pull/1425
.. _Pull Request 1424: https://github.com/galaxyproject/planemo/pull/1424
.. _Pull Request 1422: https://github.com/galaxyproject/planemo/pull/1422
.. _Pull Request 1419: https://github.com/galaxyproject/planemo/pull/1419
.. _Pull Request 1416: https://github.com/galaxyproject/planemo/pull/1416
.. _Pull Request 1388: https://github.com/galaxyproject/planemo/pull/1388
.. _Pull Request 1412: https://github.com/galaxyproject/planemo/pull/1412
.. _Pull Request 1410: https://github.com/galaxyproject/planemo/pull/1410
.. _Pull Request 1408: https://github.com/galaxyproject/planemo/pull/1408
.. _Pull Request 1407: https://github.com/galaxyproject/planemo/pull/1407
.. _Pull Request 1406: https://github.com/galaxyproject/planemo/pull/1406
.. _Pull Request 1401: https://github.com/galaxyproject/planemo/pull/1401
.. _Pull Request 1402: https://github.com/galaxyproject/planemo/pull/1402
.. _Pull Request 1398: https://github.com/galaxyproject/planemo/pull/1398
.. _Pull Request 1400: https://github.com/galaxyproject/planemo/pull/1400
.. _Pull Request 1399: https://github.com/galaxyproject/planemo/pull/1399
.. _Pull Request 1396: https://github.com/galaxyproject/planemo/pull/1396
.. _Pull Request 1397: https://github.com/galaxyproject/planemo/pull/1397
.. _Pull Request 1395: https://github.com/galaxyproject/planemo/pull/1395
.. _Pull Request 1394: https://github.com/galaxyproject/planemo/pull/1394
.. _Pull Request 1393: https://github.com/galaxyproject/planemo/pull/1393
.. _Pull Request 1391: https://github.com/galaxyproject/planemo/pull/1391
.. _Pull Request 1389: https://github.com/galaxyproject/planemo/pull/1389
.. _Pull Request 1263: https://github.com/galaxyproject/planemo/pull/1263
.. _Pull Request 1387: https://github.com/galaxyproject/planemo/pull/1387
.. _Pull Request 1385: https://github.com/galaxyproject/planemo/pull/1385
.. _Pull Request 1384: https://github.com/galaxyproject/planemo/pull/1384
.. _Pull Request 1383: https://github.com/galaxyproject/planemo/pull/1383
.. _Pull Request 1382: https://github.com/galaxyproject/planemo/pull/1382
.. _Pull Request 1355: https://github.com/galaxyproject/planemo/pull/1355
.. _Pull Request 1378: https://github.com/galaxyproject/planemo/pull/1378
.. _Pull Request 1379: https://github.com/galaxyproject/planemo/pull/1379
.. _Pull Request 1377: https://github.com/galaxyproject/planemo/pull/1377
.. _Pull Request 1375: https://github.com/galaxyproject/planemo/pull/1375
.. _Pull Request 1374: https://github.com/galaxyproject/planemo/pull/1374
.. _Pull Request 1373: https://github.com/galaxyproject/planemo/pull/1373
.. _Pull Request 1372: https://github.com/galaxyproject/planemo/pull/1372
.. _Pull Request 1371: https://github.com/galaxyproject/planemo/pull/1371
.. _Pull Request 1369: https://github.com/galaxyproject/planemo/pull/1369
.. _Pull Request 1370: https://github.com/galaxyproject/planemo/pull/1370
.. _Pull Request 1364: https://github.com/galaxyproject/planemo/pull/1364
.. _Pull Request 1358: https://github.com/galaxyproject/planemo/pull/1358
.. _Pull Request 1357: https://github.com/galaxyproject/planemo/pull/1357
.. _Pull Request 1265: https://github.com/galaxyproject/planemo/pull/1265
.. _Pull Request 1350: https://github.com/galaxyproject/planemo/pull/1350
.. _Pull Request 1275: https://github.com/galaxyproject/planemo/pull/1275
.. _Pull Request 1347: https://github.com/galaxyproject/planemo/pull/1347
.. _Pull Request 1348: https://github.com/galaxyproject/planemo/pull/1348
.. _Pull Request 1346: https://github.com/galaxyproject/planemo/pull/1346
.. _Pull Request 1344: https://github.com/galaxyproject/planemo/pull/1344
.. _Pull Request 1338: https://github.com/galaxyproject/planemo/pull/1338
.. _Pull Request 1337: https://github.com/galaxyproject/planemo/pull/1337
.. _Pull Request 1334: https://github.com/galaxyproject/planemo/pull/1334
.. _Pull Request 1327: https://github.com/galaxyproject/planemo/pull/1327
.. _Pull Request 1332: https://github.com/galaxyproject/planemo/pull/1332
.. _Pull Request 1330: https://github.com/galaxyproject/planemo/pull/1330
.. _Pull Request 1329: https://github.com/galaxyproject/planemo/pull/1329
.. _Pull Request 1326: https://github.com/galaxyproject/planemo/pull/1326
.. _Pull Request 1322: https://github.com/galaxyproject/planemo/pull/1322
.. _Pull Request 1325: https://github.com/galaxyproject/planemo/pull/1325
.. _Pull Request 1320: https://github.com/galaxyproject/planemo/pull/1320
.. _Pull Request 1314: https://github.com/galaxyproject/planemo/pull/1314
.. _Pull Request 1313: https://github.com/galaxyproject/planemo/pull/1313
.. _Pull Request 1312: https://github.com/galaxyproject/planemo/pull/1312
.. _Pull Request 1310: https://github.com/galaxyproject/planemo/pull/1310
.. _Pull Request 1308: https://github.com/galaxyproject/planemo/pull/1308
.. _Pull Request 1302: https://github.com/galaxyproject/planemo/pull/1302
.. _Pull Request 1303: https://github.com/galaxyproject/planemo/pull/1303
.. _Pull Request 1304: https://github.com/galaxyproject/planemo/pull/1304
.. _Pull Request 1305: https://github.com/galaxyproject/planemo/pull/1305
.. _Pull Request 1306: https://github.com/galaxyproject/planemo/pull/1306
.. _Pull Request 1307: https://github.com/galaxyproject/planemo/pull/1307
.. _Pull Request 1247: https://github.com/galaxyproject/planemo/pull/1247
.. _Pull Request 1249: https://github.com/galaxyproject/planemo/pull/1249
.. _Pull Request 1255: https://github.com/galaxyproject/planemo/pull/1255
.. _Pull Request 1257: https://github.com/galaxyproject/planemo/pull/1257
.. _Pull Request 1259: https://github.com/galaxyproject/planemo/pull/1259
.. _Pull Request 1260: https://github.com/galaxyproject/planemo/pull/1260
.. _Pull Request 1262: https://github.com/galaxyproject/planemo/pull/1262
.. _Pull Request 1212: https://github.com/galaxyproject/planemo/pull/1212
.. _Pull Request 1264: https://github.com/galaxyproject/planemo/pull/1264
.. _Pull Request 1232: https://github.com/galaxyproject/planemo/pull/1232
.. _Pull Request 1270: https://github.com/galaxyproject/planemo/pull/1270
.. _Pull Request 1274: https://github.com/galaxyproject/planemo/pull/1274
.. _Pull Request 1278: https://github.com/galaxyproject/planemo/pull/1278
.. _Pull Request 1277: https://github.com/galaxyproject/planemo/pull/1277
.. _Pull Request 1279: https://github.com/galaxyproject/planemo/pull/1279
.. _Pull Request 1281: https://github.com/galaxyproject/planemo/pull/1281
.. _Pull Request 1283: https://github.com/galaxyproject/planemo/pull/1283
.. _Pull Request 1280: https://github.com/galaxyproject/planemo/pull/1280
.. _Pull Request 1284: https://github.com/galaxyproject/planemo/pull/1284
.. _Pull Request 1287: https://github.com/galaxyproject/planemo/pull/1287
.. _Pull Request 1288: https://github.com/galaxyproject/planemo/pull/1288
.. _Pull Request 1285: https://github.com/galaxyproject/planemo/pull/1285
.. _Pull Request 1271: https://github.com/galaxyproject/planemo/pull/1271
.. _Pull Request 1291: https://github.com/galaxyproject/planemo/pull/1291
.. _Pull Request 1227: https://github.com/galaxyproject/planemo/pull/1227
.. _Pull Request 1292: https://github.com/galaxyproject/planemo/pull/1292
.. _Pull Request 1293: https://github.com/galaxyproject/planemo/pull/1293
.. _Pull Request 1276: https://github.com/galaxyproject/planemo/pull/1276
.. _Pull Request 1295: https://github.com/galaxyproject/planemo/pull/1295
.. _Pull Request 1294: https://github.com/galaxyproject/planemo/pull/1294
.. _Pull Request 1296: https://github.com/galaxyproject/planemo/pull/1296
.. _Pull Request 1298: https://github.com/galaxyproject/planemo/pull/1298
.. _Pull Request 1299: https://github.com/galaxyproject/planemo/pull/1299
.. _Pull Request 1297: https://github.com/galaxyproject/planemo/pull/1297
.. _Pull Request 1244: https://github.com/galaxyproject/planemo/pull/1244
.. _Pull Request 1242: https://github.com/galaxyproject/planemo/pull/1242
.. _Pull Request 1241: https://github.com/galaxyproject/planemo/pull/1241
.. _Pull Request 1239: https://github.com/galaxyproject/planemo/pull/1239
.. _Pull Request 1237: https://github.com/galaxyproject/planemo/pull/1237
.. _Pull Request 1230: https://github.com/galaxyproject/planemo/pull/1230
.. _Pull Request 1228: https://github.com/galaxyproject/planemo/pull/1228
.. _Pull Request 1224: https://github.com/galaxyproject/planemo/pull/1224
.. _Pull Request 1226: https://github.com/galaxyproject/planemo/pull/1226
.. _Pull Request 1222: https://github.com/galaxyproject/planemo/pull/1222
.. _Pull Request 1217: https://github.com/galaxyproject/planemo/pull/1217
.. _Pull Request 1213: https://github.com/galaxyproject/planemo/pull/1213
.. _Pull Request 1214: https://github.com/galaxyproject/planemo/pull/1214
.. _Pull Request 1215: https://github.com/galaxyproject/planemo/pull/1215
.. _Pull Request 1209: https://github.com/galaxyproject/planemo/pull/1209
.. _Pull Request 1206: https://github.com/galaxyproject/planemo/pull/1206
.. _Pull Request 1207: https://github.com/galaxyproject/planemo/pull/1207
.. _Pull Request 1205: https://github.com/galaxyproject/planemo/pull/1205
.. _Pull Request 1198: https://github.com/galaxyproject/planemo/pull/1198
.. _Pull Request 1140: https://github.com/galaxyproject/planemo/pull/1140
.. _Pull Request 1200: https://github.com/galaxyproject/planemo/pull/1200
.. _Pull Request 1201: https://github.com/galaxyproject/planemo/pull/1201
.. _Pull Request 1188: https://github.com/galaxyproject/planemo/pull/1188
.. _Pull Request 1193: https://github.com/galaxyproject/planemo/pull/1193
.. _Pull Request 1195: https://github.com/galaxyproject/planemo/pull/1195
.. _Pull Request 1196: https://github.com/galaxyproject/planemo/pull/1196
.. _Pull Request 1184: https://github.com/galaxyproject/planemo/pull/1184
.. _Pull Request 1187: https://github.com/galaxyproject/planemo/pull/1187
.. _Pull Request 1151: https://github.com/galaxyproject/planemo/pull/1151
.. _Pull Request 1153: https://github.com/galaxyproject/planemo/pull/1153
.. _Pull Request 1179: https://github.com/galaxyproject/planemo/pull/1179
.. _Pull Request 1180: https://github.com/galaxyproject/planemo/pull/1180
.. _Pull Request 1182: https://github.com/galaxyproject/planemo/pull/1182
.. _Pull Request 1170: https://github.com/galaxyproject/planemo/pull/1170
.. _Pull Request 1171: https://github.com/galaxyproject/planemo/pull/1171
.. _Pull Request 1172: https://github.com/galaxyproject/planemo/pull/1172
.. _Pull Request 1173: https://github.com/galaxyproject/planemo/pull/1173
.. _Pull Request 1174: https://github.com/galaxyproject/planemo/pull/1174
.. _Pull Request 1177: https://github.com/galaxyproject/planemo/pull/1177
.. _Pull Request 1169: https://github.com/galaxyproject/planemo/pull/1169
.. _Pull Request 1165: https://github.com/galaxyproject/planemo/pull/1165
.. _Pull Request 1164: https://github.com/galaxyproject/planemo/pull/1164
.. _Pull Request 1157: https://github.com/galaxyproject/planemo/pull/1157
.. _Pull Request 1156: https://github.com/galaxyproject/planemo/pull/1156
.. _Pull Request 1154: https://github.com/galaxyproject/planemo/pull/1154
.. _Pull Request 1152: https://github.com/galaxyproject/planemo/pull/1152
.. _Pull Request 1146: https://github.com/galaxyproject/planemo/pull/1146
.. _Pull Request 1145: https://github.com/galaxyproject/planemo/pull/1145
.. _Pull Request 1144: https://github.com/galaxyproject/planemo/pull/1144
.. _Pull Request 1142: https://github.com/galaxyproject/planemo/pull/1142
.. _Pull Request 1095: https://github.com/galaxyproject/planemo/pull/1095
.. _Pull Request 1135: https://github.com/galaxyproject/planemo/pull/1135
.. _Pull Request 1134: https://github.com/galaxyproject/planemo/pull/1134
.. _Pull Request 1133: https://github.com/galaxyproject/planemo/pull/1133
.. _Pull Request 1128: https://github.com/galaxyproject/planemo/pull/1128
.. _Pull Request 1127: https://github.com/galaxyproject/planemo/pull/1127
.. _Pull Request 1126: https://github.com/galaxyproject/planemo/pull/1126
.. _Pull Request 1125: https://github.com/galaxyproject/planemo/pull/1125
.. _Pull Request 1124: https://github.com/galaxyproject/planemo/pull/1124
.. _Pull Request 1123: https://github.com/galaxyproject/planemo/pull/1123
.. _Pull Request 1064: https://github.com/galaxyproject/planemo/pull/1064
.. _Pull Request 1066: https://github.com/galaxyproject/planemo/pull/1066
.. _Pull Request 1068: https://github.com/galaxyproject/planemo/pull/1068
.. _Pull Request 1072: https://github.com/galaxyproject/planemo/pull/1072
.. _Pull Request 1074: https://github.com/galaxyproject/planemo/pull/1074
.. _Pull Request 1076: https://github.com/galaxyproject/planemo/pull/1076
.. _Pull Request 1079: https://github.com/galaxyproject/planemo/pull/1079
.. _Pull Request 1083: https://github.com/galaxyproject/planemo/pull/1083
.. _Pull Request 1086: https://github.com/galaxyproject/planemo/pull/1086
.. _Pull Request 1091: https://github.com/galaxyproject/planemo/pull/1091
.. _Pull Request 1093: https://github.com/galaxyproject/planemo/pull/1093
.. _Pull Request 1094: https://github.com/galaxyproject/planemo/pull/1094
.. _Pull Request 1096: https://github.com/galaxyproject/planemo/pull/1096
.. _Pull Request 1099: https://github.com/galaxyproject/planemo/pull/1099
.. _Pull Request 1101: https://github.com/galaxyproject/planemo/pull/1101
.. _Pull Request 1102: https://github.com/galaxyproject/planemo/pull/1102
.. _Pull Request 1108: https://github.com/galaxyproject/planemo/pull/1108
.. _Pull Request 1110: https://github.com/galaxyproject/planemo/pull/1110
.. _Pull Request 1114: https://github.com/galaxyproject/planemo/pull/1114
.. _Pull Request 1115: https://github.com/galaxyproject/planemo/pull/1115
.. _Pull Request 1116: https://github.com/galaxyproject/planemo/pull/1116
.. _Pull Request 1118: https://github.com/galaxyproject/planemo/pull/1118
.. _Pull Request 1120: https://github.com/galaxyproject/planemo/pull/1120
.. _Pull Request 1121: https://github.com/galaxyproject/planemo/pull/1121
.. _Pull Request 821: https://github.com/galaxyproject/planemo/pull/821
.. _Pull Request 1052: https://github.com/galaxyproject/planemo/pull/1052
.. _Pull Request 1061: https://github.com/galaxyproject/planemo/pull/1061
.. _Pull Request 1062: https://github.com/galaxyproject/planemo/pull/1062
.. _Pull Request 1060: https://github.com/galaxyproject/planemo/pull/1060
.. _Pull Request 1059: https://github.com/galaxyproject/planemo/pull/1059
.. _Pull Request 1058: https://github.com/galaxyproject/planemo/pull/1058
.. _Pull Request 1051: https://github.com/galaxyproject/planemo/pull/1051
.. _Pull Request 1049: https://github.com/galaxyproject/planemo/pull/1049
.. _Pull Request 1046: https://github.com/galaxyproject/planemo/pull/1046
.. _Pull Request 1044: https://github.com/galaxyproject/planemo/pull/1044
.. _Pull Request 1043: https://github.com/galaxyproject/planemo/pull/1043
.. _Pull Request 1042: https://github.com/galaxyproject/planemo/pull/1042
.. _Pull Request 1041: https://github.com/galaxyproject/planemo/pull/1041
.. _Pull Request 1040: https://github.com/galaxyproject/planemo/pull/1040
.. _Pull Request 1038: https://github.com/galaxyproject/planemo/pull/1038
.. _Pull Request 1037: https://github.com/galaxyproject/planemo/pull/1037
.. _Pull Request 1036: https://github.com/galaxyproject/planemo/pull/1036
.. _Pull Request 1034: https://github.com/galaxyproject/planemo/pull/1034
.. _Pull Request 1032: https://github.com/galaxyproject/planemo/pull/1032
.. _Pull Request 1029: https://github.com/galaxyproject/planemo/pull/1029
.. _Pull Request 1028: https://github.com/galaxyproject/planemo/pull/1028
.. _Pull Request 1031: https://github.com/galaxyproject/planemo/pull/1031
.. _Pull Request 1026: https://github.com/galaxyproject/planemo/pull/1026
.. _Pull Request 994: https://github.com/galaxyproject/planemo/pull/994
.. _Pull Request 993: https://github.com/galaxyproject/planemo/pull/993
.. _Pull Request 1001: https://github.com/galaxyproject/planemo/pull/1001
.. _Pull Request 1003: https://github.com/galaxyproject/planemo/pull/1003
.. _Pull Request 900: https://github.com/galaxyproject/planemo/pull/900
.. _Pull Request 1008: https://github.com/galaxyproject/planemo/pull/1008
.. _Pull Request 1006: https://github.com/galaxyproject/planemo/pull/1006
.. _Pull Request 1011: https://github.com/galaxyproject/planemo/pull/1011
.. _Pull Request 1017: https://github.com/galaxyproject/planemo/pull/1017
.. _Pull Request 1015: https://github.com/galaxyproject/planemo/pull/1015
.. _Pull Request 1013: https://github.com/galaxyproject/planemo/pull/1013
.. _Pull Request 1020: https://github.com/galaxyproject/planemo/pull/1020
.. _Pull Request 1021: https://github.com/galaxyproject/planemo/pull/1021
.. _Pull Request 1022: https://github.com/galaxyproject/planemo/pull/1022
.. _Pull Request 1023: https://github.com/galaxyproject/planemo/pull/1023
.. _Pull Request 1025: https://github.com/galaxyproject/planemo/pull/1025
.. _Pull Request 1024: https://github.com/galaxyproject/planemo/pull/1024
.. _Pull Request 991: https://github.com/galaxyproject/planemo/pull/991
.. _Pull Request 988: https://github.com/galaxyproject/planemo/pull/988
.. _Pull Request 989: https://github.com/galaxyproject/planemo/pull/989
.. _Pull Request 985: https://github.com/galaxyproject/planemo/pull/985
.. _Pull Request 984: https://github.com/galaxyproject/planemo/pull/984
.. _Pull Request 986: https://github.com/galaxyproject/planemo/pull/986
.. _Pull Request 983: https://github.com/galaxyproject/planemo/pull/983
.. _Pull Request 982: https://github.com/galaxyproject/planemo/pull/982
.. _Pull Request 980: https://github.com/galaxyproject/planemo/pull/980
.. _Pull Request 978: https://github.com/galaxyproject/planemo/pull/978
.. _Pull Request 979: https://github.com/galaxyproject/planemo/pull/979
.. _Pull Request 977: https://github.com/galaxyproject/planemo/pull/977
.. _Pull Request 975: https://github.com/galaxyproject/planemo/pull/975
.. _Pull Request 974: https://github.com/galaxyproject/planemo/pull/974
.. _Pull Request 976: https://github.com/galaxyproject/planemo/pull/976
.. _Pull Request 972: https://github.com/galaxyproject/planemo/pull/972
.. _Pull Request 973: https://github.com/galaxyproject/planemo/pull/973
.. _Pull Request 971: https://github.com/galaxyproject/planemo/pull/971
.. _Pull Request 970: https://github.com/galaxyproject/planemo/pull/970
.. _Pull Request 968: https://github.com/galaxyproject/planemo/pull/968
.. _1ab8530: https://github.com/galaxyproject/planemo/commit/1ab8530
.. _Pull Request 966: https://github.com/galaxyproject/planemo/pull/966
.. _Pull Request 964: https://github.com/galaxyproject/planemo/pull/964
.. _Pull Request 963: https://github.com/galaxyproject/planemo/pull/963
.. _Pull Request 959: https://github.com/galaxyproject/planemo/pull/959
.. _Pull Request 958: https://github.com/galaxyproject/planemo/pull/958
.. _Pull Request 950: https://github.com/galaxyproject/planemo/pull/950
.. _Pull Request 944: https://github.com/galaxyproject/planemo/pull/944
.. _Pull Request 926: https://github.com/galaxyproject/planemo/pull/926
.. _Pull Request 937: https://github.com/galaxyproject/planemo/pull/937
.. _Pull Request 938: https://github.com/galaxyproject/planemo/pull/938
.. _Pull Request 943: https://github.com/galaxyproject/planemo/pull/943
.. _Pull Request 940: https://github.com/galaxyproject/planemo/pull/940
.. _Pull Request 937: https://github.com/galaxyproject/planemo/pull/937
.. _Pull Request 935: https://github.com/galaxyproject/planemo/pull/935
.. _Pull Request 931: https://github.com/galaxyproject/planemo/pull/931
.. _Pull Request 930: https://github.com/galaxyproject/planemo/pull/930
.. _Pull Request 913: https://github.com/galaxyproject/planemo/pull/913
.. _Pull Request 917: https://github.com/galaxyproject/planemo/pull/917
.. _Pull Request 921: https://github.com/galaxyproject/planemo/pull/921
.. _Pull Request 918: https://github.com/galaxyproject/planemo/pull/918
.. _Pull Request 924: https://github.com/galaxyproject/planemo/pull/924
.. _Pull Request 925: https://github.com/galaxyproject/planemo/pull/925
.. _Pull Request 912: https://github.com/galaxyproject/planemo/pull/912
.. _Pull Request 915: https://github.com/galaxyproject/planemo/pull/915
.. _Pull Request 914: https://github.com/galaxyproject/planemo/pull/914
.. _07dc6e0: https://github.com/galaxyproject/planemo/commit/07dc6e0
.. _Pull Request 910: https://github.com/galaxyproject/planemo/pull/910
.. _Pull Request 909: https://github.com/galaxyproject/planemo/pull/909
.. _Pull Request 908: https://github.com/galaxyproject/planemo/pull/908
.. _Pull Request 907: https://github.com/galaxyproject/planemo/pull/907
.. _Pull Request 906: https://github.com/galaxyproject/planemo/pull/906
.. _Pull Request 902: https://github.com/galaxyproject/planemo/pull/902
.. _Pull Request 895: https://github.com/galaxyproject/planemo/pull/895
.. _Issue 845: https://github.com/galaxyproject/planemo/issues/845
.. _Issue 898: https://github.com/galaxyproject/planemo/issues/898
.. _Pull Request 899: https://github.com/galaxyproject/planemo/pull/899
.. _Pull Request 896: https://github.com/galaxyproject/planemo/pull/896
.. _Pull Request 894: https://github.com/galaxyproject/planemo/pull/894
.. _Pull Request 876: https://github.com/galaxyproject/planemo/pull/876
.. _Pull Request 893: https://github.com/galaxyproject/planemo/pull/893
.. _Pull Request 892: https://github.com/galaxyproject/planemo/pull/892
.. _Pull Request 891: https://github.com/galaxyproject/planemo/pull/891
.. _Pull Request 889: https://github.com/galaxyproject/planemo/pull/889
.. _Pull Request 888: https://github.com/galaxyproject/planemo/pull/888
.. _Pull Request 887: https://github.com/galaxyproject/planemo/pull/887
.. _Pull Request 882: https://github.com/galaxyproject/planemo/pull/882
.. _Pull Request 877: https://github.com/galaxyproject/planemo/pull/877
.. _Pull Request 874: https://github.com/galaxyproject/planemo/pull/874
.. _Pull Request 871: https://github.com/galaxyproject/planemo/pull/871
.. _Pull Request 870: https://github.com/galaxyproject/planemo/pull/870
.. _Pull Request 864: https://github.com/galaxyproject/planemo/pull/864
.. _Pull Request 867: https://github.com/galaxyproject/planemo/pull/867
.. _Pull Request 868: https://github.com/galaxyproject/planemo/pull/868
.. _bad810a: https://github.com/galaxyproject/planemo/commit/bad810a
.. _Pull Request 851: https://github.com/galaxyproject/planemo/pull/851
.. _Pull Request 856: https://github.com/galaxyproject/planemo/pull/856
.. _Pull Request 860: https://github.com/galaxyproject/planemo/pull/860
.. _Pull Request 866: https://github.com/galaxyproject/planemo/pull/866
.. _Pull Request 861: https://github.com/galaxyproject/planemo/pull/861
.. _324c776: https://github.com/galaxyproject/planemo/commit/324c776
.. _72d2ca7: https://github.com/galaxyproject/planemo/commit/72d2ca7
.. _b12b117: https://github.com/galaxyproject/planemo/commit/b12b117
.. _016b923: https://github.com/galaxyproject/planemo/commit/016b923
.. _2002b49: https://github.com/galaxyproject/planemo/commit/2002b49
.. _Pull Request 843: https://github.com/galaxyproject/planemo/pull/843
.. _Pull Request 842: https://github.com/galaxyproject/planemo/pull/842
.. _Pull Request 841: https://github.com/galaxyproject/planemo/pull/841
.. _Pull Request 847: https://github.com/galaxyproject/planemo/pull/847
.. _Pull Request 848: https://github.com/galaxyproject/planemo/pull/848
.. _Pull Request 849: https://github.com/galaxyproject/planemo/pull/849
.. _Pull Request 850: https://github.com/galaxyproject/planemo/pull/850
.. _Pull Request 836: https://github.com/galaxyproject/planemo/pull/836
.. _Pull Request 833: https://github.com/galaxyproject/planemo/pull/833
.. _Pull Request 837: https://github.com/galaxyproject/planemo/pull/837
.. _Pull Request 840: https://github.com/galaxyproject/planemo/pull/840
.. _Pull Request 838: https://github.com/galaxyproject/planemo/pull/838
.. _Pull Request 834: https://github.com/galaxyproject/planemo/pull/834
.. _Pull Request 835: https://github.com/galaxyproject/planemo/pull/835
.. _347c622: https://github.com/galaxyproject/planemo/commit/347c622
.. _Pull Request 832: https://github.com/galaxyproject/planemo/pull/832
.. _Pull Request 831: https://github.com/galaxyproject/planemo/pull/831
.. _Pull Request 830: https://github.com/galaxyproject/planemo/pull/830
.. _Pull Request 829: https://github.com/galaxyproject/planemo/pull/829
.. _Pull Request 828: https://github.com/galaxyproject/planemo/pull/828
.. _Pull Request 826: https://github.com/galaxyproject/planemo/pull/826
.. _Pull Request 827: https://github.com/galaxyproject/planemo/pull/827
.. _Pull Request 825: https://github.com/galaxyproject/planemo/pull/825
.. _Pull Request 820: https://github.com/galaxyproject/planemo/pull/820
.. _Pull Request 823: https://github.com/galaxyproject/planemo/pull/823
.. _Pull Request 822: https://github.com/galaxyproject/planemo/pull/822
.. _a5c72e3: https://github.com/galaxyproject/planemo/commit/a5c72e3
.. _Pull Request 818: https://github.com/galaxyproject/planemo/pull/818
.. _Pull Request 816: https://github.com/galaxyproject/planemo/pull/816
.. _Pull Request 817: https://github.com/galaxyproject/planemo/pull/817
.. _Pull Request 795: https://github.com/galaxyproject/planemo/pull/795
.. _Pull Request 799: https://github.com/galaxyproject/planemo/pull/799
.. _Pull Request 800: https://github.com/galaxyproject/planemo/pull/800
.. _Pull Request 781: https://github.com/galaxyproject/planemo/pull/781
.. _Pull Request 801: https://github.com/galaxyproject/planemo/pull/801
.. _Pull Request 802: https://github.com/galaxyproject/planemo/pull/802
.. _Pull Request 803: https://github.com/galaxyproject/planemo/pull/803
.. _Pull Request 805: https://github.com/galaxyproject/planemo/pull/805
.. _Pull Request 806: https://github.com/galaxyproject/planemo/pull/806
.. _Pull Request 809: https://github.com/galaxyproject/planemo/pull/809
.. _Pull Request 810: https://github.com/galaxyproject/planemo/pull/810
.. _Pull Request 787: https://github.com/galaxyproject/planemo/pull/787
.. _Pull Request 792: https://github.com/galaxyproject/planemo/pull/792
.. _dc443d6: https://github.com/galaxyproject/planemo/commit/dc443d6
.. _8cfe9e9: https://github.com/galaxyproject/planemo/commit/8cfe9e9
.. _41f7df1: https://github.com/galaxyproject/planemo/commit/41f7df1
.. _Pull Request 790: https://github.com/galaxyproject/planemo/pull/790
.. _Pull Request 776: https://github.com/galaxyproject/planemo/pull/776
.. _Pull Request 774: https://github.com/galaxyproject/planemo/pull/774
.. _Pull Request 773: https://github.com/galaxyproject/planemo/pull/773
.. _Pull Request 771: https://github.com/galaxyproject/planemo/pull/771
.. _Pull Request 770: https://github.com/galaxyproject/planemo/pull/770
.. _Pull Request 769: https://github.com/galaxyproject/planemo/pull/769
.. _Pull Request 768: https://github.com/galaxyproject/planemo/pull/768
.. _Pull Request 764: https://github.com/galaxyproject/planemo/pull/764
.. _Pull Request 761: https://github.com/galaxyproject/planemo/pull/761
.. _Pull Request 759: https://github.com/galaxyproject/planemo/pull/759
.. _Pull Request 756: https://github.com/galaxyproject/planemo/pull/756
.. _Pull Request 753: https://github.com/galaxyproject/planemo/pull/753
.. _Pull Request 747: https://github.com/galaxyproject/planemo/pull/747
.. _Pull Request 745: https://github.com/galaxyproject/planemo/pull/745
.. _Pull Request 743: https://github.com/galaxyproject/planemo/pull/743
.. _Pull Request 739: https://github.com/galaxyproject/planemo/pull/739
.. _Pull Request 738: https://github.com/galaxyproject/planemo/pull/738
.. _Pull Request 725: https://github.com/galaxyproject/planemo/pull/725
.. _Pull Request 727: https://github.com/galaxyproject/planemo/pull/727
.. _Pull Request 729: https://github.com/galaxyproject/planemo/pull/729
.. _Pull Request 730: https://github.com/galaxyproject/planemo/pull/730
.. _Pull Request 731: https://github.com/galaxyproject/planemo/pull/731
.. _Pull Request 733: https://github.com/galaxyproject/planemo/pull/733
.. _Pull Request 732: https://github.com/galaxyproject/planemo/pull/732
.. _Pull Request 704: https://github.com/galaxyproject/planemo/pull/704
.. _Pull Request 709: https://github.com/galaxyproject/planemo/pull/709
.. _Pull Request 715: https://github.com/galaxyproject/planemo/pull/715
.. _Pull Request 716: https://github.com/galaxyproject/planemo/pull/716
.. _Pull Request 720: https://github.com/galaxyproject/planemo/pull/720
.. _Pull Request 723: https://github.com/galaxyproject/planemo/pull/723
.. _8a608e0: https://github.com/galaxyproject/planemo/commit/8a608e0
.. _ecc1bc2: https://github.com/galaxyproject/planemo/commit/ecc1bc2
.. _Pull Request 702: https://github.com/galaxyproject/planemo/pull/702
.. _Pull Request 701: https://github.com/galaxyproject/planemo/pull/701
.. _Pull Request 699: https://github.com/galaxyproject/planemo/pull/699
.. _91b6fa0: https://github.com/galaxyproject/planemo/commit/91b6fa0
.. _904d77a: https://github.com/galaxyproject/planemo/commit/904d77a
.. _9636682: https://github.com/galaxyproject/planemo/commit/9636682
.. _475104c: https://github.com/galaxyproject/planemo/commit/475104c
.. _Pull Request 684: https://github.com/galaxyproject/planemo/pull/684
.. _Pull Request 687: https://github.com/galaxyproject/planemo/pull/687
.. _Pull Request 688: https://github.com/galaxyproject/planemo/pull/688
.. _Pull Request 689: https://github.com/galaxyproject/planemo/pull/689
.. _Pull Request 690: https://github.com/galaxyproject/planemo/pull/690
.. _Issue 494: https://github.com/galaxyproject/planemo/issues/494
.. _Pull Request 665: https://github.com/galaxyproject/planemo/pull/665
.. _Pull Request 675: https://github.com/galaxyproject/planemo/pull/675
.. _Pull Request 680: https://github.com/galaxyproject/planemo/pull/680
.. _Pull Request 682: https://github.com/galaxyproject/planemo/pull/682
.. _Pull Request 683: https://github.com/galaxyproject/planemo/pull/683
.. _Pull Request 662: https://github.com/galaxyproject/planemo/pull/662
.. _Pull Request 665: https://github.com/galaxyproject/planemo/pull/665
.. _Pull Request 664: https://github.com/galaxyproject/planemo/pull/664
.. _84c4a73: https://github.com/galaxyproject/planemo/commit/84c4a73
.. _32f41c9: https://github.com/galaxyproject/planemo/commit/32f41c9
.. _3129216: https://github.com/galaxyproject/planemo/commit/3129216
.. _b4ae44d: https://github.com/galaxyproject/planemo/commit/b4ae44d
.. _3c95b7b: https://github.com/galaxyproject/planemo/commit/3c95b7b
.. _06bcf19: https://github.com/galaxyproject/planemo/commit/06bcf19
.. _525de8f: https://github.com/galaxyproject/planemo/commit/525de8f
.. _9867e56: https://github.com/galaxyproject/planemo/commit/9867e56
.. _ce0dc4e: https://github.com/galaxyproject/planemo/commit/ce0dc4e
.. _4c0f100: https://github.com/galaxyproject/planemo/commit/4c0f100
.. _04238d3: https://github.com/galaxyproject/planemo/commit/04238d3
.. _ced5ce2: https://github.com/galaxyproject/planemo/commit/ced5ce2
.. _9ab4a0d: https://github.com/galaxyproject/planemo/commit/9ab4a0d
.. _Pull Request 640: https://github.com/galaxyproject/planemo/pull/640
.. _0a1abfe: https://github.com/galaxyproject/planemo/commit/0a1abfe
.. _Pull Request 649: https://github.com/galaxyproject/planemo/pull/649
.. _Issue 620: https://github.com/galaxyproject/planemo/issues/620
.. _Pull Request 643: https://github.com/galaxyproject/planemo/pull/643
.. _Pull Request 642: https://github.com/galaxyproject/planemo/pull/642
.. _Pull Request 641: https://github.com/galaxyproject/planemo/pull/641
.. _Pull Request 639: https://github.com/galaxyproject/planemo/pull/639
.. _Pull Request 635: https://github.com/galaxyproject/planemo/pull/635
.. _Issue 633: https://github.com/galaxyproject/planemo/issues/633
.. _Issue 260: https://github.com/galaxyproject/planemo/issues/260
.. _Pull Request 638: https://github.com/galaxyproject/planemo/pull/638
.. _6638caa: https://github.com/galaxyproject/planemo/commit/6638caa
.. _8faf661: https://github.com/galaxyproject/planemo/commit/8faf661
.. _e343b67: https://github.com/galaxyproject/planemo/commit/e343b67
.. _Pull Request 634: https://github.com/galaxyproject/planemo/pull/634
.. _84ebc1f: https://github.com/galaxyproject/planemo/commit/84ebc1f
.. _03c9658: https://github.com/galaxyproject/planemo/commit/03c9658
.. _08c067c: https://github.com/galaxyproject/planemo/commit/08c067c
.. _fca4183: https://github.com/galaxyproject/planemo/commit/fca4183
.. _Issue 564: https://github.com/galaxyproject/planemo/issues/564
.. _Pull Request 628: https://github.com/galaxyproject/planemo/pull/628
.. _Issue 515: https://github.com/galaxyproject/planemo/issues/515
.. _Pull Request 629: https://github.com/galaxyproject/planemo/pull/629
.. _Pull Request 614: https://github.com/galaxyproject/planemo/pull/614
.. _32acd68: https://github.com/galaxyproject/planemo/commit/32acd68
.. _4595953: https://github.com/galaxyproject/planemo/commit/4595953
.. _Pull Request 612: https://github.com/galaxyproject/planemo/pull/612
.. _Issue 388: https://github.com/galaxyproject/planemo/issues/388
.. _Pull Request 610: https://github.com/galaxyproject/planemo/pull/610
.. _Pull Request 609: https://github.com/galaxyproject/planemo/pull/609
.. _Pull Request 608: https://github.com/galaxyproject/planemo/pull/608
.. _Pull Request 605: https://github.com/galaxyproject/planemo/pull/605
.. _Pull Request 606: https://github.com/galaxyproject/planemo/pull/606
.. _Pull Request 602: https://github.com/galaxyproject/planemo/pull/602
.. _Pull Request 570: https://github.com/galaxyproject/planemo/pull/570
.. _9228416: https://github.com/galaxyproject/planemo/commit/9228416
.. _50d3c4a: https://github.com/galaxyproject/planemo/commit/50d3c4a
.. _Issue 578: https://github.com/galaxyproject/planemo/issues/578
.. _Pull Request 591: https://github.com/galaxyproject/planemo/pull/591
.. _Pull Request 590: https://github.com/galaxyproject/planemo/pull/590
.. _f0da66f: https://github.com/galaxyproject/planemo/commit/f0da66f
.. _19b2ee9: https://github.com/galaxyproject/planemo/commit/19b2ee9
.. _9da8387: https://github.com/galaxyproject/planemo/commit/9da8387
.. _08cef54: https://github.com/galaxyproject/planemo/commit/08cef54
.. _2e4e5fc: https://github.com/galaxyproject/planemo/commit/2e4e5fc
.. _2e4e5fc: https://github.com/galaxyproject/planemo/commit/2e4e5fc
.. _Issue 573: https://github.com/galaxyproject/planemo/issues/573
.. _Pull Request 579: https://github.com/galaxyproject/planemo/pull/579
.. _ccdd2d5: https://github.com/galaxyproject/planemo/commit/ccdd2d5
.. _e925ba1: https://github.com/galaxyproject/planemo/commit/e925ba1
.. _ea5324f: https://github.com/galaxyproject/planemo/commit/ea5324f
.. _ca88b0c: https://github.com/galaxyproject/planemo/commit/ca88b0c
.. _b6d8294: https://github.com/galaxyproject/planemo/commit/b6d8294
.. _6a6f164: https://github.com/galaxyproject/planemo/commit/6a6f164
.. _d6da3a8: https://github.com/galaxyproject/planemo/commit/d6da3a8
.. _1ef05d2: https://github.com/galaxyproject/planemo/commit/1ef05d2
.. _7cca2e4: https://github.com/galaxyproject/planemo/commit/7cca2e4
.. _34538de: https://github.com/galaxyproject/planemo/commit/34538de
.. _6f91719: https://github.com/galaxyproject/planemo/commit/6f91719
.. _Pull Request 566: https://github.com/galaxyproject/planemo/pull/566
.. _Pull Request 559: https://github.com/galaxyproject/planemo/pull/559
.. _Pull Request 561: https://github.com/galaxyproject/planemo/pull/561
.. _Pull Request 565: https://github.com/galaxyproject/planemo/pull/565
.. _Pull Request 555: https://github.com/galaxyproject/planemo/pull/555
.. _a8e797b: https://github.com/galaxyproject/planemo/commit/a8e797b
.. _6c03de8: https://github.com/galaxyproject/planemo/commit/6c03de8
.. _ef4b9f4: https://github.com/galaxyproject/planemo/commit/ef4b9f4
.. _f7b6c7e: https://github.com/galaxyproject/planemo/commit/f7b6c7e
.. _07d94bd: https://github.com/galaxyproject/planemo/commit/07d94bd
.. _ca19910: https://github.com/galaxyproject/planemo/commit/ca19910
.. _24008ab: https://github.com/galaxyproject/planemo/commit/24008ab
.. _ce44e87: https://github.com/galaxyproject/planemo/commit/ce44e87
.. _Pull Request 550: https://github.com/galaxyproject/planemo/pull/550
.. _c2204b3: https://github.com/galaxyproject/planemo/commit/c2204b3
.. _c262b6d: https://github.com/galaxyproject/planemo/commit/c262b6d
.. _Pull Request 539: https://github.com/galaxyproject/planemo/pull/539
.. _Pull Request 541: https://github.com/galaxyproject/planemo/pull/541
.. _Pull Request 540: https://github.com/galaxyproject/planemo/pull/540
.. _Pull Request 545: https://github.com/galaxyproject/planemo/pull/545
.. _Pull Request 546: https://github.com/galaxyproject/planemo/pull/546
.. _3ceaa40: https://github.com/galaxyproject/planemo/commit/3ceaa40
.. _057f4f0: https://github.com/galaxyproject/planemo/commit/057f4f0
.. _9fdf490: https://github.com/galaxyproject/planemo/commit/9fdf490
.. _8c088c6: https://github.com/galaxyproject/planemo/commit/8c088c6
.. _e2398fb: https://github.com/galaxyproject/planemo/commit/e2398fb
.. _Pull Request 526: https://github.com/galaxyproject/planemo/pull/526
.. _Pull Request 528: https://github.com/galaxyproject/planemo/pull/528
.. _Pull Request 525: https://github.com/galaxyproject/planemo/pull/525
.. _a811e65: https://github.com/galaxyproject/planemo/commit/a811e65
.. _Pull Request 521: https://github.com/galaxyproject/planemo/pull/521
.. _a066afb: https://github.com/galaxyproject/planemo/commit/a066afb
.. _Pull Request 512: https://github.com/galaxyproject/planemo/pull/512
.. _08bb354: https://github.com/galaxyproject/planemo/commit/08bb354
.. _Pull Request 513: https://github.com/galaxyproject/planemo/pull/513
.. _Pull Request 510: https://github.com/galaxyproject/planemo/pull/510
.. _e890ab5: https://github.com/galaxyproject/planemo/commit/e890ab5
.. _Pull Request 507: https://github.com/galaxyproject/planemo/pull/507
.. _d53bcd6: https://github.com/galaxyproject/planemo/commit/d53bcd6
.. _725b232: https://github.com/galaxyproject/planemo/commit/725b232
.. _Pull Request 498: https://github.com/galaxyproject/planemo/pull/498
.. _01584c5: https://github.com/galaxyproject/planemo/commit/01584c5
.. _01f2af9: https://github.com/galaxyproject/planemo/commit/01f2af9
.. _0298510: https://github.com/galaxyproject/planemo/commit/0298510
.. _02a08a0: https://github.com/galaxyproject/planemo/commit/02a08a0
.. _05cc9f4: https://github.com/galaxyproject/planemo/commit/05cc9f485ee87bc344e3f43bb1cfd025a16a6247
.. _069e7ba: https://github.com/galaxyproject/planemo/commit/069e7ba
.. _08de8de: https://github.com/galaxyproject/planemo/commit/08de8de
.. _0bd4ff0: https://github.com/galaxyproject/planemo/commit/0bd4ff0
.. _0e4f70a: https://github.com/galaxyproject/planemo/commit/0e4f70a
.. _0f8cb10: https://github.com/galaxyproject/planemo/commit/0f8cb10
.. _13a5ae7: https://github.com/galaxyproject/planemo/commit/13a5ae7
.. _15804be: https://github.com/galaxyproject/planemo/commit/15804be
.. _15d33c7: https://github.com/galaxyproject/planemo/commit/15d33c7
.. _182fe57: https://github.com/galaxyproject/planemo/commit/182fe57
.. _1927168: https://github.com/galaxyproject/planemo/commit/1927168
.. _1982076: https://github.com/galaxyproject/planemo/commit/1982076
.. _19900a6: https://github.com/galaxyproject/planemo/commit/19900a6
.. _1a157d4: https://github.com/galaxyproject/planemo/commit/1a157d4
.. _1a85493: https://github.com/galaxyproject/planemo/commit/1a85493
.. _1c6cfbb: https://github.com/galaxyproject/planemo/commit/1c6cfbb
.. _1c7ee5b: https://github.com/galaxyproject/planemo/commit/1c7ee5b
.. _1cd0e2d: https://github.com/galaxyproject/planemo/commit/1cd0e2d
.. _1e3668a: https://github.com/galaxyproject/planemo/commit/1e3668a
.. _2052db0: https://github.com/galaxyproject/planemo/commit/2052db0
.. _20a8680: https://github.com/galaxyproject/planemo/commit/20a86807cb7ea87db2dbc0197ae08a40df3ab2bc
.. _21bb463: https://github.com/galaxyproject/planemo/commit/21bb463ad6c321bcb669603049a5e89a69766ad9
.. _25ef0d5: https://github.com/galaxyproject/planemo/commit/25ef0d5
.. _26e378e: https://github.com/galaxyproject/planemo/commit/26e378e
.. _26e3cdb: https://github.com/galaxyproject/planemo/commit/26e3cdb
.. _2a7c792: https://github.com/galaxyproject/planemo/commit/2a7c792
.. _2ae2b49: https://github.com/galaxyproject/planemo/commit/2ae2b49
.. _2e41e0a: https://github.com/galaxyproject/planemo/commit/2e41e0a
.. _2f66fc3: https://github.com/galaxyproject/planemo/commit/2f66fc3
.. _30a9c3f: https://github.com/galaxyproject/planemo/commit/30a9c3f
.. _32c6e7f: https://github.com/galaxyproject/planemo/commit/32c6e7f78bb8f04d27615cfd8948b0b89f27b4e6
.. _33294d2: https://github.com/galaxyproject/planemo/commit/33294d2
.. _334f2d4: https://github.com/galaxyproject/planemo/commit/334f2d4
.. _343902d: https://github.com/galaxyproject/planemo/commit/343902d
.. _3499ca0: https://github.com/galaxyproject/planemo/commit/3499ca0a15affcaf8ac9efc55880da40b0626679
.. _358a42c: https://github.com/galaxyproject/planemo/commit/358a42c
.. _36ac6d8: https://github.com/galaxyproject/planemo/commit/36ac6d8
.. _36f7cb1: https://github.com/galaxyproject/planemo/commit/36f7cb114f77731f90860d513a930e10ce5c1ba5
.. _37dcc07: https://github.com/galaxyproject/planemo/commit/37dcc07
.. _39fedd2: https://github.com/galaxyproject/planemo/commit/39fedd2
.. _3f4ab44: https://github.com/galaxyproject/planemo/commit/3f4ab44
.. _40a1f57: https://github.com/galaxyproject/planemo/commit/40a1f57
.. _411a8da: https://github.com/galaxyproject/planemo/commit/411a8da21c92ba37c7ad95bfce9928d9b8fd998e
.. _44de95c: https://github.com/galaxyproject/planemo/commit/44de95c0d7087a5822941959f9a062f6382e329b
.. _45135ff: https://github.com/galaxyproject/planemo/commit/45135ff
.. _4823c5e: https://github.com/galaxyproject/planemo/commit/4823c5e
.. _49c5c1e: https://github.com/galaxyproject/planemo/commit/49c5c1e
.. _4c71299: https://github.com/galaxyproject/planemo/commit/4c71299
.. _4cd571c: https://github.com/galaxyproject/planemo/commit/4cd571c
.. _4d29bf1: https://github.com/galaxyproject/planemo/commit/4d29bf1
.. _4d6f7d9: https://github.com/galaxyproject/planemo/commit/4d6f7d9
.. _4e1377c: https://github.com/galaxyproject/planemo/commit/4e1377c
.. _4f61025: https://github.com/galaxyproject/planemo/commit/4f61025
.. _508dce7: https://github.com/galaxyproject/planemo/commit/508dce7
.. _53a6766: https://github.com/galaxyproject/planemo/commit/53a6766cdebdddc976189f6dc6a264bb4105c4bf
.. _53edd99: https://github.com/galaxyproject/planemo/commit/53edd99
.. _552059f: https://github.com/galaxyproject/planemo/commit/552059f
.. _572e754: https://github.com/galaxyproject/planemo/commit/572e754
.. _5b97f2e: https://github.com/galaxyproject/planemo/commit/5b97f2e
.. _5d08b67: https://github.com/galaxyproject/planemo/commit/5d08b67
.. _5d7db92: https://github.com/galaxyproject/planemo/commit/5d7db92
.. _5e0b6d1: https://github.com/galaxyproject/planemo/commit/5e0b6d1
.. _63cd431: https://github.com/galaxyproject/planemo/commit/63cd431
.. _63e456c: https://github.com/galaxyproject/planemo/commit/63e456c
.. _6409449: https://github.com/galaxyproject/planemo/commit/6409449
.. _6514ff5: https://github.com/galaxyproject/planemo/commit/6514ff5
.. _65b999d: https://github.com/galaxyproject/planemo/commit/65b999d21bacc133a80ecf5f61e0728afec66ccc
.. _6b4e7a6: https://github.com/galaxyproject/planemo/commit/6b4e7a6
.. _6bcf699: https://github.com/galaxyproject/planemo/commit/6bcf699
.. _6d0f502: https://github.com/galaxyproject/planemo/commit/6d0f502
.. _6d81a94: https://github.com/galaxyproject/planemo/commit/6d81a94
.. _6e1e726: https://github.com/galaxyproject/planemo/commit/6e1e726
.. _7572e99: https://github.com/galaxyproject/planemo/commit/7572e99
.. _764ce01: https://github.com/galaxyproject/planemo/commit/764ce01
.. _775bf49: https://github.com/galaxyproject/planemo/commit/775bf49
.. _776773c: https://github.com/galaxyproject/planemo/commit/776773c
.. _78f8274: https://github.com/galaxyproject/planemo/commit/78f82747996e4a28f96c85ad72efe5e54c8c74bd
.. _7be1bf5: https://github.com/galaxyproject/planemo/commit/7be1bf5
.. _7c69bf6: https://github.com/galaxyproject/planemo/commit/7c69bf6
.. _7d07782: https://github.com/galaxyproject/planemo/commit/7d077828559c9c9c352ac814f9e3b86b1b3a2a9f
.. _8117e03: https://github.com/galaxyproject/planemo/commit/8117e03
.. _8207026: https://github.com/galaxyproject/planemo/commit/8207026
.. _826d371: https://github.com/galaxyproject/planemo/commit/826d371
.. _82e8b1f: https://github.com/galaxyproject/planemo/commit/82e8b1f17eae526aeb341cb4fffb8d09d73bb419
.. _834bfb2: https://github.com/galaxyproject/planemo/commit/834bfb2929d367892a3abe9c0b88d5a0277d7905
.. _83e227a: https://github.com/galaxyproject/planemo/commit/83e227a
.. _85b9614: https://github.com/galaxyproject/planemo/commit/85b961465f46351507f80ddc3758349535060502
.. _89674cb: https://github.com/galaxyproject/planemo/commit/89674cb
.. _8b31850: https://github.com/galaxyproject/planemo/commit/8b31850
.. _8e96864: https://github.com/galaxyproject/planemo/commit/8e96864
.. _8eda729: https://github.com/galaxyproject/planemo/commit/8eda729
.. _912df02: https://github.com/galaxyproject/planemo/commit/912df02
.. _916f610: https://github.com/galaxyproject/planemo/commit/916f610
.. _93b7bda: https://github.com/galaxyproject/planemo/commit/93b7bda
.. _94097c7: https://github.com/galaxyproject/planemo/commit/94097c7
.. _9427b47: https://github.com/galaxyproject/planemo/commit/9427b47
.. _94645ed: https://github.com/galaxyproject/planemo/commit/94645ed
.. _949a36d: https://github.com/galaxyproject/planemo/commit/949a36d
.. _95d5cba: https://github.com/galaxyproject/planemo/commit/95d5cba
.. _965511d: https://github.com/galaxyproject/planemo/commit/965511d
.. _988de1d: https://github.com/galaxyproject/planemo/commit/988de1d
.. _98fdc8c: https://github.com/galaxyproject/planemo/commit/98fdc8c
.. _99ee51a: https://github.com/galaxyproject/planemo/commit/99ee51a
.. _9bf1eab: https://github.com/galaxyproject/planemo/commit/9bf1eab
.. _9e746b4: https://github.com/galaxyproject/planemo/commit/9e746b455e3b15219878cddcdeda722979639401
.. _9f3957d: https://github.com/galaxyproject/planemo/commit/9f3957d
.. _9ff0d2d: https://github.com/galaxyproject/planemo/commit/9ff0d2d
.. _CWL: http://www.commonwl.org/
.. _Issue 108: https://github.com/galaxyproject/planemo/issues/108
.. _Issue 114: https://github.com/galaxyproject/planemo/issues/114
.. _Issue 118: https://github.com/galaxyproject/planemo/issues/118
.. _Issue 124: https://github.com/galaxyproject/planemo/issues/#124
.. _Issue 138: https://github.com/galaxyproject/planemo/issues/#138
.. _Issue 139: https://github.com/galaxyproject/planemo/issues/139
.. _Issue 150: https://github.com/galaxyproject/planemo/issues/150
.. _Issue 156: https://github.com/galaxyproject/planemo/issues/156
.. _Issue 158: https://github.com/galaxyproject/planemo/issues/158
.. _Issue 159: https://github.com/galaxyproject/planemo/issues/159
.. _Issue 15: https://github.com/galaxyproject/planemo/issues/15
.. _Issue 161: https://github.com/galaxyproject/planemo/issues/161
.. _Issue 167: https://github.com/galaxyproject/planemo/issues/167
.. _Issue 168: https://github.com/galaxyproject/planemo/issues/168
.. _Issue 169: https://github.com/galaxyproject/planemo/issues/169
.. _Issue 170: https://github.com/galaxyproject/planemo/issues/170
.. _Issue 176: https://github.com/galaxyproject/planemo/issues/176
.. _Issue 179: https://github.com/galaxyproject/planemo/issues/179
.. _Issue 180: https://github.com/galaxyproject/planemo/issues/180
.. _Issue 181: https://github.com/galaxyproject/planemo/issues/181
.. _Issue 184: https://github.com/galaxyproject/planemo/issues/184
.. _Issue 186: https://github.com/galaxyproject/planemo/issues/186
.. _Issue 188: https://github.com/galaxyproject/planemo/issues/188
.. _Issue 189: https://github.com/galaxyproject/planemo/issues/189
.. _Issue 192: https://github.com/galaxyproject/planemo/issues/192
.. _Issue 205: https://github.com/galaxyproject/planemo/issues/205
.. _Issue 206: https://github.com/galaxyproject/planemo/issues/206
.. _Issue 209: https://github.com/galaxyproject/planemo/issues/209
.. _Issue 211: https://github.com/galaxyproject/planemo/issues/211
.. _Issue 217: https://github.com/galaxyproject/planemo/issues/217
.. _Issue 223: https://github.com/galaxyproject/planemo/issues/223
.. _Issue 231: https://github.com/galaxyproject/planemo/issues/231
.. _Issue 233: https://github.com/galaxyproject/planemo/issues/233
.. _Issue 240: https://github.com/galaxyproject/planemo/issues/240
.. _Issue 243: https://github.com/galaxyproject/planemo/issues/243
.. _Issue 245: https://github.com/galaxyproject/planemo/issues/245
.. _Issue 246: https://github.com/galaxyproject/planemo/issues/246
.. _Issue 272: https://github.com/galaxyproject/planemo/issues/272
.. _Issue 303: https://github.com/galaxyproject/planemo/issues/303
.. _Issue 313: https://github.com/galaxyproject/planemo/issues/313
.. _Issue 329: https://github.com/galaxyproject/planemo/issues/329
.. _Issue 333: https://github.com/galaxyproject/planemo/issues/333
.. _Issue 361: https://github.com/galaxyproject/planemo/issues/361
.. _Issue 362: https://github.com/galaxyproject/planemo/issues/362
.. _Issue 373: https://github.com/galaxyproject/planemo/issues/373
.. _Issue 391: https://github.com/galaxyproject/planemo/issues/391
.. _Issue 416: https://github.com/galaxyproject/planemo/issues/416
.. _Issue 420: https://github.com/galaxyproject/planemo/issues/420
.. _Issue 475: https://github.com/galaxyproject/planemo/issues/475
.. _Issue 61: https://github.com/galaxyproject/planemo/issues/61
.. _Issue 70: https://github.com/galaxyproject/planemo/issues/70
.. _Issue 78: https://github.com/galaxyproject/planemo/issues/78
.. _Issue 80: https://github.com/galaxyproject/planemo/issues/80
.. _Issue 83: https://github.com/galaxyproject/planemo/issues/83
.. _Issue 88: https://github.com/galaxyproject/planemo/issues/88
.. _Issue 89: https://github.com/galaxyproject/planemo/issues/#89
.. _Issue 91: https://github.com/galaxyproject/planemo/issues/#91
.. _Pull Request 101: https://github.com/galaxyproject/planemo/pull/101
.. _Pull Request 102: https://github.com/galaxyproject/planemo/pull/102
.. _Pull Request 104: https://github.com/galaxyproject/planemo/pull/104
.. _Pull Request 111: https://github.com/galaxyproject/planemo/pull/111
.. _Pull Request 113: https://github.com/galaxyproject/planemo/pull/113
.. _Pull Request 129: https://github.com/galaxyproject/planemo/pull/129
.. _Pull Request 130: https://github.com/galaxyproject/planemo/pull/130
.. _Pull Request 143: https://github.com/galaxyproject/planemo/pull/143
.. _Pull Request 151: https://github.com/galaxyproject/planemo/pull/151
.. _Pull Request 155: https://github.com/galaxyproject/planemo/pull/155
.. _Pull Request 164: https://github.com/galaxyproject/planemo/pull/164
.. _Pull Request 171: https://github.com/galaxyproject/planemo/pull/171
.. _Pull Request 173: https://github.com/galaxyproject/planemo/pull/173
.. _Pull Request 175: https://github.com/galaxyproject/planemo/pull/175
.. _Pull Request 185: https://github.com/galaxyproject/planemo/pull/185
.. _Pull Request 186: https://github.com/galaxyproject/planemo/pull/186
.. _Pull Request 187: https://github.com/galaxyproject/planemo/pull/187
.. _Pull Request 190: https://github.com/galaxyproject/planemo/pull/190
.. _Pull Request 196: https://github.com/galaxyproject/planemo/pull/196
.. _Pull Request 1: https://github.com/galaxyproject/planemo/pull/1
.. _Pull Request 200: https://github.com/galaxyproject/planemo/pull/200
.. _Pull Request 203: https://github.com/galaxyproject/planemo/pull/203
.. _Pull Request 206: https://github.com/galaxyproject/planemo/pull/206
.. _Pull Request 207: https://github.com/galaxyproject/planemo/pull/207
.. _Pull Request 208: https://github.com/galaxyproject/planemo/pull/208
.. _Pull Request 210: https://github.com/galaxyproject/planemo/pull/210
.. _Pull Request 213: https://github.com/galaxyproject/planemo/pull/213
.. _Pull Request 215: https://github.com/galaxyproject/planemo/pull/215
.. _Pull Request 216: https://github.com/galaxyproject/planemo/pull/216
.. _Pull Request 22: https://github.com/galaxyproject/planemo/pull/22
.. _Pull Request 230: https://github.com/galaxyproject/planemo/pull/230
.. _Pull Request 235: https://github.com/galaxyproject/planemo/pull/235
.. _Pull Request 23: https://github.com/galaxyproject/planemo/pull/23
.. _Pull Request 251: https://github.com/galaxyproject/planemo/pull/251
.. _Pull Request 253: https://github.com/galaxyproject/planemo/pull/253
.. _Pull Request 254: https://github.com/galaxyproject/planemo/pull/254
.. _Pull Request 255: https://github.com/galaxyproject/planemo/pull/255
.. _Pull Request 256: https://github.com/galaxyproject/planemo/pull/256
.. _Pull Request 277: https://github.com/galaxyproject/planemo/pull/277
.. _Pull Request 278: https://github.com/galaxyproject/planemo/pull/278
.. _Pull Request 284: https://github.com/galaxyproject/planemo/pull/284
.. _Pull Request 285: https://github.com/galaxyproject/planemo/pull/285
.. _Pull Request 287: https://github.com/galaxyproject/planemo/pull/287
.. _Pull Request 292: https://github.com/galaxyproject/planemo/pull/292
.. _Pull Request 297: https://github.com/galaxyproject/planemo/pull/297
.. _Pull Request 29: https://github.com/galaxyproject/planemo/pull/29
.. _Pull Request 301: https://github.com/galaxyproject/planemo/pull/301
.. _Pull Request 304: https://github.com/galaxyproject/planemo/pull/304
.. _Pull Request 305: https://github.com/galaxyproject/planemo/pull/305
.. _Pull Request 307: https://github.com/galaxyproject/planemo/pull/307
.. _Pull Request 309: https://github.com/galaxyproject/planemo/pull/309
.. _Pull Request 310: https://github.com/galaxyproject/planemo/pull/310
.. _Pull Request 311: https://github.com/galaxyproject/planemo/pull/311
.. _Pull Request 312: https://github.com/galaxyproject/planemo/pull/312
.. _Pull Request 314: https://github.com/galaxyproject/planemo/pull/314
.. _Pull Request 316: https://github.com/galaxyproject/planemo/pull/316
.. _Pull Request 322: https://github.com/galaxyproject/planemo/pull/322
.. _Pull Request 327: https://github.com/galaxyproject/planemo/pull/327
.. _Pull Request 330: https://github.com/galaxyproject/planemo/pull/330
.. _Pull Request 333: https://github.com/galaxyproject/planemo/pull/333
.. _Pull Request 334: https://github.com/galaxyproject/planemo/pull/334
.. _Pull Request 335: https://github.com/galaxyproject/planemo/pull/335
.. _Pull Request 339: https://github.com/galaxyproject/planemo/pull/339
.. _Pull Request 33: https://github.com/galaxyproject/planemo/pull/33
.. _Pull Request 343: https://github.com/galaxyproject/planemo/pull/343
.. _Pull Request 344: https://github.com/galaxyproject/planemo/pull/344
.. _Pull Request 345: https://github.com/galaxyproject/planemo/pull/345
.. _Pull Request 350: https://github.com/galaxyproject/planemo/pull/350
.. _Pull Request 351: https://github.com/galaxyproject/planemo/pull/351
.. _Pull Request 356: https://github.com/galaxyproject/planemo/pull/356
.. _Pull Request 375: https://github.com/galaxyproject/planemo/pull/375
.. _Pull Request 390: https://github.com/galaxyproject/planemo/pull/390
.. _Pull Request 394: https://github.com/galaxyproject/planemo/pull/394
.. _Pull Request 398: https://github.com/galaxyproject/planemo/pull/398
.. _Pull Request 403: https://github.com/galaxyproject/planemo/pull/403
.. _Pull Request 40: https://github.com/galaxyproject/planemo/pull/40
.. _Pull Request 425: https://github.com/galaxyproject/planemo/pull/425
.. _Pull Request 426: https://github.com/galaxyproject/planemo/pull/426
.. _Pull Request 428: https://github.com/galaxyproject/planemo/pull/428
.. _Pull Request 429: https://github.com/galaxyproject/planemo/pull/429
.. _Pull Request 454: https://github.com/galaxyproject/planemo/pull/454
.. _Pull Request 472: https://github.com/galaxyproject/planemo/pull/472
.. _Pull Request 479: https://github.com/galaxyproject/planemo/pull/479
.. _Pull Request 480: https://github.com/galaxyproject/planemo/pull/480
.. _Pull Request 484: https://github.com/galaxyproject/planemo/pull/484
.. _Pull Request 488: https://github.com/galaxyproject/planemo/pull/488
.. _Pull Request 491: https://github.com/galaxyproject/planemo/pull/491
.. _Pull Request 51: https://github.com/galaxyproject/planemo/pull/51
.. _Pull Request 56: https://github.com/galaxyproject/planemo/pull/56
.. _Pull Request 63: https://github.com/galaxyproject/planemo/pull/63
.. _Pull Request 68: https://github.com/galaxyproject/planemo/pull/68
.. _Pull Request 6: https://github.com/galaxyproject/planemo/pull/6
.. _Pull Request 98: https://github.com/galaxyproject/planemo/pull/98
.. _Pull Request 99: https://github.com/galaxyproject/planemo/pull/99
.. _XSD: http://www.w3schools.com/schema/
.. _a13a120: https://github.com/galaxyproject/planemo/commit/a13a120
.. _a2c13e4: https://github.com/galaxyproject/planemo/commit/a2c13e46259e3be35de1ecaae858ba818bb94734
.. _a2ee135: https://github.com/galaxyproject/planemo/commit/a2ee135
.. _a4110a8: https://github.com/galaxyproject/planemo/commit/a4110a85a770988e5cd3c31ccc9475717897d59c
.. _a4e6958: https://github.com/galaxyproject/planemo/commit/a4e6958
.. _a58a3b8: https://github.com/galaxyproject/planemo/commit/a58a3b8
.. _a87899b: https://github.com/galaxyproject/planemo/commit/a87899b
.. _aad1eed: https://github.com/galaxyproject/planemo/commit/aad1eed
.. _ac4f828: https://github.com/galaxyproject/planemo/commit/ac4f82898f7006799142503a33c3978428660ce7
.. _ad3b2f0: https://github.com/galaxyproject/planemo/commit/ad3b2f0
.. _af39061: https://github.com/galaxyproject/planemo/commit/af390612004dab636d8696839bb723d39f97c85d
.. _af7448c: https://github.com/galaxyproject/planemo/commit/af7448c
.. _b0b867e: https://github.com/galaxyproject/planemo/commit/b0b867e
.. _b1c8f1d: https://github.com/galaxyproject/planemo/commit/b1c8f1d
.. _b53006d: https://github.com/galaxyproject/planemo/commit/b53006d
.. _b757791: https://github.com/galaxyproject/planemo/commit/b757791
.. _b7d9e96: https://github.com/galaxyproject/planemo/commit/b7d9e96
.. _b86fe1f: https://github.com/galaxyproject/planemo/commit/b86fe1f
.. _b8d90ab: https://github.com/galaxyproject/planemo/commit/b8d90abab8bf53ae2e7cca4317223c01af9ab68c
.. _b9232e5: https://github.com/galaxyproject/planemo/commit/b9232e55e713abbd1d9ce8b0b34cbec6c701dc17
.. _badc25f: https://github.com/galaxyproject/planemo/commit/badc25fca495b61457ffb2e027f3fe9cf17c798f
.. _bioblend: https://github.com/galaxyproject/bioblend/
.. _c1713d2: https://github.com/galaxyproject/planemo/commit/c1713d2
.. _c23569f: https://github.com/galaxyproject/planemo/commit/c23569f
.. _c444855: https://github.com/galaxyproject/planemo/commit/c444855
.. _c4dfd55: https://github.com/galaxyproject/planemo/commit/c4dfd55
.. _c8640b6: https://github.com/galaxyproject/planemo/commit/c8640b6
.. _cb5b906: https://github.com/galaxyproject/planemo/commit/cb5b906
.. _cc1a447: https://github.com/galaxyproject/planemo/commit/cc1a447
.. _cc8abb6: https://github.com/galaxyproject/planemo/commit/cc8abb6
.. _ce8e1be: https://github.com/galaxyproject/planemo/commit/ce8e1be
.. _cwltool: https://github.com/common-workflow-language/cwltool/.. _d26929e: https://github.com/galaxyproject/planemo/commit/d26929e
.. _d26929e: https://github.com/galaxyproject/planemo/commit/d26929e
.. _d755fe7: https://github.com/galaxyproject/planemo/commit/d755fe7
.. _d76b489: https://github.com/galaxyproject/planemo/commit/d76b489
.. _d8f2038: https://github.com/galaxyproject/planemo/commit/d8f2038
.. _dad2d9d: https://github.com/galaxyproject/planemo/commit/dad2d9d
.. _dd94ddc: https://github.com/galaxyproject/planemo/commit/dd94ddc
.. _dff4f33: https://github.com/galaxyproject/planemo/commit/dff4f33c750a8dbe651c38e149a26dd42e706a82
.. _e0577e7: https://github.com/galaxyproject/planemo/commit/e0577e7
.. _e0acf91: https://github.com/galaxyproject/planemo/commit/e0acf91
.. _e38c436: https://github.com/galaxyproject/planemo/commit/e38c436
.. _e769118: https://github.com/galaxyproject/planemo/commit/e769118
.. _e8c1d45: https://github.com/galaxyproject/planemo/commit/e8c1d45f0c9a11bcf69ec2967836c3b8f432dd97
.. _eb039c0: https://github.com/galaxyproject/planemo/commit/eb039c0
.. _ec6e30f: https://github.com/galaxyproject/planemo/commit/ec6e30f
.. _efc5f30: https://github.com/galaxyproject/planemo/commit/efc5f30
.. _f0610d7: https://github.com/galaxyproject/planemo/commit/f0610d7
.. _f3394e7: https://github.com/galaxyproject/planemo/commit/f3394e7
.. _f3c6917: https://github.com/galaxyproject/planemo/commit/f3c6917
.. _f3cafaa: https://github.com/galaxyproject/planemo/commit/f3cafaa
.. _f7554d1: https://github.com/galaxyproject/planemo/commit/f7554d1
.. _f798c7e: https://github.com/galaxyproject/planemo/commit/f798c7e
.. _f854138: https://github.com/galaxyproject/planemo/commit/f854138
.. _f99f6c1: https://github.com/galaxyproject/planemo/commit/f99f6c1
.. _fba3874: https://github.com/galaxyproject/planemo/commit/fba3874
.. _fdb1b51: https://github.com/galaxyproject/planemo/commit/fdb1b51
.. _fdce74c: https://github.com/galaxyproject/planemo/commit/fdce74c
.. _fe7ad46: https://github.com/galaxyproject/planemo/commit/fe7ad46
.. _fea51fc: https://github.com/galaxyproject/planemo/commit/fea51fc
.. _lxml: http://lxml.de/
.. _nose: https://nose.readthedocs.org/en/latest/
.. _xmllint: http://xmlsoft.org/xmllint.html
.. _Conda: http://conda.pydata.org/
.. _Tool Factory: http://bioinformatics.oxfordjournals.org/content/early/2012/09/27/bioinformatics.bts573.full.pdf
.. _git: https://git-scm.com/
.. _anaconda-verify: https://github.com/ContinuumIO/anaconda-verify
.. _galaxy.xsd: https://github.com/galaxyproject/planemo/blob/master/planemo/xml/xsd/tool/galaxy.xsd
.. _setup.py: https://github.com/galaxyproject/planemo/blob/master/setup.py
.. _Bioconductor: https://www.bioconductor.org/
.. _tools-iuc: https://github.com/galaxyproject/tools-iuc
.. _PyPI: https://pypi.python.org/pypi
.. _Involucro: https://github.com/involucro/involucro
.. _Bioconda: https://bioconda.github.io/
.. _pip: https://pip.pypa.io/en/stable/
.. _BioContainers: http://biocontainers.pro/
.. _Toil: https://github.com/BD2KGenomics/toil
.. _quay.io: https://quay.io/
.. _galaxy-lib: https://github.com/galaxyproject/galaxy-lib
.. _gxwf: https://github.com/simonbray/gxwf
.. _Cheetah: https://cheetahtemplate.org/users_guide/intro.html
.. _Allure: http://allure.qatools.ru/
.. _@abretaud: https://github.com/abretaud
.. _@hexylena: https://github.com/hexylena
.. _@peterjc: https://github.com/peterjc
.. _@mr-c: https://github.com/mr-c
.. _@martenson: https://github.com/martenson
.. _@nsoranzo: https://github.com/nsoranzo
.. _@nturaga: https://github.com/nturaga
.. _@bgruening: https://github.com/bgruening
.. _@carlfeberhard: https://github.com/carlfeberhard
.. _@lparsons: https://github.com/lparsons
.. _@kellrott: https://github.com/kellrott
.. _@mvdbeek: https://github.com/mvdbeek
.. _@natefoo: https://github.com/natefoo
.. _@pstew: https://github.com/pstew
.. _@ramezrawas: https://github.com/ramezrawas
.. _@chambm: https://github.com/chambm
.. _@takadonet: https://github.com/takadonet
.. _@petrkadlec: https://github.com/petrkadlec
.. _@pvanheus: https://github.com/pvanheus
.. _@einon: https://github.com/einon
.. _@blankenberg: https://github.com/blankenberg
.. _@JeanFred: https://github.com/JeanFred
.. _@gregvonkuster: https://github.com/gregvonkuster
.. _@remimarenco: https://github.com/remimarenco
.. _@thriqon: https://github.com/thriqon
.. _@RJMW: https://github.com/RJMW
.. _@manabuishii: https://github.com/manabuishii
.. _@dfornika: https://github.com/dfornika
.. _@bernt-matthias: https://github.com/bernt-matthias
.. _@katrinleinweber: https://github.com/katrinleinweber
.. _@bebatut: https://github.com/bebatut
.. _@selten: https://github.com/selten
.. _@shiltemann: https://github.com/shiltemann
.. _@bedroesb: https://github.com/bedroesb
.. _@ic4f: https://github.com/ic4f
.. _@martin-raden: https://github.com/martin-raden
.. _@andreassko: https://github.com/andreassko
.. _@mblue9: https://github.com/mblue9
.. _@TMiguelT: https://github.com/TMiguelT
.. _@bedroesb: https://github.com/bedroesb
.. _@simonbray: https://github.com/simonbray
.. _@gallardoalba: https://github.com/gallardoalba
.. _@stain: https://github.com/stain
.. _@profgiuseppe: https://github.com/profgiuseppe
.. _@adRn-s: https://github.com/adRn-s
.. _@lldelisle: https://github.com/lldelisle
.. _@wm75: https://github.com/wm75
.. _@SimonWaldherr: https://github.com/SimonWaldherr
.. _@mstabrin: https://github.com/mstabrin
.. _@paulzierep: https://github.com/paulzierep
.. _@Kulivox: https://github.com/Kulivox
.. _@Delphine-L: https://github.com/Delphine-L
.. _@elichad: https://github.com/elichad
.. _@pavanvidem: https://github.com/pavanvidem
.. _@jdavcs: https://github.com/jdavcs
.. _@Smeds: https://github.com/Smeds
.. _@jmchilton: https://github.com/jmchilton
.. _@kostrykin: https://github.com/kostrykin
.. _@ahmedhamidawan: https://github.com/ahmedhamidawan
