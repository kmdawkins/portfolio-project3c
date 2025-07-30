import json
import boto3
from botocore.exceptions import ClientError, NoCredentialsError, BotoCoreError
from loguru import logger
import os


class SecretsManagerError(Exception):
    """Custom exception for AWS Secrets Manager errors."""
    pass


def get_secret(secret_name: str, region_name: str = "us-west-2") -> dict:
    """
    Retrieve a secret from AWS Secrets Manager using optional AWS profile.
    
    Args:
        secret_name (str): AWS Secrets Manager secret name.
        region_name (str): AWS region. Defaults to 'us-west-2'.
    
    Returns:
        dict: Parsed JSON secret.
    
    Raises:
        SecretsManagerError: If retrieval or parsing fails.
    """
    profile = os.getenv("AWS_PROFILE")

    # Initialize session
    try:
        if profile:
            logger.info(f"Using AWS profile: {profile}")
            session = boto3.Session(profile_name=profile, region_name=region_name)
        else:
            session = boto3.Session(region_name=region_name)

        client = session.client("secretsmanager")
    except (BotoCoreError, Exception) as e:
        logger.error(f"❌ Failed to initialize Secrets Manager client: {str(e)}")
        raise SecretsManagerError("Failed to initialize Secrets Manager client") from e

    # Call get_secret_value
    try:
        logger.info(f"Retrieving secret from AWS Secrets Manager: {secret_name}")
        response = client.get_secret_value(SecretId=secret_name)
    except NoCredentialsError:
        logger.error("❌ AWS credentials not found. Is your profile configured?")
        raise SecretsManagerError("AWS credentials are missing.")
    except ClientError as e:
        logger.error(f"❌ ClientError: {e.response['Error']['Message']}")
        raise SecretsManagerError(f"Failed to retrieve secret: {secret_name}") from e
    except Exception as e:
        logger.error(f"❌ Unhandled exception while retrieving secret: {str(e)}")
        raise SecretsManagerError("Unexpected error occurred") from e

    # Validate presence of SecretString
    secret_string = response.get("SecretString")
    if not secret_string:
        logger.error("❌ SecretString is empty or missing.")
        raise SecretsManagerError("SecretString is empty or missing")

    # Validate it’s proper JSON
    try:
        parsed_secret = json.loads(secret_string)
    except json.JSONDecodeError:
        logger.error("❌ Secret is not valid JSON.")
        raise
