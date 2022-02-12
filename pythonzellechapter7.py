# Chapter 7 Exercises

"""
# Exercise 7.1

# Many companies pay time-and-a-half for any hours worked above 40 in a
# given week. Write a program to input the number of hours worked and
# the hourly rate and calculate the total wages for the week.

def total_weekly_pay():

    hourly_rate = float(input("What is the employee's hourly wage? "))
    hours_worked = float(input("How many hours did the employee work? "))

    if hours_worked > 40.0:
        pay = (hours_worked - 40) * (1.5 * hourly_rate) + (40 * hourly_rate)
    else:
        pay = hourly_rate * hours_worked

    print(f"The employee earned ${pay:.2f}")

total_weekly_pay()

# Exercise 7.5

# The body mass index (BMI) is calculated as a person's weight (in pounds)
# times 720, divided by the square of the person's height (in inches).

# A BMI in the range 19-25, inclusive, is considered healthy. Write a
# program that calculates a person's BMI and prints a message telling
# whether they are above, within, or below the healthy range.



def calculate_BMI():

    # Get person's weight and height in pounds/inches, respectively
    weight = float(input("Please enter your weight in pounds: "))
    height = float(input("Please enter your height in inches: "))

    bmi = (weight * 720) / (height ** 2)

    if bmi > 25.0:
        print(f"Your BMI is {bmi}; you are fat.")
    elif bmi < 19.0:
        print(f"Your BMI is {bmi}; you are underweight.")
    else:
        print(f"Your BMI is {bmi}; you are within a healthy weight range.")

calculate_BMI()

"""


