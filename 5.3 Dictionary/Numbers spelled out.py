




def dict_of_numbers():
    first_nums = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 
             12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
    tens = {20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

    new_dict = {}
    for i in range(0,100):
        new_dict[i] = ''
    for i in new_dict:
        if i in first_nums:
            new_dict[i] = first_nums[i]
        elif i in tens:
            new_dict[i] = tens[i]
        else:
            tens_value = (i // 10) * 10
            one_part = i % 10
            new_dict[i] = tens[tens_value] + '-' + first_nums[one_part]
    return new_dict

numbers = dict_of_numbers()
print(numbers[24])
print(numbers[0])
print(numbers[98])