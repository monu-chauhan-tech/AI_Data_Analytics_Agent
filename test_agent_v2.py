from data_engine import DataEngine
from agent_v2 import AnalyticsAgentV2


DATA_FILE = "data/employees.csv"

engine = DataEngine(DATA_FILE)

agent = AnalyticsAgentV2(engine)


commands = [

    "What is the average salary?",

    "Show employees earning more than 45000",

    "Show employees above 25 age",

    "How many employees are in IT?",

    "Show IT employees",

    "Show top 3 employees by salary",

    "Sort employees by salary",

    "Delete employee ID 10"

]


for command in commands:

    print("\n" + "=" * 70)

    print("USER:")
    print(command)

    result = agent.process(command)

    print("\nAI RESULT:")
    print(result)