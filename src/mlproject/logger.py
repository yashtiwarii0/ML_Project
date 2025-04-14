import logging
import os
from datetime import datetime

# Create a "logs" directory path
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Define the log file name with timestamp
log_filename = f"{datetime.now().strftime('%m-%d-%Y-%H-%M-%S')}.log"
log_file_path = os.path.join(log_dir, log_filename)

# Setup logging
logging.basicConfig(
    filename=log_file_path,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filemode='w'
)
