
import logging

class Noisy(object):
    def __init__(self):
        self.log = logging.getLogger("verboselib.Noisy")

    def do_debug(self):
        self.log.debug("logged at debug")

    def do_info(self):
        self.log.info("logged at info")

    def do_warn(self):
        self.log.warn("logged at warn")
