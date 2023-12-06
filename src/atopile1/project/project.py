from itertools import chain
from pathlib import Path
from typing import Dict, Iterable, Optional, Tuple

from atopile.project.config import make_config


CONFIG_FILENAME = "ato.yaml"
ATO_DIR_NAME = ".ato"
MODULE_DIR_NAME = "modules"


def resolve_project_dir(path: Path):
    """
    Resolve the project directory from the specified path.
    """
    for p in [path] + list(path.parents):
        clean_path = p.resolve().absolute()
        if (clean_path / CONFIG_FILENAME).exists():
            return clean_path
    raise FileNotFoundError(
        f"Could not find {CONFIG_FILENAME} in {path} or any parents"
    )


class Project:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve().absolute()
        self._std_import_to_abs: Dict[Path, Path] = {}

        self.config = make_config(self.root / CONFIG_FILENAME)

        self.ato_dir = self.root / ATO_DIR_NAME
        self.module_dir = self.ato_dir / MODULE_DIR_NAME

    @classmethod
    def from_path(cls, path: Path) -> "Project":
        """
        Create a Project from the specified path.
        """
        return cls(resolve_project_dir(Path(path)))

    def ensure_build_dir(self):
        self.config.paths.build.mkdir(parents=True, exist_ok=True)

    def get_import_search_paths(self, cwp: Optional[Path] = None):
        if cwp is None:
            search_paths = [self.module_dir]
        else:
            if cwp.is_dir():
                search_paths = [cwp, self.module_dir]
            else:
                search_paths = [cwp.parent, self.module_dir]
        search_paths += [
            self.config.paths.abs_src,
        ]
        return search_paths

    def standardise_import_path(self, path: Path) -> Path:
        """Turn an absolute path into an ato-standardised import path for this project."""
        abs_path = path.resolve().absolute()
        project_src_path = self.config.paths.abs_src.resolve().absolute()

        if abs_path.is_relative_to(self.module_dir):
            std_path = abs_path.relative_to(self.module_dir)
        elif abs_path.is_relative_to(project_src_path):
            std_path = abs_path.relative_to(project_src_path)
        else:
            raise ImportError(
                f"Import {path} is outside the project directory"
                " and isn't part of the std lib"
            )

        if std_path in self._std_import_to_abs:
            if self._std_import_to_abs[std_path] != abs_path:
                # not sure we can ever hit this, but I wanna know about it if we can
                raise ImportError(
                    f"Import path {std_path} is ambiguous. This is"
                    " a core SW bug. Please report it."
                )
        else:
            self._std_import_to_abs[std_path] = abs_path
        return std_path

    def get_abs_import_path_from_std_path(self, std_path: Path) -> Path:
        if std_path in self._std_import_to_abs:
            return self._std_import_to_abs[std_path]
        else:
            raise ImportError(
                f"Import path {std_path} is not imported (or at least standardised)."
            )

    def resolve_import(
        self,
        name: str,
        cwp: Optional[Path] = None,
        additional_search_paths: Optional[Iterable[Path]] = None,
    ) -> Tuple[Path, Path]:
        non_relative_paths = []
        for path in chain(self.get_import_search_paths(cwp), additional_search_paths or []):
            abs_path = (path / name).resolve().absolute()
            if abs_path.exists():
                if not abs_path.is_relative_to(self.config.paths.abs_src.resolve().absolute()):
                    non_relative_paths.append(abs_path)
                return abs_path, self.standardise_import_path(abs_path)

        if non_relative_paths:
            raise FileNotFoundError(
                f"Found {len(non_relative_paths)} files with name {name}"
                " in the import search paths, but none are within the"
                " project itself."
            )
        raise FileNotFoundError(name)