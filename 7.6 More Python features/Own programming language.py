
import string

def initialize_vars(variables: dict):
    for letter in string.ascii_uppercase:
        variables[letter] = 0

def run(program: list):
    vars = {}
    initialize_vars(vars)
    answer = []
    # This is for keeping track of where the location is 
    labels = {}
    idx = 0
    for i in program:
        parts = i.split(' ')
        if parts[0].endswith(':'):
            label_name = parts[0].replace(':','')
            labels[label_name] = idx
        idx += 1
    pointer = 0
    while pointer < len(program):
        parts = program[pointer].split(' ')
        action = parts[0]
        if action == 'MOV':
            if parts[2] in vars:
                vars[parts[1]] = vars[parts[2]]
            else:
                vars[parts[1]] = int(parts[2])
        elif action == 'ADD':
            if parts[2] in vars:
                vars[parts[1]] += vars[parts[2]]
            else:
                vars[parts[1]] += int(parts[2])
        elif action == 'SUB':
            if parts[2] in vars:
                vars[parts[1]] -= vars[parts[2]]
            else:
                vars[parts[1]] -= int(parts[2])
        elif action == 'MUL':
            if parts[2] in vars:
                vars[parts[1]] *= vars[parts[2]]
            else:
                vars[parts[1]] *= int(parts[2])
        elif action == 'PRINT':
            if parts[1] in vars:
                answer.append(vars[parts[1]])
            else:
                answer.append(int(parts[1]))
        elif action == 'END':
            break
        elif action.endswith(':'):
            pass
        elif action == 'JUMP':
            label = parts[1]
            pointer = labels[label]
        elif action == 'IF':
            left = parts[1]
            op = parts[2]
            right = parts[3]
            act = parts[4]
            lab = parts[5]
            left_value = vars[left] if left in vars else int(left)
            right_value = vars[right] if right in vars else int(right)
            condition = False
            if op == '==':
                condition = left_value == right_value
            elif op == '!=':
                condition = left_value != right_value
            elif op == '>=':
                condition = left_value >= right_value
            elif op == '<=':
                condition = left_value <= right_value
            elif op == '>':
                condition = left_value > right_value
            elif op == '<':
                condition = left_value < right_value
            if condition:
                pointer = labels[lab]
                continue

        pointer += 1
    return answer

program1 = []
program1.append("MOV A 1")
program1.append("MOV B 2")
program1.append("PRINT A")
program1.append("PRINT B")
program1.append("ADD A B")
program1.append("PRINT A")
program1.append("END")
result = run(program1)
print(result)


program2 = []
program2.append("MOV A 1")
program2.append("MOV B 10")
program2.append("begin:")
program2.append("IF A >= B JUMP quit")
program2.append("PRINT A")
program2.append("PRINT B")
program2.append("ADD A 1")
program2.append("SUB B 1")
program2.append("JUMP begin")
program2.append("quit:")
program2.append("END")
result = run(program2)
print(result)

program3 = []
program3.append("MOV A 1")
program3.append("MOV B 1")
program3.append("begin:")
program3.append("PRINT A")
program3.append("ADD B 1")
program3.append("MUL A B")
program3.append("IF B <= 10 JUMP begin")
program3.append("END")
result = run(program3)
print(result)


program4 = []
program4.append("MOV N 50")
program4.append("PRINT 2")
program4.append("MOV A 3")
program4.append("begin:")
program4.append("MOV B 2")
program4.append("MOV Z 0")
program4.append("test:")
program4.append("MOV C B")
program4.append("new:")
program4.append("IF C == A JUMP error")
program4.append("IF C > A JUMP over")
program4.append("ADD C B")
program4.append("JUMP new")
program4.append("error:")
program4.append("MOV Z 1")
program4.append("JUMP over2")
program4.append("over:")
program4.append("ADD B 1")
program4.append("IF B < A JUMP test")
program4.append("over2:")
program4.append("IF Z == 1 JUMP over3")
program4.append("PRINT A")
program4.append("over3:")
program4.append("ADD A 1")
program4.append("IF A <= N JUMP begin")
result = run(program4)
print(result)



