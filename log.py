import logging


def setup_custom_logger(name):
    FORMAT = '%(asctime)s.%(msecs)03d, FILE=%(filename)s, FUNC=%(funcName)s(), LINENO=%(lineno)s, LEVEL=%(levelname)s, MESSAGE="%(message)s"'

    formatter = logging.Formatter(fmt=FORMAT)

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger
