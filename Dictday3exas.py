#1. Invert a dictionary with list values (group keys by their values)
#Input:
#d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
#Output:
#{1: ['a', 'c'], 2: ['b'], 3: ['d']}
#(Hint: Use setdefault method)

d = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
inverted_dict = {}
for key, value in d.items():
    inverted_dict.setdefault(value, []).append(key)
print(inverted_dict)

#2. Find Max and Min Value in Dictionary
#Input:
#d = {'a': 10, 'b': 5, 'c': 15}
#Output:
#Max Value → 15
#Min Value → 5

d = {'a': 8, 'b': 5, 'c': 15}
max_value = max(d.values())
min_value = min(d.values())
print("Max Value →", max_value)
print("Min Value →", min_value)

#3. Create a dictionary using dictionary comprehension for the given list of numbers,
#where:
#• Each number is a key.
#•The value is "prime" if the number is prime.
#•The value is "notprime" if the number is not prime.
#Output: {2: 'prime', 3: 'prime', 4: 'notprime', 5: 'prime', 6: 'notprime'}

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
numbers = [2, 3, 4, 5, 6]
prime_dict = {n: "prime" if is_prime(n) else "notprime" for n in numbers}
print(prime_dict)

#4. Create a dictionary from a list of words, keys as words, values as word lengths, but
#only for words longer than 3 characters
# List: ["hi", "hello", "world", "is", "great"]

words = ["hi", "hello", "world", "is", "great"]
word_length_dict = {word: len(word) for word in words if len(word) > 3}
print(word_length_dict)

#5. Create a dictionary with uppercase letters as keys and their ASCII values as values use
#dict comprehension .
#Input: letters = ['a', 'b', 'c']
#Expected Output:
#{'A': 65, 'B': 66, 'C': 67}

letters = ['a', 'b', 'c']
ascii_dict = {letter.upper(): ord(letter.upper()) for letter in letters}
print(ascii_dict)

#6. Explain about setdefault function in dictionary data type ?

#setdefault() Function in Python Dictionary
#The setdefault() method in Python dictionaries is used to:
#Get the value of a key if it exists.
#Insert the key with a default value if it does not exist.
#Syntax - dict.setdefault(key, default_ 

#Example 1: Key exists
d = {'name': 'Alice', 'age': 25}
value = d.setdefault('name', 'Unknown')
print(value) 
print(d)          

#Example 2: Key does not exist
d = {'name': 'Alice', 'age': 25}
value = d.setdefault('city', 'New York')
print(value)
print(d)    

#Example 3: Grouping items
data = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot'), ('vegetable', 'tomato')]
grouped = {}
for category, item in data:
    grouped.setdefault(category, []).append(item)
print(grouped)

#7. Difference between d[key] and d.get(key)?

#1. d[key] – Direct Access
#Raises an error if the key is not found (KeyError).
#Used when you're sure the key exists.

#Example:
d = {'name': 'Alice', 'age': 23}
print(d['name']) 
print(d['age']) 

#2. d.get(key) – Safe Access
#Returns None if the key is not found (or a custom default value).
#Safer for optional keys or when missing keys are okay.

#Example:
d = {'name': 'Alice', 'age': 23}
print(d.get('name'))
print(d.get('age'))
print(d.get('age', 0))

#8. What is the difference between Shallow Copy and Deep Copy in Python? Explain with examples.

#1. Shallow Copy
#Creates a new outer object.
#Nested objects (like lists inside lists) are not copied — only references are copied.

#Example:
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
shallow[0][0] = 99
print("Original:", original)
print("Shallow:", shallow)

#2. Deep Copy
#Creates a new outer object and recursively copies all nested objects.
#Completely independent copy.

#Example:
import copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 99
print("Original:", original)
print("Deep:", deep)

#9.How to swap two variables without using a third variable?

#Pythonic Way (Tuple Unpacking)
a = 10
b = 20
a, b = b, a
print("a =", a)
print("b =", b)

#2. Using Arithmetic Operations (only for numbers)
a = 5
b = 7
a = a + b
b = a - b
a = a - b
print("a =", a)
print("b =", b)

#10.Explain packing and unpacking in Python.

#Packing
x=["Sunny",25,"CE"]
print(x)

#Unpacking
x=["Ravi",20,"Btech","CE"]
name,age,education,department=x
print(name)
print(age)
print(education)
print(department)

#11.What is the use of enumerate(), zip(), map(), filter(), reduce()?

#1. enumerate()
#Purpose: Adds a counter to an iterable (like a list), returning index-value pairs.

#Example:
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

#2. zip()
#Purpose: Combines multiple iterables into a single iterable of tuples, pairing elements by position.

#Example:
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(name, age)

#3. map()
#Purpose: Applies a function to each item in an iterable and returns a new iterator.

#Example:
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

#4. filter()
#Purpose: Filters items from an iterable based on a function that returns True/False.

#Example:
numbers = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # [2, 4]

#5. reduce() (from functools module)
#Purpose: Applies a function cumulatively to items in a sequence, reducing it to a single value.

#Example:
from functools import reduce
numbers = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 10