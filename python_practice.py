# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning.
# Name: Faye Chiang 

# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments
XXX 
Have user input an integer N
Set a to 0
Set b to 1
Set count to 0
Set total to 0

While count is less than N
    Add a to total
    Set next_value to a + b
    Set a to b
    Set b to next_value
    Increment count by 1

Print total
 XXX
"""

# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments
# to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to 
# identify the error and fix it (the correct total that should be printed is 12).
N = 6

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 # set count to 0
total = 0 # set total to 0

while count < N: # loop while count is less than N
    total = total + a # add a to total

    next_value = a + b # calculate the next fibonacci number
    a = b # set a to b
    b = next_value # set b to next_value

    count = count + 1 # increment count by 1

print(total) # print the total of the first N fibonacci numbers

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.
import numpy as np

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
standard_deviation = np.std(fibonacci)

print(standard_deviation)

# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.

def fibonacci_sum(N): 
    a = 0
    b = 1
    total = 0

    for count in range(N):
        total = total + a
        next_value = a + b
        a = b
        b = next_value

    return total


values = [5, 10, 15, 20, 25, 30]
sums = []

for N in values:
    sums.append(fibonacci_sum(N))

print(sums)

# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = 0 # TypeError: a must be an integer, not a string
    b = 1 # TypeError: b must be an integer, not a string
    index = 0  # Fixes NameError by defining index 

    while a <= limit: 
        next_value = a + b
        a = b
        b = next_value
        index += 1 # NameError: index must be defined

    return index


result = find_fib_above_limit(50)
print("The index of the first number above your limit is: ", result)
# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. 
# If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers 
# less than or equal to the input "limit".


def sum_odd_fib(limit):
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 != 0:  # This line checks if the Fibonacci number is odd
            total += b
        a, b = b, a + b
    return total


# Add your test cases here
print(sum_odd_fib(0)) #expected: 0
print(sum_odd_fib(1))   #expected: 2
print(sum_odd_fib(3))   #expected: 5
print(sum_odd_fib(10))  #expected: 10
print(sum_odd_fib(13)) #expected: 23
# %%
