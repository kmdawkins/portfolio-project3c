import pandas as pd

from etl_pipeline.utils.validation import validate_columns_exist




def test_validate_pmo_columns():
    """
    Test to ensure all expected columns exist in the PMO CSV
    """
    csv_path = "include/raw/pmo.csv"
    df = pd.read_csv(csv_path)


    expected_columns = [
        "payment_no", "transaction_date", "campaign_id", "description",
        "contract_no", "purchase_order", "purchase_requisition",
        "project_no", "payment_entity", "amount_usd", "amount_cny"
    ]
    

    assert validate_columns_exist(df, expected_columns)