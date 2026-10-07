from parameter_extractor import ParameterExtractor


extractor = ParameterExtractor()


commands = [

    "Show employees earning more than 45000",

    "Show employees above 25 age",

    "What is the average salary?",

    "Change employee ID 3 salary to 60000",

    "Delete employee ID 5",

    "Show top 3 employees by salary",

    "Show IT employees"
]


for command in commands:

    result = extractor.extract(command)

    print("\nCommand:")
    print(command)

    print("Parameters:")
    print(result)