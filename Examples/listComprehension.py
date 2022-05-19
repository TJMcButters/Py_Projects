# You could make a list like this
a_list = []
for x in range(10):
    a_list.append(x)
    
# Or you could simplify the process by using a list comprehension, like this:
another_list = [x for x in range(10)]

# both lists produce the same result
print(a_list)
print(another_list)