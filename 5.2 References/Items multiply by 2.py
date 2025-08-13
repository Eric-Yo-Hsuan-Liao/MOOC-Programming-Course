

def double_items(numbers: list):
    result = []
    for i in numbers:
        result.append(i * 2)
    print(numbers)
    print(result)
    return result


nums = [2,4,5,3,11,-4]
nums_doubled = double_items(nums)
print(f"Original: {nums}")
print(f"Doubled: {nums_doubled}")