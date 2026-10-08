class InsightEngine:

    def __init__(
        self,
        profiler,
        statistics,
        relationships
    ):
        self.profiler = profiler
        self.statistics = statistics
        self.relationships = relationships

    def generate_insights(self):

        insights = []

        # -------------------------
        # DATASET SIZE
        # -------------------------

        rows = self.profiler.get("rows", 0)
        columns = self.profiler.get("columns", 0)

        insights.append(
            f"The dataset contains {rows} rows "
            f"and {columns} columns."
        )

        # -------------------------
        # MISSING VALUES
        # -------------------------

        total_missing = self.profiler.get(
            "total_missing_values",
            0
        )

        if total_missing == 0:

            insights.append(
                "No missing values were detected "
                "in the dataset."
            )

        else:

            insights.append(
                f"The dataset contains "
                f"{total_missing} missing values."
            )

        # -------------------------
        # DUPLICATES
        # -------------------------

        duplicates = self.profiler.get(
            "duplicates",
            0
        )

        if duplicates == 0:

            insights.append(
                "No duplicate rows were detected."
            )

        else:

            insights.append(
                f"The dataset contains "
                f"{duplicates} duplicate rows."
            )

        # -------------------------
        # NUMERIC INSIGHTS
        # -------------------------

        for column, stats in self.statistics.items():

            mean = stats["mean"]
            minimum = stats["min"]
            maximum = stats["max"]

            insights.append(
                f"{column}: average is "
                f"{mean:.2f}, minimum is "
                f"{minimum:.2f}, and maximum is "
                f"{maximum:.2f}."
            )

        # -------------------------
        # STRONG CORRELATIONS
        # -------------------------

        if self.relationships:

            strongest = self.relationships[0]

            column1 = strongest["column_1"]
            column2 = strongest["column_2"]
            correlation = strongest["correlation"]

            strength = abs(correlation)

            if strength >= 0.7:
                description = "strong"

            elif strength >= 0.4:
                description = "moderate"

            else:
                description = "weak"

            direction = (
                "positive"
                if correlation > 0
                else "negative"
            )

            insights.append(
                f"{column1} and {column2} have a "
                f"{description} {direction} correlation "
                f"of {correlation:.2f}."
            )

        return insights