from data_engine import DataEngine
from intent_classifier import IntentClassifier
from parameter_extractor import ParameterExtractor
from tool_manager import ToolManager


DATA_FILE = "data/employees.csv"

engine = DataEngine(DATA_FILE)

classifier = IntentClassifier()
extractor = ParameterExtractor()
tools = ToolManager(engine)


commands = [
    "What is the average salary?",
    "Show employees earning more than 45000",
    "Show employees above 25 age",
    "How many employees are in IT?",
    "Show IT employees",
    "Show top 3 employees by salary"
]


for command in commands:

    print("\n" + "=" * 60)
    print("COMMAND:", command)

    # Step 1: Intent
    intent = classifier.classify(command)

    print("INTENT:", intent)

    # Step 2: Parameters
    parameters = extractor.extract(command)

    print("PARAMETERS:", parameters)

    # Step 3: Tool execution
    result = tools.execute(
        intent,
        parameters
    )

    print("RESULT:", result)