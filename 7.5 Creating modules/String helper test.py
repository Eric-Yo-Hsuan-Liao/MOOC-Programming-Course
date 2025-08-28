

import String_helper

my_string = "Well hello there!"

print(String_helper.change_case(my_string))

p1, p2 = String_helper.split_in_half(my_string)
print(p1)
print(p2)

m2 = String_helper.remove_special_characters("This is a test, lets see how it goes!!!11!")
print(m2)