# import re


# class AnalyticsAgent:

#     def __init__(self, engine):
#         self.engine = engine

#     def process(self, command):

#         command = command.strip()

#         if not command:
#             return {
#                 "success": False,
#                 "message": "Please enter a command."
#             }

#         text = command.lower()

#         # -------------------------
#         # CALCULATIONS
#         # -------------------------

#         if any(word in text for word in [
#             "average",
#             "mean",
#             "avg"
#         ]):

#             column = self.find_column(text)

#             if not column:
#                 return {
#                     "success": False,
#                     "message": "Which column should I calculate the average of?"
#                 }

#             result = self.engine.calculate_average(column)

#             if result is None:
#                 return {
#                     "success": False,
#                     "message": f"'{column}' is not a numeric column."
#                 }

#             return {
#                 "success": True,
#                 "type": "calculation",
#                 "message": f"Average {column} is {result:.2f}"
#             }


#         if "total" in text or "sum" in text:

#             column = self.find_column(text)

#             if not column:
#                 return {
#                     "success": False,
#                     "message": "Which column should I calculate?"
#                 }

#             result = self.engine.calculate_sum(column)

#             if result is None:
#                 return {
#                     "success": False,
#                     "message": f"'{column}' is not a numeric column."
#                 }

#             return {
#                 "success": True,
#                 "type": "calculation",
#                 "message": f"Total {column} is {result:.2f}"
#             }


#         if "highest" in text or "maximum" in text or "max" in text:

#             column = self.find_column(text)

#             if not column:
#                 column = self.find_numeric_column()

#             if column:
#                 result = self.engine.calculate_max(column)

#                 return {
#                     "success": True,
#                     "type": "calculation",
#                     "message": f"Maximum {column} is {result}"
#                 }


#         if "lowest" in text or "minimum" in text or "min" in text:

#             column = self.find_column(text)

#             if not column:
#                 column = self.find_numeric_column()

#             if column:
#                 result = self.engine.calculate_min(column)

#                 return {
#                     "success": True,
#                     "type": "calculation",
#                     "message": f"Minimum {column} is {result}"
#                 }


#         # -------------------------
#         # DELETE
#         # -------------------------

#         if "delete" in text or "remove" in text:

#             match = re.search(
#                 r"(?:id|employee)\s*(?:is|=)?\s*(\d+)",
#                 text
#             )

#             if not match:
#                 return {
#                     "success": False,
#                     "message": "Please specify the employee ID. Example: Delete employee ID 5"
#                 }

#             employee_id = match.group(1)

#             success = self.engine.delete_row(employee_id)

#             if success:
#                 return {
#                     "success": True,
#                     "type": "delete",
#                     "message": f"Employee ID {employee_id} deleted successfully."
#                 }

#             return {
#                 "success": False,
#                 "message": f"Employee ID {employee_id} was not found."
#             }


#         # -------------------------
#         # UPDATE SALARY
#         # -------------------------

#         if "update" in text or "change" in text or "set" in text:

#             id_match = re.search(
#                 r"(?:id|employee)\s*(?:is|=)?\s*(\d+)",
#                 text
#             )

#             salary_match = re.search(
#                 r"(?:salary|pay)\D*(\d+(?:,\d+)?)",
#                 text
#             )

#             if id_match and salary_match:

#                 employee_id = id_match.group(1)

#                 salary = salary_match.group(1).replace(",", "")

#                 success = self.engine.update_row(
#                     employee_id,
#                     "Salary",
#                     salary
#                 )

#                 if success:
#                     return {
#                         "success": True,
#                         "type": "update",
#                         "message":
#                             f"Salary of employee ID {employee_id} "
#                             f"updated to {salary}."
#                     }

#                 return {
#                     "success": False,
#                     "message":
#                         f"Employee ID {employee_id} was not found."
#                 }

#             return {
#                 "success": False,
#                 "message":
#                     "For salary update use: "
#                     "'Change employee ID 3 salary to 60000'"
#             }


#         # -------------------------
#         # SEARCH / QUERY
#         # -------------------------

