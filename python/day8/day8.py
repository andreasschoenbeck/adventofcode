

instructions = []
executedInstructions = []
pointer = 0
accumulator = 0

with open("C:\\data\\dotnet_projects\\adventofcode\\python\\day8\\input_01.txt", 'r') as f:
    instructions = f.readlines()


while pointer not in executedInstructions:
    instruction = instructions[pointer]
    parts = instruction.split(" ")
    operation = parts[0]
    operand = parts[1]

    executedInstructions.append(pointer)
    instructionIncrement = 1

    if operation == "acc":
        accumulator += int(operand)
    elif operation == "jmp":
        instructionIncrement = int(operand)
    
    pointer += instructionIncrement

print("accumulator before endless loop: " + str(accumulator))