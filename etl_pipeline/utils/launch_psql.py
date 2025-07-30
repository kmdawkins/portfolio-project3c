import os
import subprocess
from loguru import logger
from etl_pipeline.utils.secrets_manager import get_secret, SecretsManagerError


def launch_psql(secret_name: str, region: str = "us-west-2") -> None:
    try:
        logger.info("Retrieving PostgreSQL credentials from AWS Secrets Manager...")
        creds = get_secret(secret_name, region)

        if not creds:
            logger.error("❌ Retrieved secret is empty or None.")
            raise SecretsManagerError("Retrieved secret is empty or None.")

        required_keys = ["POSTGRES_USER", "POSTGRES_PASSWORD", "POSTGRES_HOST", "POSTGRES_DB"]
        missing_keys = [key for key in required_keys if key not in creds]

        if missing_keys:
            logger.error(f"❌ Missing required keys in secret: {missing_keys}")
            raise SecretsManagerError(f"Missing required keys: {', '.join(missing_keys)}")

        db_user = creds["POSTGRES_USER"]
        db_pass = creds["POSTGRES_PASSWORD"]
        db_host = creds["POSTGRES_HOST"]
        db_port = creds.get("POSTGRES_PORT", "5432")
        db_name = creds["POSTGRES_DB"]

        logger.info("Launching psql CLI session...")
        env = os.environ.copy()
        env["PGPASSWORD"] = db_pass  # Prevents password from being exposed in process list

        cmd = [
            "psql",
            f"--host={db_host}",
            f"--port={db_port}",
            f"--username={db_user}",
            f"--dbname={db_name}"
        ]

        subprocess.run(cmd, env=env, check=True)

    except SecretsManagerError as e:
        logger.error(f"❌ Secrets retrieval failed: {e}")
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ psql command failed: {e}")
    except Exception as e:
        logger.exception(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    # ✅ Update this to match the correct AWS secret name
    launch_psql("project3c/secrets/postgres")
