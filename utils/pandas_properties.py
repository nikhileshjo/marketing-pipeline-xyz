import pandas as pd
import sqlite3
from utils.conn import db_path


tables_df = dict()
table_names = ['Sales', 'Customer', 'Orders', 'Items']

def load_table(table_name):
    print(f"INFO: Importing table: {table_name}")
    query = f"SELECT * FROM {table_name};"
    with sqlite3.connect(db_path) as conn:
        try:
            df = pd.read_sql_query(query, conn)
        except Exception as e:
            print(f"ERROR: SQL solution failed: {e}")
            return None

    return df

for table_name in table_names:
    
    tmp_df = load_table(table_name)
    if tmp_df is not None:
        tables_df[table_name] = tmp_df
    else:
        print(f"ERROR: Failed to load table: {table_name}")
        exit(1)

print("INFO: All tables imported.")
