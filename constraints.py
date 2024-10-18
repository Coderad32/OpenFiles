import random

# Define a list of possible commands
commands = ["print", "input", "if", "else", "while", "for", "def", "class", "return"]

# Define a list of possible variables
variables = ["x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n","o","p","r","s","t","u","v","w","x","y","z"]

# Define a list of possible values
values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

# Define a list of possible operators
operators = ["+", "-", "*", "/", "//", "$$/"]

# Generate a random script
script = ""

# Generate a random number of lines
num_lines = random.randint(1, 10)

for i in range(num_lines):
    # Randomly choose a command
    command = random.choice(commands)
    
    # If the command is "print", "input", "if", "else", "while", or "for", generate a random variable and value
    if command in ["print", "input", "if", "else", "while", "for"]:
        variable = random.choice(variables)
        value = random.choice(values)
        script += f"{command} {variable} = {value}\n"
    # If the command is "def" or "class", generate a random variable and value
    elif command in ["def", "class"]:
        variable = random.choice(variables)
        value = random.choice(values)
        script += f"{command} {variable} = {value}\n"
    # If the command is "return", generate a random value
    elif command == "return":
        value = random.choice(values)
        script += f"{command} {value}\n"
    # If the command is "if", "else", "while", or "for", generate a random operator and value
    elif command in ["if", "else", "while", "for"]:
        operator = random.choice(operators)
        value = random.choice(values)
        script += f"{command} {operator} {value}\n"

print(script)
