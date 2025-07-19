# etl_pipeline/utils/log_config.py

from loguru import logger
import sys

# Remove default logger to avoid duplicate logs during testing
logger.remove()

# Add a new logger with a custom format
logger.add(
    sys.stdout,
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
           "<level>{message}</level>"
)

# Optional: Reduce log noise from external libraries during test
# logger.level("urllib3", no=30, icon="🔇")  # Uncomment if needed