#         if any(word in text for word in [
#             "show",
#             "find",
#             "search",
#             "list",
#             "who"
#         ]):

#             # Department search
#             for department in [
#                 "IT",
#                 "HR",
#                 "Finance",
#                 "Sales"
#             ]:

#                 if department.lower() in text:

#                     result = self.engine.search(
#                         "Department",
#                         department
#                     )

#                     return {
#                         "success": True,
#                         "type": "table",
#                         "message":
#                             f"Found {len(result)} employees in {department}.",
#                         "data":
#                             result.to_dict(orient="records")
#                     }


#             # Generic column/value search
#             columns = self.engine.get_data().columns

#             for column in columns:

#                 if column.lower() in text:

#                     words = text.split()

#                     for word in words:

#                         if len(word) > 2:

#                             result = self.engine.search(
#                                 column,
#                                 word
#                             )

#                             if result is not None and len(result) > 0:

#                                 return {
#                                     "success": True,
#                                     "type": "table",
#                                     "message":
#                                         f"Found {len(result)} matching records.",
#                                     "data":
#                                         result.to_dict(
#                                             orient="records"
#                                         )
#                                 }


#         # -------------------------
#         # UNKNOWN COMMAND
#         # -------------------------

#         return {
#             "success": False,
#             "message":
#                 "I couldn't understand that command yet. "
#                 "Try: 'average salary', "
#                 "'show IT employees', "
#                 "'delete employee ID 5', "
#                 "or 'change employee ID 3 salary to 60000'."
#         }


#     # -------------------------
#     # FIND COLUMN
#     # -------------------------

#     # def find_column(self, text):

#     #     columns = self.engine.get_data().columns

#     #     for column in columns:

#     #         if column.lower() in text:

#     #             return column

#     #     # Common aliases

#     #     aliases = {
#     #         "pay": "Salary",
#     #         "income": "Salary",
#     #         "age": "Age",
#     #         "salary": "Salary"
#     #     }

#     #     for word, column in aliases.items():

#     #         if word in text and column in columns:
#     #             return column

#     #     return None

#     def find_column(self, text):

#         columns = self.engine.get_data().columns

#         text = text.lower()

#         # Check exact column names first
#         for column in columns:

#             column_name = column.lower()

#             # Match complete words, not partial words
#             if re.search(r"\b" + re.escape(column_name) + r"\b", text):
#                 return column

#         # Common aliases
#         aliases = {
#             "pay": "Salary",
#             "income": "Salary",
#             "wage": "Salary",
#             "salary": "Salary",
#             "age": "Age"
#         }

#         for word, column in aliases.items():

#             if re.search(r"\b" + re.escape(word) + r"\b", text):

#                 if column in columns:
#                     return column

#         return None


#     # -------------------------
#     # NUMERIC COLUMN
#     # -------------------------

#     def find_numeric_column(self):

#         df = self.engine.get_data()

#         for column in df.columns:

#             if df[column].dtype != "object":

#                 return column

#         return None

import re
import pandas as pd


