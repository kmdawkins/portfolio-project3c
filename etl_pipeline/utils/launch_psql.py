import os
import subprocess
from loguru import logger
from etl_pipeline.utils.secrets_manager import get_secret, SecretsManagerError
from dotenv import load_dotenv

load_dotenv()


def launch_psql(secret_name: str, region: str = "us-west-2") -> None:
    try:
        logger.info("🔐 Retrieving PostgreSQL credentials from AWS Secrets Manager...")
        creds = get_secret(secret_name, region)

        if not creds:
            raise SecretsManagerError("Retrieved secret is empty or None.")

        required_keys = ["POSTGRES_USER", "POSTGRES_PASSWORD", "POSTGRES_HOST", "POSTGRES_DB"]
        missing_keys = [key for key in required_keys if key not in creds]
        if missing_keys:
            raise SecretsManagerError(f"Missing required keys: {', '.join(missing_keys)}")

        db_user = creds["POSTGRES_USER"]
        db_pass = creds["POSTGRES_PASSWORD"]
        db_host = creds["POSTGRES_HOST"]
        db_port = creds.get("POSTGRES_PORT", "5432")
        db_name = creds["POSTGRES_DB"]

        # ✅ Optional: Masked banner confirmation
        masked_user = db_user[0] + "***"
        masked_host = db_host.split('.')[0] + "..."
        logger.info(f"✅ Connecting to PostgreSQL as '{masked_user}' on host '{masked_host}' (via Secrets Manager)")

        # ✅ Use env to pass password securely
        env = os.environ.copy()
        env["PGPASSWORD"] = db_pass

        cmd = [
            "psql",
            f"--host={db_host}",
            f"--port={db_port}",
            f"--username={db_user}",
            f"--dbname={db_name}"
        ]

        logger.info("🚀 Launching interactive psql CLI session...")
        subprocess.run(cmd, env=env, check=True)
        logger.success("✅ PostgreSQL session closed successfully.")

    except SecretsManagerError as e:
        logger.error(f"❌ Secrets retrieval failed: {e}")
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ psql exited with error: {e}")
    except FileNotFoundError:
        logger.error("❌ 'psql' not found. Ensure PostgreSQL CLI is installed and available in PATH.")
    except Exception as e:
        logger.exception(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    launch_psql("project3c/secrets/postgres")
