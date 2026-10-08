from data_engine import DataEngine
from correlation_analyzer import CorrelationAnalyzer


DATA_FILE = "data/employees.csv"


engine = DataEngine(DATA_FILE)

df = engine.get_data()

analyzer = CorrelationAnalyzer(df)


print("\n========== CORRELATION MATRIX ==========\n")

matrix = analyzer.analyze()

print(matrix)


print("\n========== STRONGEST RELATIONSHIPS ==========\n")

relationships = analyzer.strongest_relationships()

for relationship in relationships:

    print(
        relationship["column_1"],
        "<->",
        relationship["column_2"],
        ":",
        round(
            relationship["correlation"],
            3
        )
    )