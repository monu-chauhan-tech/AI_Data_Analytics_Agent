from intent_classifier import IntentClassifier


classifier = IntentClassifier()


commands = [
    "What is the average salary?",
    "Show employees earning above 45000",
    "Delete employee ID 5",
    "Change employee ID 3 salary to 60000",
    "Show top 3 employees",
    "How many employees are there?",
    "Sort employees by salary",
    "Show IT employees",
    "Hello"
]


for command in commands:

    result = classifier.classify(command)

    print("\nCommand:", command)
    print("Result:", result)