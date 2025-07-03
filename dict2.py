#1.Delete a list of keys from a dictionary
#sample_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}
# Keys to remove
#keys = ["name", "salary"]

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]
# Remove each key
for key in keys:
    sample_dict.pop(key, None)  # `None` prevents error if key is missing
# Print the updated dictionary
print(sample_dict)

#2. Count the frequency of each character in a given string using a dictionary.

def count_char_frequency(text):
    freq_dict = {}
    for char in text:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict
# Example usage
input_str = "hello world"
result = count_char_frequency(input_str)
print(result)

#3. Swap keys and values in a dictionary.

original_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}
# Swap keys and values
swapped_dict = {value: key for key, value in original_dict.items()}
print(swapped_dict)

#4. Write a program to sum all the values in a dictionary.

my_dict = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40
}
# Sum all values
total = sum(my_dict.values())
print("Sum of all values:", total)

#5. Create a nested dictionary for student details (name, roll, marks).

students = {
    "student1": {
        "name": "Alice",
        "roll": 101,
        "marks": 88
    },
    "student2": {
        "name": "Bob",
        "roll": 102,
        "marks": 92
    },
    "student3": {
        "name": "Charlie",
        "roll": 103,
        "marks": 79
    }
}
# Print the nested dictionary
for student_id, details in students.items():
    print(f"{student_id}: Name = {details['name']}, Roll = {details['roll']}, Marks = {details['marks']}")

#6. Convert a dictionary to a list of tuples.

my_dict = {"name": "Alice", "age": 25, "id":109, "city": "New York"}
# Convert to list of tuples
tuple_list = list(my_dict.items())
print(tuple_list)

#7. Write a program to store names as keys and their lengths as values.

names = ["Alice", "Bob", "Catherine", "David"]
# Create dictionary with names as keys and their lengths as values
name_lengths = {name: len(name) for name in names}
# Print the dictionary
print(name_lengths)

#8. Create a dictionary for numbers 1 to 5, where the value is "even" if the number is even, and "odd" if the number is odd
#Expected Output:
#{1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

num_dict = {num: "even" if num % 2 == 0 else "odd" for num in range(1, 6)}
# Print the dictionary
print(num_dict)

#9. Create Reverse Word Dictionary
#Given list of words:
#words = ["cat", "dog", "bat"]
#Create a dictionary with words as keys and their reversed strings as values
#xpected Output:
#{'cat': 'tac', 'dog': 'god', 'bat': 'tab'}

words = ["cat", "dog", "bat"]
# Create dictionary with reversed strings as values
reverse_dict = {word: word[::-1] for word in words}
# Print the dictionary
print(reverse_dict)