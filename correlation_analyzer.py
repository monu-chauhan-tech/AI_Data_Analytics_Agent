import pandas as pd


class CorrelationAnalyzer:

    def __init__(self, dataframe):
        self.df = dataframe

    def analyze(self):

        numeric_df = self.df.select_dtypes(
            include="number"
        )

        if numeric_df.empty:
            return {}

        correlation_matrix = numeric_df.corr()

        return correlation_matrix

    def strongest_relationships(self):

        numeric_df = self.df.select_dtypes(
            include="number"
        )

        if len(numeric_df.columns) < 2:
            return []

        correlation_matrix = numeric_df.corr()

        relationships = []

        columns = correlation_matrix.columns

        for i in range(len(columns)):
            for j in range(i + 1, len(columns)):

                column1 = columns[i]
                column2 = columns[j]

                correlation = correlation_matrix.loc[
                    column1,
                    column2
                ]

                relationships.append({
                    "column_1": column1,
                    "column_2": column2,
                    "correlation": float(correlation)
                })

        relationships.sort(
            key=lambda x: abs(x["correlation"]),
            reverse=True
        )

        return relationships