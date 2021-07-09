"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
``[options.entry_points]`` section in ``setup.cfg``::

    console_scripts =
         fibonacci = jolly_brancher.skeleton:run

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``fibonacci`` inside your current environment.

Besides console scripts, the header (i.e. until ``_logger``...) of this file can
also be used as template for Python modules.

Note:
    This skeleton file can be safely removed if not needed!

References:
    - https://setuptools.readthedocs.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""
import argparse
import logging
import os
import subprocess
import sys

from jira import JIRA
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

from jolly_brancher import __version__

# DONOTCOMMIT
REPO_ROOT = "/home/ahonnecke/src"
REMOTE = "upstream"
TOKEN = ""

__author__ = "Ashton Von Honnecke"
__copyright__ = "Ashton Von Honnecke"
__license__ = "MIT"

_logger = logging.getLogger(__name__)


# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.


def parse_args(args, repo_dirs):
    """
    Extract the CLI arguments from argparse
    """
    parser = argparse.ArgumentParser(description="Sweet branch creation tool")

    parser.add_argument(
        "--repo",
        help="Repository to create banch in",
        choices=repo_dirs,
        required=False,
    )

    parser.add_argument(
        "--parent",
        help="Parent branch",
        default="dev",
        required=False,
    )

    parser.add_argument("ticket", help="Ticket to build branch name from")

    parser.add_argument(
        "--version",
        action="version",
        version="jolly_brancher {ver}".format(ver=__version__),
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )

    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def main(args):
    """Wrapper allowing :func:`fib` to be called with string arguments in a CLI fashion

    Instead of returning the value from :func:`fib`, it prints the result to the
    ``stdout`` in a nicely formatted message.

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--verbose", "42"]``).
    """
    auth_email = "ashton.honnecke@us.panasonic.com"

    jira = JIRA("https://cirrusv2x.atlassian.net", basic_auth=(auth_email, TOKEN))

    repo_dirs = os.listdir(REPO_ROOT)
    args = parse_args(None, repo_dirs)

    if args.repo:
        repo = args.repo
    else:
        html_completer = WordCompleter(repo_dirs)
        repo = prompt("Choose repository: ", completer=html_completer)
        print("Using repository: %s" % repo)

    ticket = args.ticket.upper()
    myissue = jira.issue(ticket)

    summary = myissue.fields.summary
    summary = summary.replace(" ", "-")
    for bad_char in ["."]:
        summary = summary.replace(bad_char, "")

    issue_type = str(myissue.fields.issuetype)
    issue_type = issue_type.upper()

    branch_name = f"{issue_type}/{ticket}--{summary}"

    # We're assuming that the user has cded to the appropriate dir

    os.chdir(REPO_ROOT + "/" + repo)
    print(branch_name)

    # git.checkout('dev')
    # git.reset('--hard', 'upstream/dev')
    # git checkout -b feature/V2X-2226_add-the-following-curves-to-the-curve-database upstream/dev

    print(f"Creating the branch {branch_name}")
    cmd = ["git", "checkout", "-b", branch_name, f"{REMOTE}/{args.parent}"]

    subprocess.run(cmd, check=True)


def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`

    This function can be used as entry point to create console scripts with setuptools.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html

    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m jolly_brancher.skeleton 42
    #
    run()