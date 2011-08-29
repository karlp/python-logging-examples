""" uses logging instead of prints, but no explicit logging config"""

import verboselib
import logging


if __name__ == '__main__':
    vl = verboselib.Noisy()
    logging.info("This, and the logging from Noisy, will not be output.")
    logging.info("because the default level is warn")
    vl.do_debug()
    vl.do_info()
    logging.warn("Watch out! about to log from noisy!")
    vl.do_warn() 
