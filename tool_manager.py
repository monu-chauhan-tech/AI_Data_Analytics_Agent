import pandas as pd


class ToolManager:

    def __init__(self, engine):
        self.engine = engine

    def execute(self, intent_data, parameters):

        intent = intent_data.get("intent")

        # ==========================================
        # CALCULATE
        # ==========================================

        if intent == "CALCULATE":

            operation = intent_data.get("operation")
            column = parameters.get("column")

            if not column:
                return {
                    "success": False,
                    "message": "I could not determine the column."
                }

            if operation == "AVERAGE":
                result = self.engine.calculate_average(column)

            elif operation == "SUM":
                result = self.engine.calculate_sum(column)

            elif operation == "MAX":
                result = self.engine.calculate_max(column)

            elif operation == "MIN":
                result = self.engine.calculate_min(column)

            else:
                return {
                    "success": False,
                    "message": "Unknown calculation."
                }

            if result is None:
                return {
                    "success": False,
                    "message": f"Cannot calculate {operation} for {column}."
                }

            return {
                "success": True,
                "type": "calculation",
                "operation": operation,
                "column": column,
                "result": result,
                "message": f"{operation} of {column}: {result}"
            }

        # ==========================================
        # FILTER
        # ==========================================

        if intent == "FILTER":

            column = parameters.get("column")
            operator = parameters.get("operator")
            value = parameters.get("value")

            if not column or not operator or value is None:
                return {
                    "success": False,
                    "message": "I need a column, operator and value."
                }

            df = self.engine.get_data()

            if column not in df.columns:
                return {
                    "success": False,
                    "message": f"Column '{column}' does not exist."
                }

            try:

                if operator == ">":
                    result = df[df[column] > value]

                elif operator == "<":
                    result = df[df[column] < value]

                elif operator == "=":
                    result = df[df[column] == value]

                else:
                    return {
                        "success": False,
                        "message": "Unsupported operator."
                    }

            except Exception:

                return {
                    "success": False,
                    "message": f"Cannot compare {column} with {value}."
                }

            return {
                "success": True,
                "type": "table",
                "message": f"Found {len(result)} matching records.",
                "data": result.to_dict(orient="records")
            }

        # ==========================================
        # COUNT
        # ==========================================

        if intent == "COUNT":

            df = self.engine.get_data()

            department = parameters.get("department")

            if department:

                result = df[
                    df["Department"]
                    .astype(str)
                    .str.lower()
                    == department.lower()
                ]

                return {
                    "success": True,
                    "type": "table",
                    "message":
                        f"There are {len(result)} employees in {department}.",
                    "data":
                        result.to_dict(orient="records")
                }

            return {
                "success": True,
                "type": "calculation",
                "result": len(df),
                "message": f"Total employees: {len(df)}"
            }

        # ==========================================
        # SEARCH
        # ==========================================

        if intent == "SEARCH":

            department = parameters.get("department")

            if department:

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

            return {
                "success": False,
                "message":
                    "Please specify what you want me to search for."
            }

        # ==========================================
        # TOP N
        # ==========================================

        if intent == "TOP_N":

            limit = parameters.get("limit")
            column = parameters.get("column")

            if not limit:
                return {
                    "success": False,
                    "message": "Please specify how many records."
                }

            if not column:
                column = "Salary"

            df = self.engine.get_data()

            if column not in df.columns:
                return {
                    "success": False,
                    "message": f"Column '{column}' does not exist."
                }

            result = df.sort_values(
                by=column,
                ascending=False
            ).head(limit)

            return {
                "success": True,
                "type": "table",
                "message":
                    f"Top {limit} records by {column}.",
                "data":
                    result.to_dict(orient="records")
            }

        # ==========================================
        # SORT
        # ==========================================

        if intent == "SORT":

            column = parameters.get("column")

            if not column:
                column = "Salary"

            df = self.engine.get_data()

            if column not in df.columns:
                return {
                    "success": False,
                    "message": f"Column '{column}' does not exist."
                }

            result = df.sort_values(
                by=column,
                ascending=True
            )

            return {
                "success": True,
                "type": "table",
                "message":
                    f"Sorted records by {column}.",
                "data":
                    result.to_dict(orient="records")
            }

        # ==========================================
        # DELETE
        # ==========================================

        if intent == "DELETE":

            employee_id = parameters.get("id")

            if employee_id is None:
                return {
                    "success": False,
                    "message": "Please specify the employee ID."
                }

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

        # ==========================================
        # UPDATE
        # ==========================================

        if intent == "UPDATE":

            employee_id = parameters.get("id")
            value = parameters.get("value")
            column = parameters.get("column")

            if employee_id is None:
                return {
                    "success": False,
                    "message": "Please specify the employee ID."
                }

            if not column:
                column = "Salary"

            if value is None:
                return {
                    "success": False,
                    "message": "Please specify the new value."
                }

            success = self.engine.update_row(
                employee_id,
                column,
                value
            )

            if success:

                return {
                    "success": True,
                    "type": "update",
                    "message":
                        f"Employee ID {employee_id} updated successfully."
                }

            return {
                "success": False,
                "message":
                    f"Employee ID {employee_id} was not found."
            }

        # ==========================================
        # ADD
        # ==========================================

        if intent == "ADD":

            return {
                "success": False,
                "message":
                    "Add operation will be connected in the next integration step."
            }

        # ==========================================
        # UNKNOWN
        # ==========================================

        return {
            "success": False,
            "message":
                "I don't know how to execute this operation yet."
        }