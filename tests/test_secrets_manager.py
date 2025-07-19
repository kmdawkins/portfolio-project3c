import boto3
import json
from botocore.exceptions import ClientError, NoCredentialsError
from etl_pipeline.utils.log_config import logger
from etl_pipeline.utils.exceptions import SecretsManagerError


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
        logger.info(f"Successfully retrieved secret: {secret_name}")
        return parsed_secret

    except NoCredentialsError as e:
        logger.error("No AWS credentials found.")
        raise SecretsManagerError("Missing AWS credentials.") from e

    except ClientError as e:
        logger.error(f"Client error retrieving secret: {e}")
        raise SecretsManagerError(f"Failed to retrieve secret: {e}") from e

    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse secret JSON: {e}")
        raise SecretsManagerError("Secret is not valid JSON.") from e

    except Exception as e:
        logger.error(f"Unexpected error retrieving secret: {e}")
        raise SecretsManagerError("Unexpected error occurred.") from e
