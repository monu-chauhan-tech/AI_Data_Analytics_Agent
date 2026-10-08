import os
import matplotlib.pyplot as plt


class ChartGenerator:

    def __init__(self, dataframe):
        self.df = dataframe

        self.output_folder = "static/charts"

        os.makedirs(
            self.output_folder,
            exist_ok=True
        )

    def generate_all(self):

        charts = []

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

        # Numeric distributions
        for column in numeric_columns:

            filename = (
                column.lower()
                .replace(" ", "_")
                + "_distribution.png"
            )

            filepath = os.path.join(
                self.output_folder,
                filename
            )

            plt.figure()

            plt.hist(
                self.df[column].dropna(),
                bins=10
            )

            plt.title(
                f"{column} Distribution"
            )

            plt.xlabel(column)
            plt.ylabel("Frequency")

            plt.tight_layout()

            plt.savefig(filepath)

            plt.close()

            charts.append(filepath)

        # Categorical counts
        for column in categorical_columns:

            if self.df[column].nunique() > 20:
                continue

            filename = (
                column.lower()
                .replace(" ", "_")
                + "_count.png"
            )

            filepath = os.path.join(
                self.output_folder,
                filename
            )

            counts = (
                self.df[column]
                .value_counts()
            )

            plt.figure()

            counts.plot(
                kind="bar"
            )

            plt.title(
                f"{column} Count"
            )

            plt.xlabel(column)
            plt.ylabel("Count")

            plt.xticks(
                rotation=45
            )

            plt.tight_layout()

            plt.savefig(filepath)

            plt.close()

            charts.append(filepath)

        return charts