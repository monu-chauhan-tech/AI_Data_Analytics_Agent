import pandas as pd


class DataProfiler:

    def __init__(self, dataframe):
        self.df = dataframe

    def profile(self):

        numeric_columns = list(
            self.df.select_dtypes(
                include="number"
            ).columns
        )

        categorical_columns = list(
            self.df.select_dtypes(
                exclude="number"
            ).columns
        )

        missing_values = (
            self.df.isnull()
            .sum()
            .to_dict()
        )

        duplicates = int(
            self.df.duplicated().sum()
        )

        return {
            "rows": int(len(self.df)),

            "columns": int(
                len(self.df.columns)
            ),

            "column_names": list(
                self.df.columns
            ),

            "data_types": {
                column: str(dtype)
                for column, dtype
                in self.df.dtypes.items()
            },

            "numeric_columns":
                numeric_columns,

            "categorical_columns":
                categorical_columns,

            "missing_values":
                missing_values,

            "total_missing_values":
                int(
                    self.df.isnull()
                    .sum()
                    .sum()
                ),

            "duplicates":
                duplicates
        }