

def read_input(prompt, lower_fence: int, upper_fence: int):
    while True:
        try:
            number = int(input(prompt))
            if number >= lower_fence and number <= upper_fence:
                return number
                False
            elif number <= lower_fence or number >= upper_fence:
                print(f'You must type in an integer between {lower_fence} and {upper_fence}')
        except ValueError:
            print(f'You must type in an integer between {lower_fence} and {upper_fence}')


number = read_input('Please type in a number: ', 5, 10)
print('You typed in: ', number)