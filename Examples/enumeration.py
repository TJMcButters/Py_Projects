# Enumerations add an interable to the item that you are iterating over
a_list = ["apple", "banana", "cantoloupe"]
print(f"No Enumeration: {a_list}")

b_list = [(index, value) for index, value in enumerate(a_list)]
print(f"With Enumeration: {b_list}")