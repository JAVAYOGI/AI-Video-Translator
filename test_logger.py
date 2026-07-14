import os
import sys

print("Python:", sys.executable)
print("Current Folder:", os.getcwd())
print("File Running:", __file__)

from utils.logger import get_logger

logger = get_logger()

print("Before Logger")

logger.info("Application Started")
logger.warning("This is a warning")
logger.error("This is an error")
logger.critical("Critical Error")

print("After Logger")