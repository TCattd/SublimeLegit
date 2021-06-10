# coding: utf-8
import sys
import logging

import sublime

# set up some logging
logging.basicConfig(level=logging.WARNING, format="[%(asctime)s - %(levelname)-8s - %(name)s] %(message)s")
logger = logging.getLogger('SublimeLegit')

# reload modules if necessary
LOAD_ORDER = [
    # base
    '',
    '.util',
    '.cmd',
    '.helpers',

    # meta
    '.sublimelegit',

    # extensions
    '.git_extensions.legit',
    '.git_extensions.git_flow',
]

needs_reload = [n for n, m in list(sys.modules.items()) if n[0:4] == 'slegit' and m is not None]

reloaded = []
for postfix in LOAD_ORDER:
    module = 'slegit' + postfix
    if module in needs_reload:
        reloaded.append(module)
        reload(sys.modules[module])
if reloaded:
    logger.info('Reloaded %s' % ", ".join(reloaded))


# import commands and listeners
if sys.version_info[0] == 2:
    settings = sublime.load_settings('SublimeLegit.sublime-settings')

    # set log level
    lvl = getattr(logging, settings.get('log_level', '').upper(), logging.WARNING)
    logger.setLevel(lvl)

    from slegit import *  # noqa
    from slegit.git_extensions.legit import *  # noqa
    from slegit.git_extensions.git_flow import *  # noqa

    # Enable plugins
    git_extensions.legit.enabled = settings.get('git_extensions', {}).get('legit', True)
    git_extensions.git_flow.enabled = settings.get('git_extensions', {}).get('git_flow', True)

    def unload_handler():
        logging.shutdown()
else:
    from .slegit import *  # noqa
    from .slegit.git_extensions.legit import *  # noqa
    from .slegit.git_extensions.git_flow import *  # noqa

    def plugin_loaded():
        settings = sublime.load_settings('SublimeLegit.sublime-settings')

        # set log level
        lvl = getattr(logging, settings.get('log_level', '').upper(), logging.WARNING)
        logger.setLevel(lvl)

        # Enable plugins
        git_extensions.legit.enabled = settings.get('git_extensions', {}).get('legit', True)
        git_extensions.git_flow.enabled = settings.get('git_extensions', {}).get('git_flow', True)

    def plugin_unloaded():
        logging.shutdown()
