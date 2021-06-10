# coding: utf-8
import sys
import logging
import webbrowser

import sublime
from sublime_plugin import WindowCommand

from . import __version__


logger = logging.getLogger('SublimeLegit.sublimelegit')


class SublimeLegitVersionCommand(WindowCommand):
    """
    Show the currently installed version of SublimeLegit.
    """

    def run(self):
        sublime.message_dialog("You have SublimeLegit %s" % __version__)


class SublimeLegitDocumentationCommand(WindowCommand):
    """
    Open a webbrowser to the online SublimeLegit documentation.
    """

    URL = "https://github.com/TCattd/SublimeLegit/?utm_source=st%s&utm_medium=command&utm_campaign=docs"

    def run(self):
        url = self.URL % sys.version_info[0]
        webbrowser.open(url)
