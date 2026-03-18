from utils.conn import db_path
from utils.pandas_properties import tables_df

def run_data_pandas(db_path = db_path):

    # joining tables
    df = tables_df['Orders'].merge(tables_df['Sales'], on="sales_id", how="inner")
    df = df.merge(tables_df['Items'], on="item_id", how="inner")
    df = df.merge(tables_df['Customer'], on="customer_id", how="inner")

    # filtering
    df = df[(df["age"] >= 18) & (df["age"] <= 35)]
    df = df[df["quantity"].notna()]

    # Aggregation
    df = (
        df.groupby(["customer_id", "age", "item_name"], as_index=False)["quantity"]
        .sum()
    )
    # type casting
    df["quantity"] = df["quantity"].astype(int)
    # filtering on aggregation
    df = df[df["quantity"] > 0]

    # renaming for presentation
    df = df.rename(columns={
        "customer_id": "Customer",
        "age": "Age",
        "item_name": "Item",
        "quantity": "Quantity"
    })

    # sorting to keep outputs equal to SQL solution
    df = df.sort_values(by=["Customer", "Age", "Item", "Quantity"])

    return df