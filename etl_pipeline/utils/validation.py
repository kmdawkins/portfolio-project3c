from typing import List
import pandas as pd
from loguru import logger


def validate_columns_exist(df: pd.DataFrame, expected_columns: List[str]) -> bool:
    """
    Ensure all expected columns exist in the DataFrame.
    """
    missing = [col for col in expected_columns if col not in df.columns]
    if missing:
        logger.error(f"Missing columns: {missing}")
        return False
    logger.info("All expected columns are present.")
    return True


def validate_non_null(df: pd.DataFrame, critical_columns: List[str]) -> bool:
    """
    Confirm critical columns have no null values.
    """
    null_counts = df[critical_columns].isnull().sum()
    nulls = null_counts[null_counts > 0]
    if not nulls.empty:
        logger.warning(f"Nulls detected in critical columns:\n{nulls}")
        return False
    logger.info("No nulls detected in critical columns.")
    return True


def validate_unique_key(df: pd.DataFrame, key_columns: List[str]) -> bool:
    """
    Validate that key columns form a unique identifier.
    """
    duplicates = df.duplicated(subset=key_columns)
    if duplicates.any():
        logger.error(f"Duplicate records found based on key columns: {key_columns}")
        return False
    logger.info(f"Key columns {key_columns} form a unique identifier.")
    return True