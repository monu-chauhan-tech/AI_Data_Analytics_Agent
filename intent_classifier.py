import re


class IntentClassifier:

    def classify(self, command):

        text = command.lower().strip()

        # -----------------------------
        # CALCULATION
        # -----------------------------

        if any(word in text for word in [
            "average",
            "mean",
            "avg"
        ]):
            return {
                "intent": "CALCULATE",
                "operation": "AVERAGE",
                "confidence": 0.95
            }

        if any(word in text for word in [
            "total",
            "sum"
        ]):
            return {
                "intent": "CALCULATE",
                "operation": "SUM",
                "confidence": 0.95
            }

        if any(word in text for word in [
            "highest",
            "maximum",
            "max"
        ]):
            return {
                "intent": "CALCULATE",
                "operation": "MAX",
                "confidence": 0.93
            }

        if any(word in text for word in [
            "lowest",
            "minimum",
            "min"
        ]):
            return {
                "intent": "CALCULATE",
                "operation": "MIN",
                "confidence": 0.93
            }

        # -----------------------------
        # DELETE
        # -----------------------------

        if any(word in text for word in [
            "delete",
            "remove"
        ]):
            return {
                "intent": "DELETE",
                "confidence": 0.98
            }

        # -----------------------------
        # UPDATE
        # -----------------------------

        if any(word in text for word in [
            "update",
            "change",
            "set"
        ]):
            return {
                "intent": "UPDATE",
                "confidence": 0.95
            }

        # -----------------------------
        # ADD
        # -----------------------------

        if any(word in text for word in [
            "add",
            "insert",
            "create"
        ]):
            return {
                "intent": "ADD",
                "confidence": 0.90
            }

        # -----------------------------
        # COUNT
        # -----------------------------

        if (
            "how many" in text
            or "count" in text
            or "number of" in text
        ):
            return {
                "intent": "COUNT",
                "confidence": 0.94
            }

        # -----------------------------
        # SORT
        # -----------------------------

        if any(word in text for word in [
            "sort",
            "order",
            "arrange"
        ]):
            return {
                "intent": "SORT",
                "confidence": 0.92
            }

        # -----------------------------
        # TOP N
        # -----------------------------

        if re.search(
            r"\b(top|first)\s+\d+",
            text
        ):
            return {
                "intent": "TOP_N",
                "confidence": 0.96
            }

        # -----------------------------
        # CONDITION QUERY
        # -----------------------------

        if re.search(
            r"(greater than|more than|above|over|higher than|less than|below|under)",
            text
        ):
            return {
                "intent": "FILTER",
                "confidence": 0.93
            }

        # -----------------------------
        # SEARCH / SHOW
        # -----------------------------

        if any(word in text for word in [
            "show",
            "find",
            "search",
            "list",
            "who"
        ]):
            return {
                "intent": "SEARCH",
                "confidence": 0.88
            }

        # -----------------------------
        # UNKNOWN
        # -----------------------------

        return {
            "intent": "UNKNOWN",
            "confidence": 0.20
        }