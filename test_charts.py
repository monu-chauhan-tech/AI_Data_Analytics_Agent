from data_engine import DataEngine
from chart_generator import ChartGenerator


DATA_FILE = "data/employees.csv"


engine = DataEngine(DATA_FILE)

df = engine.get_data()

generator = ChartGenerator(df)

charts = generator.generate_all()


print("\n========== GENERATED CHARTS ==========\n")

for chart in charts:
    print(chart)