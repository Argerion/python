# Chapter 2 Exercises from Python textbook by Zelle


# Exercise 2.1
# A user-friendly program should print an introduction that tells the user
# what the program does. Modify the program (Section 2.2) to
# print an introduction.

def c_to_f():
    print("This program converts Celsius to Fahrenheit degrees.")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print ("The temperature is", fahrenheit, "degrees Fahrenheit.")

c_to_f()

# Exercise 2.2

# On many systems with Python, it is possible to run a program by simply
# clicking (or double-clicking) on the icon of the program file. If you are
# able to run the convert . py program this way, you may discover another
# usability issue. The program starts running in a new window, but as soon
# as the program has finished, the window disappears so that you cannot
# read the results. Add an input statement at the end of the program so
# that it pauses to give the user a chance to read the results. Something like
# this should work:
# input ("Press the <Enter> key to quit.")

# Answer: This simply involves print("Press the <Enter> key to quit.") A more
# detailed answer would do error checking to ensure only the Enter key allows
# the program to terminate.

# Exercise 2.3

# Modify the avg2.py program (Section 2.5.3) to find the average of three
# exam scores.

print()
def avg():
    print("This program computes the average of three exam scores.")
    score1, score2, score3 = eval(input("Enter three scores separated " +
                                         "by a comma: "))
    average = (score1 + score2 + score3) / 3.0
    print ("The average of the scores is: ", average)

avg()

# Exercise 2.4

# Modify the convert. py program (Section 2.2) with a loop so that it executes
# 5 times before quitting. Each time through the loop, the program
# should get another temperature from the user and print the converted
# value.

# Solution: Add a simple statement after the print introduction and nest
# the program inside the loop
# for i in range(5):



# Exercise 2.5

# Modify the convert.py program (Section 2.2) so that it computes and
# prints a table of Celsius temperatures and the Fahrenheit equivalents every
# 10 degrees from 0°C to 100°C.

print()

def c_to_f_table():
    for i in range(0, 101, 10):
        f = (9/5 * i) + 32
        print("\t" + str(i) + "\t | \t" + str(f) + "\t")
        print("\t" + "---------------------" + "\t")

c_to_f_table()



# Exercise 2.6

# Modify the futval.py program (Section 2.7) so that the number of years
# for the investment is also a user input. Make sure to change the final
# message to reflect the correct number of years.

def futval():
    print ("This program calculates the future value")
    print ("of an investment after X number of years.")
    years = int(input("Enter the number of years: "))
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    for i in range (years):
        principal *= (1 + apr)
    print(f"The value of your initial investment " + 
          f"after {years} years is ${principal:.2f}")

futval()


# Exercise 2.7

# Suppose you have an investment plan where you invest a certain fixed
# amount every year. Modify futval.py to compute the total accumulation
# of your investment. The inputs to the program will be the amount to invest
# each year, the interest rate, and the number of years for the investment.

def futval():
    print ("This program calculates the future value")
    print ("of an investment after X number of years.")
    years = int(input("Enter the number of years: "))
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    fixed_amount = float(input("Enter the fixed investment amount per period: "))
    for i in range (years):
        principal *= (1 + apr)
        principal += fixed_amount
    principal -= fixed_amount # Discounting the final year fixed_amount as it doesn't apply
    print(f"The value of your initial investment " + 
          f"after {years} years is ${principal:.2f}")

futval()



# Exercise 2.8

# As an alternative to APR, the interest accrued on an account is often described
# in terms of a nominal rate and the number of compounding periods.
# For example, if the interest rate is 3% and the interest is compounded
# quarterly, the account actually earns 0.75% interest every 3 months.
# Modify the futval.py program to use this method of entering the
# interest rate. The program should prompt the user for the yearly rate
# (rate) and the number of times that the interest is compounded each year
# (periods). To compute the value in ten years, the program will loop 10 *
# periods times and accrue rate/period interest on each iteration.

def futval():
    print ("This program calculates the future value")
    print ("of an investment after X number of years.")
    years = int(input("Enter the number of years: "))
    periods = int(input("Enter the number of periods per year that interest is compounded: "))
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    fixed_amount = float(input("Enter the fixed investment amount per period: "))
    for i in range (years * periods):
        principal *= (1 + apr / periods)
        principal += fixed_amount
    principal -= fixed_amount # Discounting the final year fixed_amount as it doesn't apply
    print(f"The value of your initial investment " + 
          f"after {years} years is ${principal:.2f}")

futval()



# Exercise 2.9
# Write a program that converts temperatures from Fahrenheit to Celsius.

def f_to_c():
    fahrenheit = float(input("Enter the degrees Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit} degrees Fahrenheit is equivalent to {celsius} degrees" +
          f" Celsius.")

f_to_c()



# Exercise 2.10
# Write a program that converts distances measured in kilometers to miles.
# One kilometer is approximately 0.62 miles.

def kilo_to_miles():
    kilos = float(input("Enter the number of kilometers: "))
    miles = kilos * 0.62
    print(f"{kilos} kilometers is approximately {miles} miles.")


kilo_to_miles()




# Exercise 2.11
# Write a program to do a conversion of your own choosing

def minutes_to_days():
    minutes = float(input("Enter the number of minutes: "))
    days = minutes / (60 * 24)
    print(f"{minutes} minutes is approximately {days} days.")

minutes_to_days()



# Exercise 2.11
# Write an interactive Python calculator program. The program should allow
# the user to type a mathematical expression, and then print the value of the
# expression.

# Answer: There are two ways to do this. The first way is to use
# eval(input("Enter your expression: ")) and let Python handle it.
# The second way, much safer, is to use this:
# expression = sum(map(int, re.findall(r'[+-]?\d+', test_str)))
# You have to import regex 
