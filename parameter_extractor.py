# import re


# class ParameterExtractor:

#     def extract(self, command):

#         text = command.lower().strip()

#         result = {
#             "column": None,
#             "value": None,
#             "operator": None,
#             "id": None,
#             "limit": None,
#             "department": None
#         }

#         # ==========================================
#         # COLUMN
#         # ==========================================

#         if re.search(r"\b(salary|pay|income|wage)\b", text):
#             result["column"] = "Salary"

#         elif re.search(r"\bage\b", text):
#             result["column"] = "Age"

#         elif re.search(r"\bdepartment\b", text):
#             result["column"] = "Department"

#         elif re.search(r"\bname\b", text):
#             result["column"] = "Name"

#         elif re.search(r"\bid\b", text):
#             result["column"] = "ID"

#         # ==========================================
#         # OPERATOR
#         # ==========================================

#         if re.search(
#             r"\b(greater than|more than|above|over|higher than)\b",
#             text
#         ):
#             result["operator"] = ">"

#         elif re.search(
#             r"\b(less than|below|under|lower than)\b",
#             text
#         ):
#             result["operator"] = "<"

#         elif re.search(
#             r"\b(equal to|equals|is|=)\b",
#             text
#         ):
#             result["operator"] = "="

#         # ==========================================
#         # NUMBER / VALUE
#         # ==========================================

#         number_match = re.search(
#             r"[₹$]?\s*(\d+(?:,\d+)?)",
#             text
#         )

#         if number_match:

#             value = number_match.group(1)

#             result["value"] = float(
#                 value.replace(",", "")
#             )

#             if result["value"].is_integer():
#                 result["value"] = int(result["value"])

#         # ==========================================
#         # EMPLOYEE ID
#         # ==========================================

#         id_match = re.search(
#             r"(?:employee\s*)?(?:id)\s*(?:is|=)?\s*(\d+)",
#             text
#         )

#         if id_match:
#             result["id"] = int(
#                 id_match.group(1)
#             )

#         # ==========================================
#         # TOP N
#         # ==========================================

#         limit_match = re.search(
#             r"\b(?:top|first)\s+(\d+)\b",
#             text
#         )

#         if limit_match:
#             result["limit"] = int(
#                 limit_match.group(1)
#             )

#         # ==========================================
#         # DEPARTMENT
#         # ==========================================

#         departments = [
#             "IT",
#             "HR",
#             "Finance",
#             "Sales"
#         ]

#         for department in departments:

#             if re.search(
#                 r"\b" + re.escape(
#                     department.lower()
#                 ) + r"\b",
#                 text
#             ):

#                 result["department"] = department
#                 break

#         return result

import re


class ParameterExtractor:

    def extract(self, command):

        text = command.lower().strip()

        result = {
            "column": None,
            "value": None,
            "operator": None,
            "id": None,
            "limit": None,
            "department": None
        }

        # ==========================================
        # COLUMN DETECTION
        # ==========================================

        # Salary
        if re.search(
            r"\b(salary|pay|income|wage|earning|earnings)\b",
            text
        ):
            result["column"] = "Salary"

        # Age
        elif re.search(
            r"\bage\b",
            text
        ):
            result["column"] = "Age"

        # Department
        elif re.search(
            r"\bdepartment\b",
            text
        ):
            result["column"] = "Department"

        # Name
        elif re.search(
            r"\bname\b",
            text
        ):
            result["column"] = "Name"

        # ID
        elif re.search(
            r"\bid\b",
            text
        ):
            result["column"] = "ID"

        # ==========================================
        # DEPARTMENT DETECTION
        # ==========================================

        departments = [
            "IT",
            "HR",
            "Finance",
            "Sales"
        ]

        for department in departments:

            if re.search(
                r"\b" + re.escape(
                    department.lower()
                ) + r"\b",
                text
            ):

                result["department"] = department

                # If user says "IT employees",
                # IT means Department.
                if result["column"] is None:
                    result["column"] = "Department"

                break

        # ==========================================
        # OPERATOR
        # ==========================================

        if re.search(
            r"\b(greater than|more than|above|over|higher than)\b",
            text
        ):
            result["operator"] = ">"

        elif re.search(
            r"\b(less than|below|under|lower than)\b",
            text
        ):
            result["operator"] = "<"

        elif re.search(
            r"\b(equal to|equals)\b",
            text
        ):
            result["operator"] = "="

        # ==========================================
        # EMPLOYEE ID
        # ==========================================

        id_match = re.search(
            r"(?:employee\s*)?(?:id)\s*(?:is|=)?\s*(\d+)",
            text
        )

        if id_match:

            result["id"] = int(
                id_match.group(1)
            )

        # ==========================================
        # TOP N
        # ==========================================

        limit_match = re.search(
            r"\b(?:top|first)\s+(\d+)\b",
            text
        )

        if limit_match:

            result["limit"] = int(
                limit_match.group(1)
            )

        # ==========================================
        # VALUE
        # ==========================================

        # For conditions such as:
        # salary above 45000
        # age greater than 25

        value_match = re.search(
            r"(?:greater than|more than|above|over|higher than|less than|below|under|equal to|equals)"
            r"\s*[₹$]?\s*(\d+(?:,\d+)?)",
            text
        )

        if value_match:

            value = value_match.group(1)

            result["value"] = int(
                value.replace(",", "")
            )

        return result