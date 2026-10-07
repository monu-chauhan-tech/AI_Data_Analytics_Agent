from intent_classifier import IntentClassifier
from parameter_extractor import ParameterExtractor
from tool_manager import ToolManager


class AnalyticsAgentV2:

    def __init__(self, engine):

        self.engine = engine

        # AI Brain components
        self.classifier = IntentClassifier()
        self.extractor = ParameterExtractor()
        self.tools = ToolManager(engine)

    def process(self, command):

        # ==========================================
        # STEP 1: UNDERSTAND INTENT
        # ==========================================

        intent_data = self.classifier.classify(
            command
        )

        # ==========================================
        # STEP 2: EXTRACT PARAMETERS
        # ==========================================

        parameters = self.extractor.extract(
            command
        )

        # ==========================================
        # STEP 3: EXECUTE TOOL
        # ==========================================

        result = self.tools.execute(
            intent_data,
            parameters
        )

        # ==========================================
        # ADD AI BRAIN INFORMATION
        # ==========================================

        result["intent"] = intent_data.get(
            "intent"
        )

        result["confidence"] = intent_data.get(
            "confidence"
        )

        result["parameters"] = parameters

        return result 