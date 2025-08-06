

def remove_smallest(numbers: list):
    smallest = numbers[0]
    for i in numbers:
        if i < smallest:
            smallest = i
    numbers.remove(smallest)

nums = [2,4,6,1,3,5]
remove_smallest(nums)
print(nums)