import os
import subprocess
import logging
import pytest
from unittest.mock import patch, MagicMock
from loguru import logger

import etl_pipeline.utils.launch_psql as launch_psql

# ✅ Bridge Loguru logs into caplog so pytest captures them
class InterceptHandler(logging.Handler):
    def emit(self, record):
        logging.getLogger(record.name).handle(record)

logger.remove()
logger.add(InterceptHandler(), format="{message}")

@patch("etl_pipeline.utils.launch_psql.get_secret")
@patch("etl_pipeline.utils.launch_psql.subprocess.run")
def test_launch_psql_runs_expected_command(mock_run, mock_get_secret, caplog):
    mock_get_secret.return_value = {
        "POSTGRES_USER": "test_user",
        "POSTGRES_PASSWORD": "test_pass",
        "POSTGRES_HOST": "localhost",
        "POSTGRES_PORT": "5432",
        "POSTGRES_DB": "test_db"
    }

    with caplog.at_level("INFO"):
        launch_psql.launch_psql("mock/secret")

    # ✅ Assert subprocess was called with expected command
    mock_run.assert_called_once()
    cmd_run = mock_run.call_args[0][0]      # positional arg
    env_used = mock_run.call_args[1]["env"] # keyword arg

    assert cmd_run[0] == "psql"
    assert "--host=localhost" in cmd_run
    assert "--port=5432" in cmd_run
    assert "--username=test_user" in cmd_run
    assert "--dbname=test_db" in cmd_run
    assert env_used["PGPASSWORD"] == "test_pass"

    # ✅ Assert log visibility
    assert "Retrieving PostgreSQL credentials" in caplog.text
    assert "Launching psql CLI session" in caplog.text


@patch("etl_pipeline.utils.launch_psql.get_secret")
@patch("etl_pipeline.utils.launch_psql.subprocess.run", side_effect=subprocess.CalledProcessError(1, "psql"))
def test_launch_psql_logs_failure(mock_run, mock_get_secret, caplog):
    mock_get_secret.return_value = {
        "POSTGRES_USER": "u",
        "POSTGRES_PASSWORD": "p",
        "POSTGRES_HOST": "h",
        "POSTGRES_DB": "d"
    }

    with caplog.at_level("ERROR"):
        launch_psql.launch_psql("mock/secret")

    # ✅ Assert error log captured
    assert "psql command failed" in caplog.text
