from data_engine import DataEngine
from data_profiler import DataProfiler
from statistical_analyzer import StatisticalAnalyzer
from correlation_analyzer import CorrelationAnalyzer
from insight_engine import InsightEngine


DATA_FILE = "data/employees.csv"


# Load dataset
engine = DataEngine(DATA_FILE)

df = engine.get_data()


# Data profiling
profiler = DataProfiler(df)

profile_result = profiler.profile()


# Statistical analysis
statistics = StatisticalAnalyzer(df)

statistics_result = statistics.analyze()


# Correlation analysis
correlation = CorrelationAnalyzer(df)

relationships = (
    correlation.strongest_relationships()
)


# Insight engine
insight_engine = InsightEngine(
    profile_result,
    statistics_result,
    relationships
)


insights = (
    insight_engine.generate_insights()
)


print("\n========== AI DATA INSIGHTS ==========\n")


for number, insight in enumerate(
    insights,
    start=1
):

    print(
        f"{number}. {insight}"
    )