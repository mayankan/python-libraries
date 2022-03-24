"""
    @Author: Mayank Anand
    @Date: 2022-03-22
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-22
    @Title : numPy Programs - Logger Function to create log file
    """
import logging


def logging_init(name):
    """
    Description:
        Logs Output for called instance function to two log files and console stream.
    Parameter:
        name: Given Name of the file from where this function is called.
    Return:
        logger which holds the value of logging function when called, creates wo log files and console stream.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

    info_handler = logging.FileHandler('info.log')
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)

    error_handler = logging.FileHandler('error.log')
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(info_handler)
    logger.addHandler(error_handler)
    logger.addHandler(stream_handler)
    return logger
