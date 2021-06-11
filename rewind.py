# casting

numberofReminders= int('3')

print(numberofReminders)

print(type(numberofReminders))

a="Hello World"

print(a[1])

print(10<9)
print(10>3)
print(1 == 0)

# if statements

a=10
b=12

if (b > a):
    print("B is greater than a")
else:
    print("A is greater than B")

    # Opertaions

a=45
b=44

print(a + b)

# lists,tuples,sets and dictionaries in pyton are built in data types
# lists-ordered and changeable

fruits=["apple","banana"] 
print("I got githeri and fruits")

print(len(fruits))

# tuples orderred and unchangeable-
tuples=("apples","bananas","organges")

# sets-unordered,unindexed 
sets={"apple"}
# Dictionary-has key and value pairs
Dictionary={

    "type":"Honda",
    "model":"Type R",
    "year":"The latest year",


}
print (Dictionary)

# Conditional statements
# Python has two conditions- while and for
# while-executes a atatement as long as the condition is true 

p=9

while p>3:
    print(p)
    p += 1
    break

# For loop-iterating through a sequence

for x in fruits:
    print(x)

# Pass statements can be used to avoid an eror

# Functions in python is created using the def keyword

def vegetables():
    print("We all love vegetables")

vegetables()

# oop in python
class myclass():
    x=5
new = myclass()

print(new.x)
