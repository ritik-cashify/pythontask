#List Comprehension- List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
list = ["purvansh", "cashify"]
newlist = []

for x in list:
  if "a" in x:
    newlist.append(x)

print(newlist)
