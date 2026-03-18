import sqlite3
import pandas as pd
from utils.conn import db_path
from utils.sql_properties import sql_query

def run_sql_solution(db_path= db_path, sql_query = sql_query):
    print("INFO: Connecting to database...")
    try:
        conn = sqlite3.connect(db_path)
        
        df = pd.read_sql_query(sql_query, conn)
        
        return df

    except Exception as e:
        print(f"ERROR: SQL solution failed: {e}")
        return None

    finally:
        conn.close()