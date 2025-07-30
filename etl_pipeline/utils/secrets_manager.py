import json
import boto3
from botocore.exceptions import ClientError, NoCredentialsError, BotoCoreError
from loguru import logger
import os
import base64


class SecretsManagerError(Exception):
    """Custom exception for AWS Secrets Manager errors."""
    pass


def get_secret(secret_name: str, region_name: str = "us-west-2") -> dict:
    """
    Retrieve a secret from AWS Secrets Manager using environment-based credentials.

    Args:
        secret_name (str): AWS Secrets Manager secret name.
        region_name (str): AWS region. Defaults to 'us-west-2'.

    Returns:
        dict: Parsed JSON secret.

    Raises:
        SecretsManagerError: If retrieval or parsing fails.
    """
    try:
        # ✅ Load AWS credentials from .env via os.environ
        session = boto3.Session(
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=region_name
        )

        client = session.client("secretsmanager")
    except (BotoCoreError, Exception) as e:
        logger.error(f"❌ Failed to initialize Secrets Manager client: {str(e)}")
        raise SecretsManagerError("Failed to initialize Secrets Manager client") from e

    try:
        logger.info(f"Retrieving secret from AWS Secrets Manager: {secret_name}")
        response = client.get_secret_value(SecretId=secret_name)

        # TEMP: Print full response for debugging
        logger.info(f"✅ Secret {secret_name} retrieved successfully")
    except NoCredentialsError:
        logger.error("❌ AWS credentials not found in environment variables.")
        raise SecretsManagerError("AWS credentials are missing.")
    except ClientError as e:
        logger.error(f"❌ ClientError: {e.response['Error']['Message']}")
        raise SecretsManagerError(f"Failed to retrieve secret: {secret_name}") from e
    except Exception as e:
        logger.error(f"❌ Unhandled exception while retrieving secret: {str(e)}")
        raise SecretsManagerError("Unexpected error occurred") from e

    # Handle both SecretString and SecretBinary
    secret_string = response.get("SecretString")
    if not secret_string and "SecretBinary" in response:
        logger.warning("⚠️ SecretString missing, attempting to decode SecretBinary instead.")
        try:
            secret_string = base64.b64decode(response["SecretBinary"]).decode("utf-8")
        except Exception as e:
            logger.error(f"❌ Failed to decode SecretBinary: {str(e)}")
            raise SecretsManagerError("Failed to decode SecretBinary") from e

    if not secret_string:
        logger.error("❌ Retrieved secret is empty or None.")
        raise SecretsManagerError("Retrieved secret is empty or None.")

    try:
        return json.loads(secret_string)
    except json.JSONDecodeError:
        logger.error("❌ Secret is not valid JSON.")
        raise SecretsManagerError("Secret content is not valid JSON.")
