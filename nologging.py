
import verboselib

if __name__ == '__main__':
    vl = verboselib.Noisy()
    print "no logging configured, so no output at all here"
    vl.do_debug()
    vl.do_info()
    print "warning here, because no loggers configured"
    vl.do_warn()
