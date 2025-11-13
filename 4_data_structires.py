# Lists
age = 30
my_list = ["Alice", 25, age, True]

name = my_list[0]
my_list[0] = "Dave"

my_list.append("Alice") # add an item at the end of the list
my_list.remove(age)

my_list.insert(0, "Alice")

print(my_list)
print(len(my_list))
print(my_list.count(age))
print(my_list.index("Dave"))

# Dictionaries
# key value data structure

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

person["licence"] = "True"

del person["licence"]

print(person)
print(person["name"])
print(person.keys())

# Tuples - are like lists but immutable, uses parentesis
empty = ()
colors = ("red", "black", "white", "blue")

print(colors[0])

# Sets
# you can create sets using {} or using set()
empty_set = {}
set2 = set([2,3,5,7,8])