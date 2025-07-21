import os
import yaml
from etl_pipeline.utils.secrets_manager import get_secret
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

def render_profiles():
    use_aws = os.getenv("USE_AWS_SECRETS", "false").lower() == "true"
    
    if use_aws:
        print("🔐 Loading Snowflake credentials from AWS Secrets Manager...")
        secret_dict = get_secret("project3c/secrets/snowflake")
    else:
        print("📦 Loading Snowflake credentials from local .env file...")
        secret_dict = {
            "user": os.getenv("SNOWFLAKE_USER"),
            "password": os.getenv("SNOWFLAKE_PASSWORD"),
            "account": os.getenv("SNOWFLAKE_ACCOUNT"),
            "role": os.getenv("SNOWFLAKE_ROLE"),
            "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
            "database": os.getenv("SNOWFLAKE_DATABASE"),
            "schema": os.getenv("SNOWFLAKE_SCHEMA"),
        }

    profiles = {
        "default": {
            "outputs": {
                "dev": {
                    "type": "snowflake",
                    "account": secret_dict["account"],
                    "user": secret_dict["user"],
                    "password": secret_dict["password"],
                    "role": secret_dict["role"],
                    "warehouse": secret_dict["warehouse"],
                    "database": secret_dict["database"],
                    "schema": secret_dict["schema"],
                    "threads": 1,
                    "client_session_keep_alive": False
                }
            },
            "target": "dev"
        }
    }

    dbt_dir = Path.home() / ".dbt"
    dbt_dir.mkdir(exist_ok=True)

    with open(dbt_dir / "profiles.yml", "w") as f:
        yaml.dump(profiles, f, default_flow_style=False)

    print("✅ profiles.yml successfully rendered.")

if __name__ == "__main__":
    render_profiles()
