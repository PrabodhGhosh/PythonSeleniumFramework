import inspect
import logging

import pytest


@pytest.mark.usefixtures("setUp")
class BaseClass:
    def getLogger(self):
        # Set the name to pick the test case name
        loggerName = inspect.stack()[1][3]
        # Format of print
        formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
        # File to create the logs
        FileHandler = logging.FileHandler("logs/logfile.log")
        # Connect Filehandler and Format
        FileHandler.setFormatter(formatter)
        # Logger object; which takes the test case
        logger = logging.getLogger(loggerName)
        # Pass the file name to logger object
        logger.addHandler(FileHandler)
        # Set Level
        logger.setLevel(logging.INFO)

        return logger
