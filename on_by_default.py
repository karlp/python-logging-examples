""" uses logging with an explicit configuration"""

import verboselib
import logging

# This is one way, where you turn off things you don't want to see
# and everything is on by default
logging.basicConfig(level=logging.DEBUG)
logging.getLogger("verboselib").setLevel(logging.WARN)
# ... more lines for each library you want to squelch, not very pretty


if __name__ == '__main__':
    vl = verboselib.Noisy()
    logging.info("This will be output, because we set global to DEBUG.")
    logging.info("But not the verbose lib calls below at debug and info")
    vl.do_debug()
    vl.do_info()
    logging.warn("Watch out! about to log from noisy!")
    vl.do_warn() 
