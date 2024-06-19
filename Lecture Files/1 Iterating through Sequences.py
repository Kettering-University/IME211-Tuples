# Iterating through Sequences: enumerate and range(len)

# ----------------------------------------------------
# region Using enumerate with Lists and Tuples
# ----------------------------------------------------
# The enumerate function adds a counter to an iterable and returns it as an enumerate object.
# This is particularly useful when you need both the value and the index of elements in a list or tuple.

# Example: Enumerate in Action
products = ["Pump", "Valve", "Sensor", "Filter"]
for index, product in enumerate(products):
    print(f"Product {index}: {product}")

# TODO: Activity 1 - Enumerate through a Tuple of Equipment
# Given a tuple of equipment names, use enumerate to print each equipment's index and name.
# Your code here:
equipment = ("Compressor", "Heat Exchanger", "Reactor", "Distillation Column")


# endregion

# ----------------------------------------------------
# region Using range(len(variable)) in List Comprehension
# ----------------------------------------------------
# The `range(len(variable))` pattern is a common way to iterate over the indices of a list or tuple.
# This is particularly useful in scenarios where you need to use the index to perform operations or access elements.
# `range()` generates a sequence of numbers, which, by default, starts at 0 and increments by 1.
# `len(variable)` gives the total number of elements in the list or tuple, thereby setting the upper limit for the range.

# Example: Accessing Elements by Index
production_capacities = [500, 600, 700, 800]
capacities_doubled = [production_capacities[i] * 2 for i in range(len(production_capacities))]
print("Doubled Capacities:", capacities_doubled)

# TODO: Activity 2 - Modify Elements Based on Index
# Double the production capacity for the first half of the list, leaving the second half unchanged.
# Your code here:
# As standard for loop


# As list comprehension


# endregion

# ----------------------------------------------------
# region Extra Practice
# ----------------------------------------------------
# Product codes and initial stock levels are provided as follows:
product_codes = ("P1", "P2", "P3", "P4", "P5")
stock_levels = [120, 80, 150, 30, 200]

# TODO: Activity 3 - Identify products with stock levels below 100 units and print their product codes using enumerate.
# Your code here:


# TODO: Activity 4 - Identify products with stock levels below 100 units and print their product codes using range(len).
# Your code here:


# endregion
