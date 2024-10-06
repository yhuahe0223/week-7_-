
############################################################################
# Boolean expressions are statements that can be either True or False. In Python, the boolean data type is represented by the built-in data type bool.

# Boolean expressions are commonly used for decision-making in programming.

# Here's a breakdown with examples:

# 1. Comparison Operators:
# These operators are used to compare two values:

# == (Equal to): Checks if the two values are equal.

# python
# Copy code
# print(5 == 5)  # True
# print(5 == 6)  # False
# != (Not equal to): Checks if two values are not equal.

# python
# Copy code
# print(5 != 5)  # False
# print(5 != 6)  # True
# < (Less than): Checks if the left value is less than the right value.

# python
# Copy code
# print(5 < 6)  # True
# print(6 < 5)  # False
# > (Greater than): Checks if the left value is greater than the right value.

# python
# Copy code
# print(5 > 6)  # False
# print(6 > 5)  # True
# <= (Less than or equal to): Checks if the left value is less than or equal to the right value.

# python
# Copy code
# print(5 <= 6)  # True
# print(6 <= 6)  # True
# >= (Greater than or equal to): Checks if the left value is greater than or equal to the right value.

# python
# Copy code
# print(5 >= 6)  # False
# print(6 >= 6)  # True
# 2. Logical Operators:
# These operators are used to combine conditional statements:

# and: Returns True if both statements are true.

# python
# Copy code
# x = 5
# print(x > 3 and x < 10)  # True
# or: Returns True if at least one of the statements is true.

# python
# Copy code
# x = 5
# print(x > 3 or x > 10)  # True
# not: Reverse the result, returns False if the result is true.

# python
# Copy code
# x = 5
# print(not(x > 3 and x < 10))  # False
# 3. Membership Operators:
# in: Returns True if a sequence with the specified value is present in the object.

# python
# Copy code
# x = [1, 2, 3, 4, 5]
# print(3 in x)  # True
# not in: Returns True if a sequence with the specified value is not present in the object.

# python
# Copy code
# x = [1, 2, 3, 4, 5]
# print(6 not in x)  # True
# 4. Identity Operators:
# is: Returns True if both variables are the same object.

# python
# Copy code
# x = [1, 2, 3]
# y = [1, 2, 3]
# z = x
# print(x is z)  # True, because z is the same object as x
# print(x is y)  # False, because x and y are not the same objects
# is not: Returns True if both variables are not the same object.

# python
# Copy code
# x = [1, 2, 3]
# y = [1, 2, 3]
# print(x is not y)  # True
# Remember, every boolean expression will evaluate to either True or False, and understanding this concept is fundamental for decision-making in programming.
