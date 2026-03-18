from src.sql_solution import run_sql_solution
from properties.main_properties import sql_output_path

print("INFO: Executing SQL solution...")

sql_result = run_sql_solution()

if not sql_result.empty:
    print("INFO: SQL result produced successfully")
    print("INFO: Exporting SQL solution...")
    try:
        sql_result.to_csv(sql_output_path, sep=";")
        print("INFO: SQL solution exported successfully.")
    except Exception as e:
        print(f"ERROR: SQL solution export failed: {e}")
else:
    print("INFO: SQL solution produced not output.")

