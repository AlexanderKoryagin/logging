import logging.config
import os

import yaml


LOGGING_CFG_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'logging_cfg.yaml'
)


def setup_logging(
        cfg_path=LOGGING_CFG_FILE,
        log_level=None
):
    """Setup logging configuration."""
    if os.path.exists(cfg_path):
        with open(cfg_path, 'rt') as cfg_file:
            config = yaml.safe_load(cfg_file.read())

            if log_level == 'DEBUG':
                config['handlers']['console']['level'] = log_level
                config['handlers']['console']['formatter'] = log_level.lower()

        logging.config.dictConfig(config)
    else:
        raise IOError('No such file or directory: %s' % cfg_path)
