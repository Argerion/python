import math

"""

# Chapter 3 Exercises

# Exercise 3.1
# Write a program to calculate the volume and surface area of a sphere from
# its radius, given as input.

def calculate_sphere_vol_and_surface_area():
    radius = float(input("Enter the sphere's radius: "))
    vol = (4/3) * math.pi * math.pow(radius, 3)
    area = 4 * math.pi * (radius ** 2)
    print(f"A sphere with radius {radius} will have a volume of {vol:.3f} " +
          f"cube units and a surface area of {area:.3f} square units.")

calculate_sphere_vol_and_surface_area()


# Exercise 3.2

# Write a program that calculates the cost per square inch of a circular pizza,
# given its diameter and price. The formula for area is A = pi * radius ** 2

def calculate_cost_per_sq_inch():
    diameter = float(input("Enter the pizza's diameter in inches: "))
    price = float(input("Enter the price of the entire pizza in dollars: "))
    area = math.pi * ((diameter / 2) ** 2)
    price_per_sq = price / area
    print(f"Your pizza costs ${price_per_sq:.2f} for every square inch.")

calculate_cost_per_sq_inch()


# Exercise 3.3

# Write a program that computes the molecular weight of a carbohydrate (in
# grams per mole) based on the number of hydrogen, carbon, and oxygen
# atoms in the molecule. The program should prompt the user to enter the
# number of hydrogen atoms, the number of carbon atoms, and the number
# of oxygen atoms. The program then prints the total combined molecular
# weight of all the atoms based on these individual atom weights.

def calculate_molecular_weight():
    hydrogen = int(input("Enter the number of hydrogen atoms: "))
    carbon = int(input("Enter the number of carbon atoms: "))
    oxygen = int(input("Enter the number of oxygen atoms: "))

    weight = hydrogen * 1.00794 + carbon * 12.0107 + oxygen * 15.9994

    print(f"The weight of your molecule is {weight} grams/mole.")

calculate_molecular_weight()


# Exercise 3.4

# Write a program that determines the distance to a lightning strike based on
# the time elapsed between the flash and the sound of thunder. The speed
# of sound is approximately 1100 ft/sec and 1 mile is 5280 ft.

def lightning_distance():
    time = float(input("How many seconds after the flash did the sound " +
                       "of thunder roar? "))
    distance = 1100 * time / 5280
    print(f"The lightning struck {distance} miles away based on the time\n" +
          f"elapsed between the flash and the thunder.")
    
lightning_distance() 


# Exercise 3.5

# The Konditorei coffee shop sells coffee at $10.50 a pound plus the cost
# of shipping. Each order ships for $0.86 per pound + $1.50 fixed cost for
# overhead. Write a program that calculates the cost of an order.

def coffee_cost():
    weight = float(input("How many pounds of coffee will you order? "))
    cost = 1.50 + weight * (10.50 + 0.86)
    print(f"Your {weight} pound coffee order will cost ${cost:.2f}")

coffee_cost()


# Exercise 3.6

# Write a program that calculates the slope of a line through two
# (non-vertical) points entered by the user.

def slope():
    first_pt = list(map(float, input("Enter the coordinates for the first point, " +
                   "separated by a comma: ").split(",")))
    second_pt = list(map(float, input("Enter the coordinates of the second point, " +
                   "separated by a comma: ").split(",")))
    slope = (second_pt[1] - first_pt[1]) / (second_pt[0] - first_pt[0])
    print(f"The slope of the line connecting ({first_pt[0]}, {first_pt[1]}) "
          + f"with ({second_pt[0]}, {second_pt[1]}) is {slope}.")

slope()


# Exercise 3.7

# Write a program that calculates the distance between 2 points

def distance():
    first_pt = list(map(float, input("Enter the coordinates for the first point, " +
                   "separated by a comma: ").split(",")))
    second_pt = list(map(float, input("Enter the coordinates of the second point, " +
                   "separated by a comma: ").split(",")))
    distance = math.sqrt((second_pt[0] - first_pt[0]) ** 2 +
                         (second_pt[1] - first_pt[0]) ** 2)
    print(f"The distance between ({first_pt[0]}, {first_pt[1]}) "
          + f"and ({second_pt[0]}, {second_pt[1]}) is {distance}.")

distance()


# Exercise 3.8

# Write a program that prompts the user for a 4-digit year and then outputs
# the value of the Gregorian calendar epact.
# epact = (8 + (C//4) - C + ((8C + 13)//25) + 11(year % 19)) %30
# C = year // 100

def epact():
    year = int(input("Enter the Gregorian Calendar year: "))
    C = year // 100
    epact = (8 + (C // 4) - C + ((8 * C + 13) // 25) + 11 * (year % 19)) % 30
    print(epact)

epact()



# Exercise 3.9

# Write a program to calculate the area of a triangle given the length of its
# three sides-a, b, and c.

def calc_triangle_area():
    lengths = list(map(float, input("Enter the 3 side lengths for the triangle" +
                                    ", separated by a comma: ").split(",")))
    s = (lengths[0] + lengths[1] + lengths[2]) / 2
    area = math.sqrt(s * (s - lengths[0]) * (s - lengths[1])
                     * (s - lengths[2]))
    print(f"A triangle with the side lengths {lengths} has an area of {area}.")

calc_triangle_area()    



# Exercise 3.10

# Write a program to determine the length of a ladder required to reach a
# given height when leaned against a house. The height and angle of the
# ladder are given as inputs.
# Be sure to convert angle (default is in degrees) to radians.

def ladder_length():
    house = float(input("Enter the height of the house in feet: "))
    angle = float(input("Enter the angle between the ladder and" +
                        " the base in degrees: "))
    radians = math.pi / 180 * angle
    ladder_height = house / math.sin(radians)
    print(f"A house {house} feet tall would require a {ladder_height:.3f} " +
          f"feet ladder \nat an incline of {angle} degrees.")

ladder_length()


# Exercise 3.11

# Write a program to find the sum of the first n natural numbers. n is provided
# by the user

def natural_numbers_sum():
    print("Note that natural numbers are positive integers, e.g. 1, 2, ,...")
    n = int(input("How many natural numbers would you like to sum? "))
    sum = 0
    for i in range (1, n + 1, 1):
        sum += i
    print(f"The sum of the first {n} natural numbers is {sum}")

natural_numbers_sum()



# Exercise 3.12

# Write a program to find the sum of the cubes of the first n natural numbers
# where the value of n is provided by the user.

def natural_num_cubic_sum():
    n = int(input("How many cubes of natural numbers would you like to sum? "))
    sum = 0
    for i in range (1, n + 1, 1):
        sum += i ** 3
    print(f"The sum of the cubes of the first {n} natural numbers is {sum}")

natural_num_cubic_sum()


# Exercise 3.13

# Write a program to sum a series of numbers entered by the user. The
# program should first prompt the user for how many numbers are to be
# summed. The program should then prompt the user for each of the numbers
# in turn and print out a total sum after all the numbers have been
# entered. Hint: Use an input statement in the body of the loop.

def custom_sum():
    n = int(input("How many numbers would you like to sum? "))
    sum = 0.0
    for i in range(n):
        figure = float(input("Enter the next number to add to the total: "))
        sum += figure
    print(f"The total is {sum}")

custom_sum()



# Exercise 3.14

# Write a program that finds the average of a series of numbers entered by
# the user. As in the previous problem, the program will first ask the user
# how many numbers there are. Note: The average should always be a float,
# even if the user inputs are all ints.

def avg():
    n = int(input("How many numbers would you like to average? "))
    sum = 0.0
    for i in range(n):
        figure = float(input("Enter the next number: "))
        sum += figure
    average = sum / n
    print(f"The average of these numbers is {average}")

avg()


# Exercise 3.15

# Write a program that approximates the value of pi by summing the terms
# of this series: 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + . . . The program should
# prompt the user for n, the number of terms to sum, and then output the
# sum of the first n terms of this series. Have your program subtract the
# approximation from the value of math. pi to see how accurate it is.

def pi_approximate():
    n = int(input("How many numbers in the series would you like to use " +
                  "to approximate pi? "))
    pi_estimate = 0
    sign_changer = 1 # Keeps track of whether to add or subtract the next in series
    for i in range(1, n * 2, 2):
        pi_estimate += sign_changer * 4 / i
        sign_changer *= -1
    print(f"Based on {n} inputs into the series, pi comes out to {pi_estimate}")

pi_approximate()
                        

# Exercise 3.16

# A Fibonacci sequence is a sequence of numbers where each successive
# number is the sum of the previous two. The classic Fibonacci sequence
# begins: 1, 1, 2, 3, 5, 8, 13, . . . . Write a program that computes the nth
# Fibonacci number where n is a value input by the user. For example, if
# n = 6, then the result is 8.

def fib_num():
    n = int(input("How many Fibonacci numbers would you like to traverse? "))

    if n == 1:
        print("The first Fibonacci number is 1")
    elif n == 2:
        print("The second Fibonacci number is 1")
    else:
        first = 1
        second = 1
        for i in range(n - 2):
            next_fib = first + second
            first = second
            second = next_fib
            
        print(f"Fibonacci #{n} is {next_fib}.")

fib_num()



# Exercise 3.17

# Write a program that implements Newton's method. The program
# should prompt the user for the value to find the square root of (x) and
# the number of times to improve the guess. Starting with a guess value
# of x/2, your program should loop the specified number of times applying
# Newton's method and report the final value of guess. You should also
# subtract your estimate from the value of math. sqrt (x) to show how close
# it is.

def newtons_method():
    x = float(input("What number are you trying to estimate the sq root of? "))
    guess = float(input("What is your estimate of the number's square root? "))
    n = int(input("How many iterations do you want to apply Newton's method? "))

    for i in range(n):
        guess = (guess + (x / guess)) / 2.0

    root = math.sqrt(x)
    print()
    print(f"Newton's method yielded {guess} after {n} iterations")
    print(f"The actual square root of {x} is {root}.")
    print(f"The difference is {root - guess}")

newtons_method()

"""
