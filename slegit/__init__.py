# coding: utf-8

__version__ = '1.0.0'

# Import all the commands

from .util import GitPanelWriteCommand, GitPanelAppendCommand

from .sublimelegit import (SublimeLegitDocumentationCommand, SublimeLegitVersionCommand)

# import plugins

from . import git_extensions
