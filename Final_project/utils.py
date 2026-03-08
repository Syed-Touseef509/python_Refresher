import os
import logging
from functools import wraps

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

# Setup logging
logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Decorator to log function calls
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Finished {func.__name__}")
        return result
    return wrapper

# Custom exception for invalid records
class InvalidRecordError(Exception):
    pass