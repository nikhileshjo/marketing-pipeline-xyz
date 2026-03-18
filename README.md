# marketing-pipeline-xyz

# Overview
This project helps the marketing analyst understand their biggest product(s) in the market in certain age brackets.
Here, we're going to find the number of products each customer bought within the age range of 18 to 35 bought over a period of time.

NOTE: The received database was corrupted so I created my own, so I've not provided any output CSV files. I've provided the steps to follow to produce the necessary output files 

# Getting started
* Set up your environment using `python -m venv my_env`
* Activate your environment
    * Windows: `my_env\Scripts\activate`
    * Mac/Linux: `source my_env/bin/activate`
* Install necessary packages from the requirements.txt file with `pip install -r requirements.txt`
* Place your sqlite's .db file in the folder: `data`
* We're ready to run the script, execute: `python main.py`

The output files are produced inside the `output` folder.

# Developer's guide

## SQL solution
* The SQL solution location: `src/sql_solution.py`
* It takes the SQL from a utility module: `utils/sql_properties.py`
* You can simply modify the SQL statement in the file to modify the SQL logic inside `sql_properties.py`.
* This file doesn't run indepenently as there is a relative module reference in it, which keeps in mind that the all the scripts are run from the root.

## Pandas solution
* The pandas solution location: `src/pandas_solution.py`
* It imports all tables as dataframes from a utility module: `utils/pandas_properties.py`
* To add or remove table, you can change the list `table_names` in the `pandas_properties.py` file.
* Any kind of logical changes will require you to modify the file `pandas_solution.py`
* This file doesn't run indepenently as there is a relative module reference in it, which keeps in mind that the all the scripts are run from the root.