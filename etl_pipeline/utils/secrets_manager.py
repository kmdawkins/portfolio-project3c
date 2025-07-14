import json
import boto3
from botocore.exceptions import ClientError
from loguru import logger


class SecretsManagerError(Exception):
    """Custom exception for AWS Secrets Manager errors."""
    pass


def get_secret(secret_name: str, region_name: str = "us-west-2") -> dict:
    """
    Retrieve and return a secret stored in AWS Secrets Manager.

    Args:
        secret_name (str): The name or ARN of the secret.
        region_name (str): AWS region (default: "us-west-2").

    Returns:
        dict: Parsed JSON content of the secret.

    Raises:
        SecretsManagerError: If retrieval fails.
    """
    session = boto3.session.Session()
    client = session.client(
        service_name="secretsmanager",
        region_name=region_name
    )

    try:
        logger.info(f"Retrieving secret: {secret_name}")
        response = client.get_secret_value(SecretId=secret_name)
        secret_string = response.get("SecretString")
        if not secret_string:
            raise SecretsManagerError("SecretString is empty or missing.")
        return json.loads(secret_string)
    
    except ClientError as e:
        logger.error(f"ClientError: {e.response['Error']['Message']}")
        raise SecretsManagerError(f"Failed to retrieve secret: {secret_name}") from e

    except Exception as e:
        logger.error(f"Unhandled exception: {str(e)}")
        raise SecretsManagerError("Unexpected error occurred") from e
