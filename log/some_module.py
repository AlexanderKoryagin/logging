import logging

LOGGER = logging.getLogger(__name__)


class DoSomething(object):

    def __init__(self):
        """Some empty class to check logger."""
        LOGGER.debug('Debug info')
        LOGGER.info('Info info')
        LOGGER.warn('Warning info')
        LOGGER.error('Error info')
        LOGGER.critical('Critical info')
