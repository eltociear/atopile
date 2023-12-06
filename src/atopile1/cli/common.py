import functools
import logging
import sys
from pathlib import Path
from typing import Iterable

import click
from omegaconf import OmegaConf

from atopile.address import AddrStr, AddrValueError
from atopile.project.config import Config
from atopile.project.project import Project
from atopile.version import check_project_version

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def project_options(f):
    """
    Utility decorator to ingest common config options to build a project.
    """

    @click.argument("entry", required=False, default=None)
    @click.option("-b", "--build", default=None)
    @click.option("-c", "--config", multiple=True)
    @click.option("-t", "--target", multiple=True)
    @functools.wraps(f)
    def wrapper(
        *args,
        entry: str,
        build: str,
        config: Iterable[str],
        target: Iterable[str],
        **kwargs,
    ):
        # basic the entry address if provided, otherwise leave it as None
        if entry is not None:
            try:
                entry = AddrStr(entry)
            except AddrValueError as ex:
                raise click.BadParameter(
                    f"Invalid entry address {entry}.",
                    param_hint="entry",
                ) from ex

            if entry.file is None:
                raise click.BadParameter(
                    f"Invalid entry address {entry} - entry must specify a file.",
                    param_hint="entry",
                )

        # get the project
        try:
            project: Project = Project.from_path(entry.file if entry else Path.cwd())
        except FileNotFoundError as ex:
            raise click.BadParameter(
                f"Could not find project from path {str(entry.file)}. Is this file path within a project?"
            ) from ex

        log.info("Using project %s", project.root)

        # set the build config
        if build is not None:
            if build not in project.config.builds:
                raise click.BadParameter(
                    f'Could not find build-config "{build}". Available build configs are: {", ".join(project.config.builds.keys())}.'
                )
            project.config.selected_build_name = build

        # add custom config overrides
        if config:
            cli_conf = OmegaConf.from_dotlist(config)
        else:
            cli_conf = OmegaConf.create()

        # finally smoosh them all back together like a delicious cake
        # FIXME: why are we smooshing this -> does this need to be mutable?
        project.config: Config = OmegaConf.merge(project.config, cli_conf)

        # layer on the selected addrs config
        if entry and entry.file.is_file():
            # NOTE: we already check that entry.file isn't None if entry is specified
            if entry.ref:
                std_entry_file = project.standardise_import_path(entry.file.expanduser().resolve().absolute())
                project.config.selected_build.entry = AddrStr.from_parts(std_entry_file, entry.ref)
            else:
                raise click.BadParameter(
                    "If an entry of a file is specified, you must specify"
                    " the node within it you want to build.",
                    param_hint="entry",
                )

        # layer on selected targets
        if target:
            project.config.selected_build.targets = list(target)

        # perform pre-build checks
        if not check_project_version(project):
            sys.exit(1)

        # do the thing
        return f(*args, **kwargs, project=project)

    return wrapper