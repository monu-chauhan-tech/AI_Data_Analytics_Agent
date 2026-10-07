import pandas as pd
import os


class DataEngine:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)

    # -------------------------
    # GET DATA
    # -------------------------

    def get_data(self):
        return self.df

    # -------------------------
    # BASIC INFORMATION
    # -------------------------

    def get_info(self):

        return {
            "rows": len(self.df),
            "columns": len(self.df.columns),
            "column_names": list(self.df.columns),
            "missing_values": int(self.df.isnull().sum().sum()),
            "duplicates": int(self.df.duplicated().sum())
        }

    # -------------------------
    # SEARCH
    # -------------------------

    def search(self, column, value):

        if column not in self.df.columns:
            return None

        result = self.df[
            self.df[column].astype(str).str.contains(
                str(value),
                case=False,
                na=False
            )
        ]

        return result

    # -------------------------
    # CALCULATE
    # -------------------------

    def calculate_average(self, column):

        if column not in self.df.columns:
            return None

        if not pd.api.types.is_numeric_dtype(self.df[column]):
            return None

        return float(self.df[column].mean())

    def calculate_sum(self, column):

        if column not in self.df.columns:
            return None

        if not pd.api.types.is_numeric_dtype(self.df[column]):
            return None

        return float(self.df[column].sum())

    def calculate_max(self, column):

        if column not in self.df.columns:
            return None

        return self.df[column].max()

    def calculate_min(self, column):

        if column not in self.df.columns:
            return None

        return self.df[column].min()

    # -------------------------
    # ADD
    # -------------------------

    def add_row(self, data):

        new_row = pd.DataFrame([data])

        self.df = pd.concat(
            [self.df, new_row],
            ignore_index=True
        )

        self.save()

    # -------------------------
    # UPDATE
    # -------------------------

    def update_row(self, row_id, column, value):

        if "ID" not in self.df.columns:
            return False

        index = self.df.index[
            self.df["ID"].astype(str) == str(row_id)
        ]

        if len(index) == 0:
            return False

        self.df.loc[index[0], column] = value

        self.save()

        return True

    # -------------------------
    # DELETE
    # -------------------------

    def delete_row(self, row_id):

        if "ID" not in self.df.columns:
            return False

        original_length = len(self.df)

        self.df = self.df[
            self.df["ID"].astype(str) != str(row_id)
        ]

        if len(self.df) == original_length:
            return False

        self.save()

        return True

    # -------------------------
    # SAVE
    # -------------------------

    def save(self):

        self.df.to_csv(
            self.file_path,
            index=False
        )