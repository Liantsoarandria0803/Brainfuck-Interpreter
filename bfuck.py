def brainfuck_interpreter(code, input_data=""):
    code = list(code)
    tape = [0] * 30000
    tape_ptr = 0
    code_ptr = 0
    input_ptr = 0
    output = []

    # Preprocess brackets to find matching brackets for fast jumps
    bracket_map = {}
    stack = []

    for i, command in enumerate(code):
        if command == '[':
            stack.append(i)
        elif command == ']':
            start = stack.pop()
            bracket_map[start] = i
            bracket_map[i] = start

    while code_ptr < len(code):
        command = code[code_ptr]

        if command == '>':
            tape_ptr += 1
        elif command == '<':
            tape_ptr -= 1
        elif command == '+':
            tape[tape_ptr] = (tape[tape_ptr] + 1) % 256
        elif command == '-':
            tape[tape_ptr] = (tape[tape_ptr] - 1) % 256
        elif command == '.':
            output.append(chr(tape[tape_ptr]))
        elif command == ',':
            if input_ptr < len(input_data):
                tape[tape_ptr] = ord(input_data[input_ptr])
                input_ptr += 1
            else:
                tape[tape_ptr] = 0  # No input left, set cell to 0
        elif command == '[':
            if tape[tape_ptr] == 0:
                code_ptr = bracket_map[code_ptr]
        elif command == ']':
            if tape[tape_ptr] != 0:
                code_ptr = bracket_map[code_ptr]

        code_ptr += 1

    return ''.join(output)
## reading file 

file=open('placeYourCOde.txt','r')
BfCode=file.read() 
# Example :
#brainfuck_code = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++." ##hello
#output = brainfuck_interpreter(brainfuck_code)
#print("Output:", output)
output=brainfuck_interpreter(BfCode)
print("Your code output:",output)
### Test your code