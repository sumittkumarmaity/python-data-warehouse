import logging

# Configure logging to write to etl_execution.log with INFO level and specific format
logging.basicConfig(
    filename="logs/etl_execution.log",
    level=logging.INFO,
    format="%(asctime)s || %(levelname)s || %(message)s"
)

logger = logging.getLogger()

