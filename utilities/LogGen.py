import os
import sys
import logging

logger = ""


def cleanupLogFileName(logFileName):
    if '/' in logFileName:
        cleanedUpLogFileSplit = logFileName.split("/")
        cleanedUpLogFileName = cleanedUpLogFileSplit[-1]
    elif "\\" in logFileName:
        cleanedUpLogFileSplit = logFileName.split("\\")
        cleanedUpLogFileName = cleanedUpLogFileSplit[-1]
    else:
        cleanedUpLogFileName = logFileName

    return cleanedUpLogFileName


def create_log_file_handler(logFileName, logLevel=logging.NOTSET, logName=""):
    logging.basicConfig(level=logLevel)
    if logName == "":
        logger = logging.getLogger(__name__)
    else:
        logger = logging.getLogger(logName)
    logger.propagate = False

    silentremove(logFileName)

    # create a file handler and set level to info
    handler = logging.FileHandler(logFileName)

    # create file formatter
    formatter = logging.Formatter('%(asctime)s.%(msecs)03d: - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # add formatter to ch
    handler.setFormatter(formatter)

    # create console handler and set level to info
    ch = logging.StreamHandler(sys.stdout)

    # create console formatter
    chFormatter = logging.Formatter('%(asctime)s.%(msecs)03d: - %(levelname)s - %(message)s ', datefmt='%Y-%m-%d %H:%M:%S')

    # add formatter to ch
    ch.setFormatter(chFormatter)

    # add the handlers to the logger
    logger.addHandler(handler)
    logger.addHandler(ch)

    return logger


def silentremove(filename):
    try:
        os.remove(filename)
    except OSError:
        print("Could not delete file: ", filename)