import math

# Chapter 6 Exercises

"""

# Exercise 6.1

# Write a program to print the lyrics of the song "Old MacDonald." Your
# program should print the lyrics for five different animals, similar to the
# example verse below.

def old_macdonald(animal):
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    print("And on that farm he had a " + animal + ", Ee-igh, Ee-igh, Oh!")
    print("With a moo, moo here and a moo, moo there.")
    print("Here a moo, there a moo, everywhere a moo, moo.")
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")

old_macdonald("cow")



# Exercise 6.3

# Write definitions for these functions:

# sphereArea(radius) Returns the surface area of a sphere having the
# given radius.

# sphereVolume(radius) Returns the volume of a sphere having the given
# radius.

def sphereArea(radius):
    return 4 * math.pi * (radius ** 2)

def sphereVolume(radius):
    return (4/3 * math.pi * (radius ** 3)


# Exercise 6.7

# Write a function to compute the nth Fibonacci number. Use your function
# to solve Programming Exercise 1 6 from Chapter 3.

def fib(n):
    if n == 1 or n == 2:
        return 1
    firstNum = 1
    secondNum = 1
    for i in range (2, n):
        sum = firstNum + secondNum
        firstNum = secondNum
        secondNum = sum
    return sum

print(f"The 2nd Fibonacci number is {fib(2)}")
print(f"The 4th Fibonacci number is {fib(4)}")
print(f"The 6th Fibonacci number is {fib(6)}")


# Exercise 6.11

# Write and test a function to meet this specification.
# squareEach (nums) nums is a list of numbers. Modifies the list by squaring
# each entry.

def squareEach (nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    

testlist1 = [0, -2, 8, 50]
squareEach(testlist1)
print(testlist1)


# Exercise 6.14

# Use the functions from the previous three problems to implement a program
# that computes the sum of the squares of numbers read from a file.

# Your program should prompt for a file name and print out the sum of the
# squares of the values in the file. Hint: Use readlines()

def squareEach (nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
        
def sumList(nums):
    sum = 0
    for item in nums:
        sum += item
    return sum

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])

def file_numbers():
    filename = input("What is the file you're going to open? ")
    with open(filename) as f:
        lines = f.readlines()

    total = 0
    for line in lines:

        # Turn a string of numbers into a list of strings
        stringList = line.split()
        map_object = map(int, stringList)
        
        # Convert to a numberlist, square each item, and then sum all
        list_of_integers = list(map_object)
        
        squareEach(list_of_integers)
        sum = sumList(list_of_integers)
        total += sum

    return total

sum = file_numbers()
print(f"Sum of the square of all numbers in the numbers.txt file is {sum}")
        
"""
