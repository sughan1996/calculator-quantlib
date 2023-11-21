from CalculatorApp.app import *
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


if __name__ == '__main__':
    event = {'a': 5, 'b': 7}
    logger.info(lambda_handler_add(event))
    logger.info(lambda_handler_subtract(event))
    logger.info(lambda_handler_multiply(event))




