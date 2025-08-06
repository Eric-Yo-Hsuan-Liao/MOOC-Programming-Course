

def filter_solutions():
    with open('solutions.csv', 'r') as file:
        with open('correct.csv', 'w') as correct_file:
            with open('incorrect.csv', 'w') as incorrect_file:
                for line in file:
                    name,problem,result = line.split(';')
                    addition = '+'
                    subtraction = '-'
                    if addition in problem:
                        num1, num2 = problem.split('+')
                        answer = int(num1) + int(num2)
                        if answer == int(result):
                            correct_file.write(line)
                        else:
                            incorrect_file.write(line)
                    if subtraction in problem:
                        num1, num2 = problem.split('-')
                        answer = int(num1) - int(num2)
                        if answer == int(result):
                            correct_file.write(line)
                        else:
                            incorrect_file.write(line)

filter_solutions()
filter_solutions