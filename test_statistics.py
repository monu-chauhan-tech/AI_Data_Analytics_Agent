from data_engine import DataEngine
from statistical_analyzer import StatisticalAnalyzer


DATA_FILE = "data/employees.csv"


engine = DataEngine(DATA_FILE)

df = engine.get_data()

analyzer = StatisticalAnalyzer(df)

result = analyzer.analyze()


print("\n========== STATISTICAL ANALYSIS ==========\n")


for column, stats in result.items():

    print(f"\n--- {column} ---")

    print("Count:", stats["count"])
    print("Mean:", round(stats["mean"], 2))
    print("Median:", stats["median"])
    print("Standard Deviation:", round(stats["std"], 2))
    print("Variance:", round(stats["variance"], 2))
    print("Minimum:", stats["min"])
    print("Maximum:", stats["max"])
    print("Q1:", stats["q1"])
    print("Q3:", stats["q3"])