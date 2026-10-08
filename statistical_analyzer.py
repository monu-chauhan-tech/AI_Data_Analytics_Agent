import pandas as pd


class StatisticalAnalyzer:

    def __init__(self, dataframe):
        self.df = dataframe

    def analyze(self):

        numeric_df = self.df.select_dtypes(
            include="number"
        )

        if numeric_df.empty:
            return {}

        statistics = {}

        for column in numeric_df.columns:

            series = numeric_df[column]

            statistics[column] = {
                "count": int(series.count()),
                "mean": float(series.mean()),
                "median": float(series.median()),
                "std": float(series.std()),
                "variance": float(series.var()),
                "min": float(series.min()),
                "max": float(series.max()),
                "q1": float(series.quantile(0.25)),
                "q3": float(series.quantile(0.75))
            }

        return statistics