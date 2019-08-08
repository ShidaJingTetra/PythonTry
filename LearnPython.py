
# Python is designed to mimic English with
# inputs from math.
print("Hello World")

# Python doesn't have variable declarations.
# Variables are declared the moment they are assigned.
message = "5 is indeed greater than 2"

# Indentations are used to determine code blocks.
# They are part of the syntax.
if 5>2 :
    print(message)

print("Comment can be part of a ling") # Comment can be part of a line.

# Variables can change types after they are assigned.
message = 5;
print(message);

# All three types of numbers can be converted with respect to each other
x = 7
x = complex(x)
print(x)
print(type(x))

# Assign multi line strings using """
a = """ This is a 
multiline string.
And it ends
right here."""
print(a)

# Strings are arrays
print(a[2])
print(a[4:14])

# We can combine numbers and strings using format()
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# Python has identity operatiors to check if two things 
# are the same in object (in memory, I suspect).
x = ['this', 'that']
y = ['this', 'that']
print(x is y)
# false
print(x == y)
# true

x = 9
y = 9
print(x is y)
# true
print(x == y)
# true

# List
# Ordered, changable, allows duplicates
trylist = ['one', 'two', 'three']
print(trylist)
# Iteration
for x in trylist:
    print(x)
# Check item
if 'one' in trylist:
    print('Yes')
# Use .append, .insert to add items
# Use .remove, .pop, del to remove items

# Tuples
# Ordered, unchangable, allows duplicates
