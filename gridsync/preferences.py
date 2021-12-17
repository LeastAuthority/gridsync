# -*- coding: utf-8 -*-

import logging
import os
from typing import Optional

import attr
from twisted.python.filepath import FilePath

from gridsync import config_dir
from gridsync.config import Config

_default_config_path: FilePath = FilePath(config_dir).child("preferences.ini")


@attr.s
class Preferences:
    """
    Read and write simple values from a ini-syntax configuration file at a
    certain location.
    """

    config_file: FilePath = attr.ib(default=_default_config_path)

    def set(self, section: str, option: str, value) -> None:
        """
        Rewrite the configuration file with the given [section]option value added
        or changed.
        """
        set_preference(section, option, value, self.config_file.path)

    def get(self, section: str, option: str) -> str:
        """
        Read the value for the requested [section]option.
        """
        return get_preference(section, option, self.config_file.path)


def set_preference(
    section: str, option: str, value, config_file: Optional[str] = None
) -> None:
    if not config_file:
        config_file = os.path.join(config_dir, "preferences.ini")
    config = Config(config_file)
    config.set(section, option, value)
    logging.debug("Set user preference: %s %s %s", section, option, value)


def get_preference(
    section: str, option: str, config_file: Optional[str] = None
) -> str:
    if not config_file:
        config_file = os.path.join(config_dir, "preferences.ini")
    config = Config(config_file)
    return config.get(section, option)
