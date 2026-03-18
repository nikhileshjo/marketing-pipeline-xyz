from src.sql_solution import run_sql_solution
from utils.main_properties import sql_output_path, pd_output_path
from src.pandas_solution import run_data_pandas


# Processing SQL solution
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


# Processing pandas solution
print("INFO: Executing pandas solution...")

pd_result = run_data_pandas()

if not pd_result.empty:
    print("INFO: Pandas result produced successfully")
    print("INFO: Exporting pandas solution...")
    try:
        pd_result.to_csv(pd_output_path, sep=";")
        print("INFO: Pandas solution exported successfully.")
    except Exception as e:
        print(f"ERROR: Pandas solution export failed: {e}")
else:
    print("INFO: Pandas solution produced not output.")

print("INFO: Comparing outputs of SQL and Pandas solutions...")

# Strict comparision of dataframes
compare_result = pd_result.equals(sql_result)

if compare_result:
    print("INFO: Both outputs match.")
    print("INFO: Script sccessfully completed")
else:
    print("INFO: Output did not match.")
    print("INFO: Logic creation failed")

