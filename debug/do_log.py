# import logging
# import sys

# logger = logging.getLogger('simple_logger')
# logger.setLevel(logging.DEBUG)

# handler = logging.StreamHandler(sys.stdout)
# handler.setLevel(logging.DEBUG)

# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)

# logger.addHandler(handler)

# if __name__ == '__main__':
#     logger.debug("debug message ...")
#     logger.info('info message ...')
#     logger.warning('warning message ...')
#     logger.error('error message ...')
#     logger.critical('critical message ...')

import logging.config
import yaml

with open('logging.yaml', 'r') as f_conf:
    dict_conf = yaml.load(f_conf, Loader=yaml.Loader)

logging.config.dictConfig(dict_conf)

logger = logging.getLogger('console_xample')
logger.debug("debug message ...")
logger.info('info message ...')
logger.warning('warning message ...')
logger.error('error message ...')
logger.critical('critical message ...')
