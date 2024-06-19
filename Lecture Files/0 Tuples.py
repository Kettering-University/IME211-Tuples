# Tuples

# ----------------------------------------------------
# region Introduction to Tuples
# ----------------------------------------------------
# Tuples are immutable sequences in Python, used to store collections of items.
# Unlike lists, which are mutable, tuples cannot be modified after creation.
# Tuples are preferred over lists for fixed data, enhancing code safety and integrity.

# Example: Basic Tuple
basic_tuple = ("Pump", "Valve", "Sensor")
print("Basic Tuple:", basic_tuple)

# TODO: Activity 1 - Understanding Tuple Immutability
# First, try to change the first element of `basic_tuple` to "Compressor".
# Next, observe the TypeError indicating that tuples do not support item assignment.
# Your code here:

# endregion

# ----------------------------------------------------
# region Creating Tuples
# ----------------------------------------------------
# Tuples can be created with or without parentheses. A trailing comma is needed for a single-element tuple.

# Example: Creating Different Types of Tuples
empty_tuple = ()
single_element_tuple = ("Compressor",)
without_parentheses = "Pump", "Valve"

print("Empty Tuple:", empty_tuple)
print("Single Element Tuple:", single_element_tuple)
print("Tuple Without Parentheses:", without_parentheses)

# TODO: Activity 2 - Create Your Own Tuples
# First, create an empty tuple named `empty`.
# Next, create a tuple named `machine` with a single element "Lathe".
# Then, create a tuple `tools` with elements "Hammer" and "Wrench" without using parentheses.
# Your code here:


# endregion

# ----------------------------------------------------
# region Accessing Tuple Elements & Tuple Operations
# ----------------------------------------------------
# Elements in a tuple can be accessed via indexing. Slicing allows getting a subset of the tuple.

# Example: Accessing and Slicing Tuples
equipment = ("Hammer", "Drill", "Saw", "Lathe")
first_item = equipment[0]
last_item = equipment[-1]
subset = equipment[1:3]

print("First Item:", first_item)
print("Last Item:", last_item)
print("Subset:", subset)

# Example: Tuple Concatenation and Repetition
tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
concatenated_tuple = tuple_a + tuple_b
repeated_tuple = tuple_a * 2

print("Concatenated Tuple:", concatenated_tuple)
print("Repeated Tuple:", repeated_tuple)

# Example: Using count and index
sample_tuple = (1, 2, 3, 2, 4, 2)
print("Count of 2:", sample_tuple.count(2))
print("Index of 4:", sample_tuple.index(4))

# TODO: Activity 3 - Access and Slice Your Tuple
# Add additional equipment of another "Saw" and "Screwdriver" to the equipment list
# Then repeat the list 4 times
# Then count the number of saws in the list
# Your code here:


# endregion

# ----------------------------------------------------
# region Nested Tuples
# ----------------------------------------------------
# Tuples can contain other tuples, creating nested structures that are useful for representing complex data.

# Example: Accessing Nested Tuple Elements
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("First element of the first nested tuple:", nested_tuple[0][0])

# TODO: Activity 4 - Work with Nested Tuples
# Given `nested_tuple`, access and print the second element of the last nested tuple.
# Then, iterate over `nested_tuple` and print each nested tuple.
# Your code here:


# endregion
