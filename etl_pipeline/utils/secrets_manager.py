import json
import boto3
from botocore.exceptions import ClientError, NoCredentialsError
from loguru import logger
from functools import lru_cache  # Optional, for caching in session


class SecretsManagerError(Exception):
    """Custom exception for AWS Secrets Manager errors."""
    pass


# Optional: Uncomment to cache repeated secret fetches in-session
# @lru_cache(maxsize=None)
def get_secret(secret_name: str, region_name: str = "us-west-2") -> dict:
    """
    Retrieve a secret from AWS Secrets Manager and return it as a parsed JSON dictionary.

    Args:
        secret_name (str): Name or ARN of the AWS secret (e.g., 'project3c/secrets/snowflake').
        region_name (str): AWS region where the secret is stored. Defaults to "us-west-2".

    Returns:
        dict: Parsed JSON content of the secret.

    Raises:
        SecretsManagerError: On retrieval, credential, or parsing failure.

    Usage:
        >>> from etl_pipeline.utils.secrets_manager import get_secret
        >>> creds = get_secret("project3c/secrets/snowflake")
        >>> print(creds["user"])
    """
    session = boto3.session.Session()
    client = session.client(
        service_name="secretsmanager",
        region_name=region_name
    )

    try:
        logger.info(f"Retrieving secret from AWS Secrets Manager: {secret_name}")
        response = client.get_secret_value(SecretId=secret_name)

        secret_string = response.get("SecretString")
        if not secret_string:
            raise SecretsManagerError("SecretString is empty or missing.")

        parsed_secret = json.loads(secret_string)
        logger.success(f"✅ Successfully retrieved secret: {secret_name}")
        return parsed_secret

    except client.exceptions.ResourceNotFoundException:
        logger.error(f"❌ Secret not found: {secret_name}")
        raise SecretsManagerError(f"Secret not found: {secret_name}")

    except NoCredentialsError:
        logger.error("❌ AWS credentials not found. Is your profile configured?")
        raise SecretsManagerError("AWS credentials are missing.")

    except ClientError as e:
        logger.error(f"❌ ClientError: {e.response['Error']['Message']}")
        raise SecretsManagerError(f"Failed to retrieve secret: {secret_name}") from e

    except Exception as e:
        logger.error(f"❌ Unhandled exception while retrieving secret: {str(e)}")
        raise SecretsManagerError("Unexpected error occurred") from e
