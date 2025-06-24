import pandas as pd
from etl_pipeline.utils.validation import validate_columns_exist

def test_validate_pmo_columns():
    csv_path = "include/raw/pmo.csv"
    df = pd.read_csv(csv_path)

    expected_columns = [
        "transaction_id", "agency_id", "project_id", "campaign_id",
        "cost_center_id", "market_id", "amount", "transaction_date"
    ]

    # This will log an error and assert False if validation fails
    assert validate_columns_exist(df, expected_columns)
