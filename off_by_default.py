"""
uses logging with an explicit configuration, and a named logger
compared to on_by_default, this sets the logging only for our own app
"""

import verboselib
import logging

# Doing it this way, only WARN and higher from libraries come out,
# but you choose the level for your app.
log = logging.getLogger("my_app")
logging.basicConfig(level=logging.WARN)
logging.getLogger("my_app").setLevel(logging.DEBUG)
# no config needed for each library, unless you want to explicitly
# enable debug/info for that library


if __name__ == '__main__':
    vl = verboselib.Noisy()
    # note, use our log, not the class methods.
    log.info("This will be output, because we set global to DEBUG.")
    log.info("But not the verbose lib calls below at debug and info")
    vl.do_debug()
    vl.do_info()
    log.warn("Watch out! about to log from noisy!")
    vl.do_warn() 
