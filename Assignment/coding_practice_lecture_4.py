""" This is Coding Practices assignment"""

# * Problem 1
# * 3 - 4 guest

guest_list = ["guest1", "guest2", "guest3", "guest4"]

# * Print message to particular guest using a for loop
for guest_name in guest_list:
    print(f"Hello {guest_name}, I am inviting you for dinner tonight.")

# * Next problem :- Update guest list
# * Suppose the guest4 will not able to join the dinner party.
# * Print message, guest4 will not able to join the dinner party.
print("guest4 will not able to join the dinner party.")

# * So that, invite guest10 to the dinner party.
guest_list[3] = "guest10"

# * Print new guest list
print(guest_list)

# * Circulate message to particular guest using a for loop
# * Use f-string to print message
for guest_name in guest_list:
    print(f"Hello {guest_name}, I am inviting you for dinner tonight.")

# * Problem 3, more guests will come so we need bigger dinning table
print("Note:- More guests will come so we need bigger dinning table")

# * Use insert method of list to add new guest in list
# * I add guest5 in the initial index of the list, by using 0, it means first index of the list.
guest_list.insert(0, "guest5")
print(guest_list)

# * Similarly, add guest6 in the middle index of the list, by using 4, it means fourth index
guest_list.insert(4, "guest6")
print(guest_list)

# * Similarly, use append method to add new guest in list
guest_list.append("guest7")
print(guest_list)

# * Send invitation message to all the guests using a for loop
for guest_name in guest_list:
    print(f"Hello {guest_name}, I am inviting you for dinner tonight.")


# * Problem 4, print invitation message to only two guest
print(
    f"Invitation message, only two guest named as {guest_list[0]} and {guest_list[1]} are inviting you for dinner tonight."
)

# * Remove all guests except guest_list[0] and guest_list[1]
# * Note: pop method removes the last element from the list.
# * I invited only guest having index 0 and index 1 from the list.
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
print(guest_list)

# * Circulate message to particular guest using a for loop
for guest_name in guest_list:
    print(f"Hello {guest_name}, I am inviting you for dinner tonight.")

# * Use del method to remove guest_list[0] and guest_list[1]
# * First delete guest_list[1], index 1 item is deleted from the list.
del guest_list[1]

# * Second delete guest_list[0], index 0 item is deleted from the list.
del guest_list[0]

# * Print guest_list to show there is no guest in the list.
print(guest_list)

# * Problem 5, Seeing the world
world_list = ["world2", "world1", "world4", "world3", "world5"]

# * Print world_list using raw python print function
print(world_list[0])
print(world_list[1])
print(world_list[2])
print(world_list[3])
print(world_list[4])

# * Using sorted method to sort the list
sorted_list = sorted(world_list)
print("sorted_list", sorted_list)

# * Print original list, to show it is not modified
print("original world_list", world_list)

# * Use reverse method to reverse the list
world_list.reverse()

# * Print reversed list, to show it is modified
print("reversed world_list", world_list)

# * Again use reverse method to return original list
world_list.reverse()

# * Print world_list, to show it is back to original list
print("back to original world_list", world_list)

# * Sort world list using sort method of python
world_list.sort()

# * Print world_list, to show it is sorted
print("sorted world_list", world_list)

# * Sort world list in reverse alphabetically using sort method of python
world_list.sort(reverse=True)

# * Print world_list, to show it is sorted in reverse alphabetically
print("sorted world_list in reverse alphabetically", world_list)

# * Problem 6, Dinner Guest, print number of guests
# * It might show 0 guest while printing because in above problem (shrinking guest list), we delete all guests except guest_list[0] and guest_list[1].
print(f"Number of guests is {len(guest_list)}")

# * Problem 7, Every Function
# * Implemenation of every function in list for mountain, river, country, city , etc.

# * First initialize empty list
all_functions = []

# * Add mountain, river, country, city in all_functions list
all_functions.append("mountain")
all_functions.append("river")
all_functions.append("country")
all_functions.append("city")
all_functions.append("city")
all_functions.append("house")

# * Print mountain, river, country, city in all_functions list
print(all_functions)

# * Implement count method in list datatype
# * Count:- it count number of repeatation of each element in the list
print(all_functions.count("city"))

# * Implement index method in list datatype
# * Return the index of the element in the list
print(all_functions.index("river"))

# * Insert mountain in all_functions list
# * Add mountain in index 0 of all_functions list
all_functions.insert(0, "mountain")
print(all_functions)

# * Implement pop function to remove item from all_functions list
# * Remove mountain in index 0 of all_functions list
all_functions.pop(0)

# * Print to show index 0 item is removed from all_functions list
print(all_functions)

# * Implement remove method to remove item from all_functions list
# * Remove mountain from all_functions list
all_functions.remove("mountain")

# * Print to show mountain is removed from all_functions list
print(all_functions)

# * Implement reverse method to reverse all_functions list
all_functions.reverse()

# * Print to show all_functions list is reversed
print("reverse", all_functions)

# * Implement sort function
all_functions.sort()

# * Print to show all_functions list is sorted
print("sorted", all_functions)

# * Problem Dictionary practice
# * Initialize course dictionary with key as course name and value as instructor name
course_dictionary = {
    "course1": "Instrutor1",
    "course2": "Instrutor2",
    "course3": "Instrutor3",
    "course4": "Instrutor4",
    "course5": "Instrutor5",
    "course6": "Instrutor6",
    "course7": "Instrutor7",
}

# * Rename course instructor name of course3
course_dictionary["course3"] = "Instrutor3_replace"

# * Print course_dictionary
print(course_dictionary)
