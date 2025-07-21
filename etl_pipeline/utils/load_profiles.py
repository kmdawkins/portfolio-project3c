import os
import yaml
from dotenv import load_dotenv
from pathlib import Path
from etl_pipeline.utils.secrets_manager import get_secret

load_dotenv()

# Force block-style YAML indentation compatible with dbt
class IndentDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)

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

    # 🛑 Fail-safe: Check for missing values
    missing_keys = [k for k, v in secret_dict.items() if not v]
    if missing_keys:
        raise ValueError(
            f"❌ Missing required Snowflake credentials for: {', '.join(missing_keys)}.\n"
            f"Check your .env file or AWS Secrets Manager configuration."
        )

    # ✅ Use the correct profile name from dbt_project.yml
    profiles = {
        "project3c_profile": {
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
        yaml.dump(
            profiles,
            f,
            Dumper=IndentDumper,
            default_flow_style=False,
            sort_keys=False
        )

    print("✅ profiles.yml successfully rendered.")

if __name__ == "__main__":
    render_profiles()
