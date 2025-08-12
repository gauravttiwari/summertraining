# create a list

# using square brackets
fruits = ["apple", "banana","cherry"]

# using list function
fruits2 = list(("apple", "banana","cherry","mango","kiwi"))

# print(fruits)
# print(fruits2)


# access elements of list
# print(fruits[0])
# print(fruits[-2])
# print(fruits[-2])
# print(fruits[0:3])

#change elements in list

# fruits2[1] = "Kiwi"

# print(fruits2)

# adding element
fruits2.append("grapes")


# add at specific position
fruits2.insert(1,"orange")

# add multiple elements
fruits2
print(fruits2)


#add multiple elements
fruits2.extend(["pineapple", "watermelon"])
fruits2
print(fruits2)

# remove elements
fruits2.remove("mango")
print(fruits2)

# by index
fruits2.pop(2)
print(fruits2)

# slicing string
print(fruits2[1:4])

# slicing in the start
print(fruits2[:4])

# slicing in the end
print(fruits2[2:])

# negative indexing
print(fruits2[-3:-1])

#String Concatenation
a = 'Hello'
b = 'world'
c = a + ' ' + b
print(c)
