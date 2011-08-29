""" 
Exactly the same as nologging
but, now you can set logging.raiseExceptions to False to hide the warning...
"""

import verboselib
import logging

logging.raiseExceptions = False

if __name__ == '__main__':
    vl = verboselib.Noisy()
    print "no logging configured, so no output at all here"
    vl.do_debug()
    vl.do_info()
    print """there will be no output from here either, because we 
told logging to swallow the configuration error"""
    vl.do_warn()
