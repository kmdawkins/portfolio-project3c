import os
import subprocess
from loguru import logger
from etl_pipeline.utils.secrets_manager import get_secret, SecretsManagerError


def launch_psql(secret_name: str, region: str = "us-west-2") -> None:
    try:
        logger.info("Retrieving PostgreSQL credentials from AWS Secrets Manager...")
        creds = get_secret(secret_name, region)

        db_user = creds["POSTGRES_USER"]
        db_pass = creds["POSTGRES_PASSWORD"]
        db_host = creds["POSTGRES_HOST"]
        db_port = creds.get("POSTGRES_PORT", "5432")
        db_name = creds["POSTGRES_DB"]

        logger.info("Launching psql CLI session...")
        env = os.environ.copy()
        env["PGPASSWORD"] = db_pass  # Avoid exposing password in command args

        cmd = [
            "psql",
            f"--host={db_host}",
            f"--port={db_port}",
            f"--username={db_user}",
            f"--dbname={db_name}"
        ]

        subprocess.run(cmd, env=env, check=True)

    except KeyError as e:
        logger.error(f"Missing expected key in secret: {e}")
    except SecretsManagerError as e:
        logger.error(f"Secrets retrieval failed: {e}")
    except subprocess.CalledProcessError as e:
        logger.error(f"psql command failed: {e}")


if __name__ == "__main__":
    # Example usage: update to match your secret name
    launch_psql("project3c/secrets/postgresql")
