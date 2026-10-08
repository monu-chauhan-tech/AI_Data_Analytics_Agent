from data_engine import DataEngine
from data_profiler import DataProfiler


DATA_FILE = "data/employees.csv"


engine = DataEngine(DATA_FILE)

df = engine.get_data()

profiler = DataProfiler(df)

result = profiler.profile()


print("\n========== DATA PROFILE ==========\n")

print("Rows:", result["rows"])

print("Columns:", result["columns"])

print(
    "Column Names:",
    result["column_names"]
)

print(
    "Data Types:",
    result["data_types"]
)

print(
    "Numeric Columns:",
    result["numeric_columns"]
)

print(
    "Categorical Columns:",
    result["categorical_columns"]
)

print(
    "Missing Values:",
    result["missing_values"]
)

print(
    "Total Missing Values:",
    result["total_missing_values"]
)

print(
    "Duplicate Rows:",
    result["duplicates"]
)