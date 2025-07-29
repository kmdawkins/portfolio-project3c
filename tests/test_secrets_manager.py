import pytest
import json
import os
from unittest.mock import patch, MagicMock
from botocore.exceptions import ClientError, NoCredentialsError

from etl_pipeline.utils.secrets_manager import get_secret
from etl_pipeline.utils.exceptions import SecretsManagerError


@patch("etl_pipeline.utils.secrets_manager.boto3.session.Session")
def test_get_secret_success(mock_session, caplog):
    mock_client = MagicMock()
    mock_client.get_secret_value.return_value = {
        "SecretString": json.dumps({"user": "demo", "password": "demo_pw"})
    }
    mock_session.return_value.client.return_value = mock_client

    with caplog.at_level("INFO"):
        result = get_secret("project3c/secrets/snowflake")

    assert result["user"] == "demo"
    assert result["password"] == "demo_pw"
    assert "Retrieving secret from AWS Secrets Manager" in caplog.text
    assert "Successfully retrieved" in caplog.text


@patch("etl_pipeline.utils.secrets_manager.boto3.session.Session")
def test_get_secret_empty_string_raises(mock_session, caplog):
    mock_client = MagicMock()
    mock_client.get_secret_value.return_value = {"SecretString": ""}
    mock_session.return_value.client.return_value = mock_client

    with caplog.at_level("ERROR"), pytest.raises(SecretsManagerError, match="SecretString is empty or missing"):
        get_secret("project3c/secrets/empty")

    assert "SecretString is empty or missing" in caplog.text


@patch("etl_pipeline.utils.secrets_manager.boto3.session.Session")
def test_get_secret_missing_key_raises(mock_session, caplog):
    mock_client = MagicMock()
    mock_client.get_secret_value.return_value = {}  # No SecretString key
    mock_session.return_value.client.return_value = mock_client

    with caplog.at_level("ERROR"), pytest.raises(SecretsManagerError):
        get_secret("project3c/secrets/missing")

    assert "SecretString is empty or missing" in caplog.text


@patch("etl_pipeline.utils.secrets_manager.boto3.session.Session")
def test_get_secret_client_error(mock_session, caplog):
    mock_client = MagicMock()
    mock_client.get_secret_value.side_effect = ClientError(
        {"Error": {"Message": "Secret not found"}}, "GetSecretValue"
    )
    mock_session.return_value.client.return_value = mock_client

    with caplog.at_level("ERROR"), pytest.raises(SecretsManagerError, match="Failed to retrieve secret"):
        get_secret("project3c/secrets/invalid")

    assert "ClientError" in caplog.text


@patch("etl_pipeline.utils.secrets_manager.boto3.session.Session")
def test_get_secret_no_credentials(mock_session, caplog):
    mock_client = MagicMock()
    mock_client.get_secret_value.side_effect = NoCredentialsError()
    mock_session.return_value.client.return_value = mock_client

    with caplog.at_level("ERROR"), pytest.raises(SecretsManagerError, match="AWS credentials are missing"):
        get_secret("project3c/secrets/nocreds")

    assert "AWS credentials not found" in caplog.text


@patch("etl_pipeline.utils.secrets_manager.boto3.session.Session")
def test_get_secret_invalid_json(mock_session, caplog):
    mock_client = MagicMock()
    mock_client.get_secret_value.return_value = {"SecretString": "not valid json"}
    mock_session.return_value.client.return_value = mock_client

    with caplog.at_level("ERROR"), pytest.raises(SecretsManagerError, match="Secret is not valid JSON"):
        get_secret("project3c/secrets/invalidjson")

    assert "Failed to parse secret JSON" in caplog.text


@patch("etl_pipeline.utils.secrets_manager.boto3.session.Session")
def test_get_secret_unexpected_exception(mock_session, caplog):
    mock_client = MagicMock()
    mock_client.get_secret_value.side_effect = Exception("Something went wrong")
    mock_session.return_value.client.return_value = mock_client

    with caplog.at_level("ERROR"), pytest.raises(SecretsManagerError, match="Unexpected error occurred"):
        get_secret("project3c/secrets/broken")

    assert "Unhandled exception while retrieving secret" in caplog.text


@patch("boto3.session.Session.client")
def test_get_secret_uses_aws_profile(mock_boto_client):
    """Test that AWS_PROFILE is respected and used in boto3 session."""
    test_profile = "test-profile"
    test_secret_name = "fake/secret"
    expected_secret = {"user": "demo"}

    with patch.dict(os.environ, {"AWS_PROFILE": test_profile}):
        mock_client_instance = mock_boto_client.return_value
        mock_client_instance.get_secret_value.return_value = {
            "SecretString": json.dumps(expected_secret)
        }

        result = get_secret(test_secret_name)

        assert result == expected_secret
        mock_boto_client.assert_called_once()