class AnalyticsAgent:

    def __init__(self, engine):
        self.engine = engine

    def process(self, command):

        command = command.strip()

        if not command:
            return {
                "success": False,
                "message": "Please enter a command."
            }

        text = command.lower()

        # ==================================================
        # AVERAGE
        # ==================================================

        if any(word in text for word in ["average", "mean", "avg"]):

            column = self.find_column(text)

            if not column:
                return {
                    "success": False,
                    "message": "Which column should I calculate the average of?"
                }

            result = self.engine.calculate_average(column)

            if result is None:
                return {
                    "success": False,
                    "message": f"'{column}' is not numeric."
                }

            return {
                "success": True,
                "type": "calculation",
                "message": f"Average {column} is {result:.2f}"
            }

        # ==================================================
        # TOTAL / SUM
        # ==================================================

        if "total" in text or "sum" in text:

            column = self.find_column(text)

            if not column:
                return {
                    "success": False,
                    "message": "Which column should I calculate?"
                }

            result = self.engine.calculate_sum(column)

            if result is None:
                return {
                    "success": False,
                    "message": f"'{column}' is not numeric."
                }

            return {
                "success": True,
                "type": "calculation",
                "message": f"Total {column} is {result:.2f}"
            }

        # ==================================================
        # HIGHEST / MAXIMUM
        # ==================================================

        if (
            "highest" in text
            or "maximum" in text
            or "max" in text
        ):

            column = self.find_column(text)

            if not column:
                column = self.find_numeric_column()

            result = self.engine.calculate_max(column)

            return {
                "success": True,
                "type": "calculation",
                "message": f"Maximum {column} is {result}"
            }

        # ==================================================
        # LOWEST / MINIMUM
        # ==================================================

        if (
            "lowest" in text
            or "minimum" in text
            or "min" in text
        ):

            column = self.find_column(text)

            if not column:
                column = self.find_numeric_column()

            result = self.engine.calculate_min(column)

            return {
                "success": True,
                "type": "calculation",
                "message": f"Minimum {column} is {result}"
            }

        # ==================================================
        # COUNT
        # ==================================================

        if (
            "how many" in text
            or "count" in text
            or "number of" in text
        ):

            df = self.engine.get_data()

            # Count department
            for department in [
                "it",
                "hr",
                "finance",
                "sales"
            ]:

                if department in text:

                    result = df[
                        df["Department"]
                        .astype(str)
                        .str.lower()
                        == department
                    ]

                    return {
                        "success": True,
                        "type": "table",
                        "message":
                            f"There are {len(result)} employees in {department.upper()}.",
                        "data":
                            result.to_dict(orient="records")
                    }

            return {
                "success": True,
                "type": "calculation",
                "message": f"Total employees: {len(df)}"
            }

        # ==================================================
        # TOP N
        # ==================================================

        top_match = re.search(
            r"(?:top|first)\s+(\d+)",
            text
        )

        if top_match:

            number = int(top_match.group(1))

            column = self.find_column(text)

            if not column:
                column = "Salary"

            df = self.engine.get_data()

            if column in df.columns:

                result = df.sort_values(
                    by=column,
                    ascending=False
                ).head(number)

                return {
                    "success": True,
                    "type": "table",
                    "message":
                        f"Top {number} employees by {column}.",
                    "data":
                        result.to_dict(orient="records")
                }

        # ==================================================
        # SORT
        # ==================================================

        if (
            "sort" in text
            or "order" in text
            or "arrange" in text
        ):

            column = self.find_column(text)

            if not column:
                column = "Salary"

            descending = (
                "descending" in text
                or "highest" in text
                or "largest" in text
                or "high to low" in text
            )

            df = self.engine.get_data()

            if column in df.columns:

                result = df.sort_values(
                    by=column,
                    ascending=not descending
                )

                direction = (
                    "highest to lowest"
                    if descending
                    else "lowest to highest"
                )

                return {
                    "success": True,
                    "type": "table",
                    "message":
                        f"Sorted {column} from {direction}.",
                    "data":
                        result.to_dict(orient="records")
                }

        # ==================================================
        # NUMERIC CONDITION
        # ==================================================

        condition_match = re.search(
            r"(?:greater than|more than|above|over|higher than|less than|below|under)\s*[₹$]?\s*(\d+(?:,\d+)?)",
            text
        )

        if condition_match:

            value = float(
                condition_match.group(1).replace(",", "")
            )

            column = self.find_column(text)

            # If no explicit numeric column is found,
            # assume Salary when employee query is used.
            if not column:
                column = "Salary"

            df = self.engine.get_data()

            if column in df.columns:

                if any(
                    phrase in text
                    for phrase in [
                        "less than",
                        "below",
                        "under"
                    ]
                ):

                    result = df[
                        df[column] < value
                    ]

                    operator_text = f"below {value:g}"

                else:

                    result = df[
                        df[column] > value
                    ]

                    operator_text = f"above {value:g}"

                return {
                    "success": True,
                    "type": "table",
                    "message":
                        f"Found {len(result)} records with {column} {operator_text}.",
                    "data":
                        result.to_dict(orient="records")
                }

        # ==================================================
        # DEPARTMENT QUERY
        # ==================================================

        for department in [
            "IT",
            "HR",
            "Finance",
            "Sales"
        ]:

            if department.lower() in text:

                result = self.engine.search(
                    "Department",
                    department
                )

                return {
                    "success": True,
                    "type": "table",
                    "message":
                        f"Found {len(result)} employees in {department}.",
                    "data":
                        result.to_dict(orient="records")
                }

        # ==================================================
        # DELETE
        # ==================================================

        if (
            "delete" in text
            or "remove" in text
        ):

            match = re.search(
                r"(?:id|employee)\s*(?:is|=)?\s*(\d+)",
                text
            )

            if not match:

                return {
                    "success": False,
                    "message":
                        "Please specify the employee ID."
                }

            employee_id = match.group(1)

            success = self.engine.delete_row(
                employee_id
            )

            if success:

                return {
                    "success": True,
                    "type": "delete",
                    "message":
                        f"Employee ID {employee_id} deleted successfully."
                }

            return {
                "success": False,
                "message":
                    f"Employee ID {employee_id} was not found."
            }

        # ==================================================
        # UPDATE
        # ==================================================

        if (
            "update" in text
            or "change" in text
            or "set" in text
        ):

            id_match = re.search(
                r"(?:id|employee)\s*(?:is|=)?\s*(\d+)",
                text
            )

            salary_match = re.search(
                r"(?:salary|pay)\D*(\d+(?:,\d+)?)",
                text
            )

            if id_match and salary_match:

                employee_id = id_match.group(1)

                salary = salary_match.group(1).replace(
                    ",",
                    ""
                )

                success = self.engine.update_row(
                    employee_id,
                    "Salary",
                    salary
                )

                if success:

                    return {
                        "success": True,
                        "type": "update",
                        "message":
                            f"Salary of employee ID {employee_id} updated to {salary}."
                    }

                return {
                    "success": False,
                    "message":
                        f"Employee ID {employee_id} was not found."
                }

            return {
                "success": False,
                "message":
                    "Example: Change employee ID 3 salary to 60000"
            }

        # ==================================================
        # GENERIC SEARCH
        # ==================================================

        if any(
            word in text
            for word in [
                "show",
                "find",
                "search",
                "list",
                "who"
            ]
        ):

            df = self.engine.get_data()

            for column in df.columns:

                column_lower = column.lower()

                if column_lower in text:

                    # Try to find useful words
                    words = text.split()

                    for word in words:

                        if len(word) < 3:
                            continue

                        result = self.engine.search(
                            column,
                            word
                        )

                        if (
                            result is not None
                            and len(result) > 0
                        ):

                            return {
                                "success": True,
                                "type": "table",
                                "message":
                                    f"Found {len(result)} matching records.",
                                "data":
                                    result.to_dict(
                                        orient="records"
                                    )
                            }

        # ==================================================
        # UNKNOWN COMMAND
        # ==================================================

        return {
            "success": False,
            "message":
                "I couldn't understand that query yet."
        }

    # ==================================================
    # FIND COLUMN
    # ==================================================

    def find_column(self, text):

        columns = self.engine.get_data().columns

        text = text.lower()

        for column in columns:

            column_name = column.lower()

            if re.search(
                r"\b"
                + re.escape(column_name)
                + r"\b",
                text
            ):
                return column

        aliases = {
            "pay": "Salary",
            "income": "Salary",
            "wage": "Salary",
            "salary": "Salary",
            "age": "Age"
        }

        for word, column in aliases.items():

            if re.search(
                r"\b"
                + re.escape(word)
                + r"\b",
                text
            ):

                if column in columns:
                    return column

        return None

    # ==================================================
    # FIND NUMERIC COLUMN
    # ==================================================

    def find_numeric_column(self):

        df = self.engine.get_data()

        for column in df.columns:

            if pd.api.types.is_numeric_dtype(
                df[column]
            ):

                return column

        return None