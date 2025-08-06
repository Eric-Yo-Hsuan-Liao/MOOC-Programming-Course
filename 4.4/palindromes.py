
prompt = input('Please type in a palindrome: ')

prompt2 = list(prompt)
prompt_original = prompt2.copy()
reversed = []
while len(prompt2) != 0:
    letter = prompt2.pop()
    reversed.append(letter)
if prompt_original == reversed:
    print('This is a palindrome')
elif prompt_original != reversed:
    print('This is not a palindrome')







