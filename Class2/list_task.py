""" Class work in list operations
"""

name = ["ujjawal", "joshep "]
age = [26, 25]

print(name[0], "=", age[0])
print(name[1], "=", age[1])

# * Implementation specific methods in list
# * count functions in list operations
number = [1, 2, 3, 4, 5, 6, 7, 8, 8, 1, 2]
print(number.count(2))

# * Index functions in list operations
print(number.index(1))

# * Insert functions:- inster specific values in particular index
number.insert(4, 55)
print(number)

# * Pop functions:- remove specific values from specific index
number.pop(4)
print(number)

# * reverse methods in list operations
name = ["a", "b", "c", "z", "d", "e"]
name.reverse()
print(name)

# * sort methods in list operations
name.sort()
print(name)

# * clear methods in list operations
name.clear()
print(name)
