import os
from os.path import expanduser

home = expanduser("~")
eia_root = f"{home}/data/eia-py"
eia_root = os.path.abspath(eia_root)


def ensure_exists(path):
    """ensure a given path exists

    Args:
        path: string representing a path.
    """
    assert isinstance(path, str)
    os.makedirs(path, exist_ok=True)


def get_base_dir():
    """returns a base directory for the eia data loader.

    This path follows the format: `~/data/eia-py`.
    If this directory does not exist, this method creates
    the directory.
    """
    ensure_exists(eia_root)
    return eia_root
