
# example with a string and number

string_1 = "123"
string_2 = 123

a_list = [string_1, string_2]
a_list.remove(string_1)
print(f"Add a string and remove again before printing {a_list}")


class CustomString(object):
    def __init__(self, text, number):
        self.text = text
        self.number = number

    def __eq__(self, other):
        print(self, other)
        # return self.text == other.text and self.number == other.number and self is other
        return self.text == other.text and self.number == other.number

    def __repr__(self):
        return f"CustomString({self.text}, {self.number})"

# Example with Custom class


# Setups 3 CustomString objects and adds them to a list
custom_string_1 = CustomString("abc1", 1)
custom_string_2 = CustomString("abc2", 2)
custom_string_3 = CustomString("abc3", 3)
print(f"Printing a CustomString instance: {custom_string_2}")
a_custom_list = [custom_string_1, custom_string_2, custom_string_3]

# Create a 4th CustomString object and try to remove it from the list
print(f"Printing a list of CustomString instances: {a_custom_list}")
print(" --------------- Remove ----------------- ")
custom_string_not_in_list = CustomString("abc3", 3)
a_custom_list.remove(custom_string_not_in_list)
print(" --------------- Remove ----------------- ")
print(f"Printing a list of CustomString instances after one remove: {a_custom_list}")

# QUESTIONS
# 1. What happens when you try to delete the forth element not in the list?
# 2. What happens if you change the __eq__ implementation in CustomString

# Print the remaining list
for string in a_custom_list:
    print(repr(string))
