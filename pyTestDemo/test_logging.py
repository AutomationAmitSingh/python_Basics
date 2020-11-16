import logging


def test_logging_demo():
    logger = logging.getLogger(__name__)

    file_handler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)  # file handler object

    logger.setLevel(logging.CRITICAL)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.debug("A debug statement is executed")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happend")
    logger.critical("Critical issue")



