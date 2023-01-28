# * Dictionary class example
class_dict = {"car": "Tesla", "truck": "Toyota", "bus": "Ford"}

# * Print class_dict
print(class_dict)

# * Print particular value of class_dict
print(class_dict["bus"])

# * Use variable to print particular value of class_dict
bus = class_dict["bus"]
print(bus)

# * Print all keys of class_dict
print(class_dict.keys())

# * Print all values of class_dict
print(class_dict.values())

# * Replace particular value of class_dict
class_dict["bus"] = "Honda"
print(class_dict)

# * Update key and value in dictionary
class_dict.update({"milage": "20"})
print(class_dict)

# * Next method to add key and value in dictionary
class_dict["colour"] = "Red"
print(class_dict)

# * Delete particular key value pair from dictionary
class_dict.pop("bus")
print(class_dict)

# * Print all keys of class_dict using for loop
for key, value in class_dict.items():
    print(key, value)

# * Copy dictionary
copy_class_dict = class_dict.copy()
print(copy_class_dict)

# * Delete all key value pairs from dictionary
class_dict.clear()
print(class_dict)
