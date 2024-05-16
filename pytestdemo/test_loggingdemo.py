import logging


def test_loggingdemo():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.INFO)
    logger.debug("A debug statement executed")
    logger.info("Information statement")
    logger.warning("Something is in warninig mode")
    logger.error("A major error has happened")
    logger.critical("Crittical situation")
