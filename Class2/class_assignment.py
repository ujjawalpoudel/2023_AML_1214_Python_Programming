# * Question number 1 create a list to print 10 furniture stores items

# * Approache :- Create list of ten furniture stores
furniture_stores = [
    "first furniture store",
    "second furniture store",
    "third furniture store",
    "fourth furniture store",
    "fifth furniture store",
    "sixth furniture store",
    "seventh furniture store",
    "eighth furniture store",
    "ninth furniture store",
    "tenth furniture store",
]

# * Question number 2 replace all of the items with gadgets
gadgets_name_list = [
    "first gadget",
    "second gadget",
    "third gadget",
    "fourth gadget",
    "fifth gadget",
    "sixth gadget",
    "seventh gadget",
    "eighth gadget",
    "ninth gadget",
    "tenth gadget",
]

# * Conditional:- length of furniture stores list and gadget names list must be equal
for x in range(len(furniture_stores)):
    furniture_stores[x] = gadgets_name_list[x]
    # * replace every index value of furniture stores with gadget name

# * print list of furniture
print(furniture_stores)

# * Question number 3 print the values using for loop
for x in furniture_stores:
    print(x)

# * Question number 4 delete middle 2 items
legth_of_list = len(furniture_stores)

middle_index = legth_of_list // 2

# * substrate index with 1 as index start from 0 not from 1
middle_index = middle_index - 1

# * remove middle 2 items
furniture_stores.pop(middle_index)
# * After del operation, list is reorder that's why same index is use for delete next items from list
furniture_stores.pop(middle_index)

print(furniture_stores)

# * Question number 5 craeet one more list for keeping college names in Ontario
college_name_list = ["college_1", "college_2", "college_3", "college_4"]

# * Question number 6 now merge both lists gadgets and college
new_college_name_list = college_name_list + gadgets_name_list
print(new_college_name_list)
