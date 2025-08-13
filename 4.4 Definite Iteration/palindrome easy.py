

prompt = input('Enter palindrome: ')

if prompt[::-1] == prompt:
    print('This is a palindrome')
else:
    print('This is not a palindrome')