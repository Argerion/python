from beautifultable import BeautifulTable


# Chapter 1 Exercises, Python Programming (Zelle)

# Exercise 1.1
# Start up an interactive Python session and try typing in each of
# the following commands. Write down the results you see.

print("Hello, world!") # Shows "Hello, world!"
print("Hello", "world!") # Shows "Hello world!"
print(3) # Shows 3
print(3.0) # Shows 3.0 (float)
print (2 + 3) # Shows 5
print(2.0 + 3.0) # Shows 5.0
print("2" + "3") # Shows "23"
print("2 + 3 =", 2+3) # Shows "2 + 3 = 5"
print(2 * 3) # Shows 6
print(2 ** 3) # Shows 8
print(7 / 3) # Shows 2.33333335
print(7 // 3) # Shows 2

# Exercise 1.2
# Enter and run the chaos program from Section 1.6. Try it out with various
# values of input to see that it functions as described in the chapter.

print()

def chaos():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: ") )
    for i in range(10) :
        x = 3.9 * x * (1 - x)
        print(x)

chaos()

# Using 0.5 as the input yields

"""
0.975
0.09506250000000008
0.33549992226562525
0.8694649252590003
0.44263310911310905
0.962165255336889
0.1419727793616139
0.4750843861996143
0.9725789275369049
0.1040097132674683
"""


# Exercise 1.3
# Modify the chaos program using 2.0 in place of 3.9 as the multiplier in the
# logistic function. Your modified line of code should look like this:
# X = 2. 0 * X * (1 - X)

print()
def chaos_modified():
    print("This program illustrates a chaotic function - slightly modified")
    x = eval(input("Enter a number between 0 and 1: ") )
    for i in range(10) :
        x = 2.0 * x * (1 - x)
        print(x)

chaos_modified()

# Using 0.5 as the input yields 0.5 all the way through
# Using 0.9 yields

"""
0.17999999999999997
0.29519999999999996
0.41611392
0.4859262511644672
0.49960385918742867
0.49999968614491325
0.49999999999980305
0.5
0.5
0.5
"""

# Converges to 0.5

# Exercise 1.4
# Modify the chaos function to print out 20 values instead of 10

# Answer: This can be done easily by changing range from 10 to 20


# Exercise 1.5
# Modify the chaos function to print out a certain number of values
# based on user input


# Answer: Add the following lines after x = eval(input( line

# y = int(input("How many calculations would you like to print out?"))
# for i in range(y):
#   ...

# More sophisticated programs will do error checking, e.g. no negative numbers
# or zeroes, only integers, etc.


# Exercise 1.6
# The calculation performed in the chaos program can be written in a number
# of ways that are algebraically equivalent. Write a version of the program
# for each of the following ways of doing the computation. Have your
# modified programs print out 100 iterations of the calculation and compare
# the results when run on the same input.
# a) 3.9 * x * (1 - x)
# b) 3.9 * (x - x * x)
# c) 3.9 * X - 3.9 * X * X

# Explain the results of this experiment.

def chaos_v1():
    print("Chaos Function Version 1")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x = 3.9 * x * (1 - x)
        print(x)

def chaos_v2():
    print("Chaos Function Version 2")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100) :
        x = 3.9 * (x - x * x)
        print(x)

def chaos_v3():
    print("Chaos Function Version 3")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100) :
        x = 3.9 * x - 3.9 * x * x
        print(x)

print()
chaos_v1()
print()
chaos_v2()
print()
chaos_v3()

    
# Explanation: Although these are algebraically equivalent, the second iteration
# already showed minor differences in the least significant digits.
# These differences compounded over time such that by the 100th iteration,
# the end results were completely different.

# 2nd iteration for chaos 1 (input 0.4): 0.2336256000000002
# 2nd iteration for chaos 2 (input 0.4): 0.23362560000000027
# 2nd iteration for chaos 3 (input 0.4): 0.23362560000000032



# Exercise 1.7
# (Advanced) Modify the chaos program so that it accepts two inputs and
# then prints a table with two columns similar to the one shown in Section
# 1.8.

# This will make use of the BeautifulTable API to simplify the process


def chaos_table():
    table = BeautifulTable()
    print("This program accepts 2 inputs and prints out results side-by-side")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter a number between 0 and 1: "))
    table.columns.header = ["Input: " + str(x), "Input: " + str(y)]
    for i in range(1, 11, 1):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        table.rows.append([x, y])
    print(table)

chaos_table()
