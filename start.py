import argparse
import logging

import log.logging_cfg
from log.some_module import DoSomething


LOGGER = logging.getLogger(__name__)


def get_args():
    """Read script arguments."""
    parser = argparse.ArgumentParser(
        description="Experiments with logging."
    )
    parser.add_argument(
        "--debug", '--D',
        action="store_true",
        default=False,
        help="console logger debug mode ON"
    )
    return parser.parse_args()


if __name__ == "__main__":

    ARGS = get_args()

    LOG_LEVEL = 'DEBUG' if ARGS.debug else None
    log.logging_cfg.setup_logging(
        log_level=LOG_LEVEL
    )

    for x in range(0, 5):
        LOGGER.debug('Info debug %s', x)
        LOGGER.info('Info numb %s', x)
        LOGGER.warn('Warning numb %s', x)
        LOGGER.error('Error numb %s', x)
        LOGGER.critical('Critical numb %s', x)

    SomeClass = DoSomething
    SomeClass()
