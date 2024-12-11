

##############################ranges#####################################################

# Range Practice #1
# Create a list consisting of all the numbers from 2500 to 2585 (inclusive). Store this list in the variable my_list.

#list comprehention = A concise way to create lists in Python Compact amd easier to read than traditional loops [expression for value in iterable if condition]

# doubles = []
# for x in range(1,11):
#     doubles.append(x*2)

# print(doubles)
###############################################################
# doubles = [ x *2 for x in range(1,11)]
# tripes = [y  * 3 for y in range(1,11)]
# squares = [ z*z for z in range(1,11)]


# print(doubles)
# print(tripes)
# print(squares)
#############################################################
fruits = ["apple"," mango",' bannana','coconut']
# fruit_chars = [fruit[1]for fruit in fruits]

# print(fruit_chars)
word_legnths = [len() for word in fruits]
print(word_legnths)
###############################################################
# numbers = [1,-2, 3,4,5,-6]
# positive_nums = [num for num in numbers if num>= 0 ]
# negative_nums = [num for num in numbers if num< 0 ]
# evens_nums = [num for num in numbers if num %2 == 0 ]
# odd_nums = [num for num in numbers if num %2 == 1]
# print(positive_nums)
# print(negative_nums)
# print(evens_nums)
# print(odd_nums)

# grades = [85,42,79,61,30,90]
# passing_grades  = [grade for grade in grades if grade >= 60]

# print(passing_grades)

# numbers = [ 3, 7, 10, 15, 21]
# doubled_values = [ value * 2 for value in numbers]

# print( doubled_values)




# Range Practice #2
# Using the range() function, create in a single line of code a list consisting of all numbers that are multiples of 3 from 3 to 300 (inclusive). Store this list in the variable my_list.



# Range Practice #3
# Use the range() function and a loop to add the squares of all the numbers from 1 to 15 (inclusive). Store the result in a variable called sum_squares.



# For this purpose:

# Create a range of values that you can iterate through in a loop

# For each of these values, find its squared value (power of 2). You may need to create intermediate variables (optionally).

# Sum all the squared values obtained. Accumulate the sum in the variable sum_squares.



##############################enumerators in python #####################################################


# Enumerator Practice #1
# Print sentences like the following on the screen:

# '{name} is found at index {index}'

# Where name must be each of the names in the list below, and the index, must be obtained via enumerate().

# list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]

# You can use the given print() line as an example and change its variable names, but the returned phrases must be the same!

# Tip: use loops!

# list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]

# print(f'{nombre} se encuentra en el índice {indice}')



# Enumerator Practice #2
# Create a list formed by the tuples (index, element), obtained through enumerating the indices of each character of the "Python" string.

# Call the returned list with the variable name indices_list.

# "Python"


# Enumerator Practice #3
# Print to the screen only the indices of those names in the list below, that start with M:

# list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]

# You can solve it in different ways, but it will help you keeping mind some (if not all) the following elements:

# loops

# if conditionals

# the enumerate() method

# string methods and indexing

# list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]



#######################ranges challenge#####################
# Challenge: Create a list of all numbers from 10 to 100 that are divisible by both 4 and 6.

# Use a range and list comprehension to find numbers divisible by 4 and 6

# Print the result


#######################enumerators challenge#####################
# Challenge: Print the index and name of each fruit in a list using the enumerate() function.

# List of fruits

# Use enumerate to display each fruit with its index