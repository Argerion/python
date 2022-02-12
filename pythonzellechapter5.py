from tabulate import tabulate

"""

# Chapter 5 Exercises

# Exercise 5.1

# As discussed in the chapter, string formatting could be used to simplify the
# dateconvert.py program. Go back and redo this program making use
# of the string-formatting method.

def date_convert():
    # get the date
    dateStr = input("Enter a date (mm/dd/yyyy): ")
    
    # split into components
    monthStr , dayStr , yearStr = dateStr.split ("/")
    
    # convert monthStr to the month name
    months = ["January" , "February" , "March" , "April" ,
              "May" , "June" , "July" , "August" , "September" ,
              "October" , "November" , "December"]

    monthStr = months[int(monthStr) - 1]
    
    # output result in month day, year format
    print(f"The converted date is {monthStr} {dayStr}, {yearStr}")

date_convert()



# Exercise 5.2

# A certain CS professor gives 5-point quizzes that are graded on the scale
# 5-A, 4-B, 3-C, 2-D, 1-F, 0-F. Write a program that accepts a quiz score as
# an input and prints out the corresponding grade.
    
def quiz_conversion():

    score = int(input("Enter the quiz score (0 - 5): "))

    grades = ["F", "F", "D", "C", "B", "A"]

    grade = grades[score]
    print(f"You earned a {grade} on your quiz.")

quiz_conversion()


# Exercise 5.3

# A certain CS professor gives 100-point exams that are graded on the scale
# 90- 100:A, 80-89:B, 70-79:C, 60-69:D, <60:F. Write a program that accepts
# an exam score as input and prints out the corresponding grade.

def grade_conversion():

    score = int(input("Enter the exam score (0 - 100): "))

    grades = ["A", "B", "C", "D", "F"]

    if score >= 90:
        print(f"You earned a {grades[0]} on your exam.")
    elif score >= 80:
        print(f"You earned a {grades[1]} on your exam.")
    elif score >= 70:
        print(f"You earned a {grades[2]} on your exam.")
    elif score >= 60:
        print(f"You earned a {grades[3]} on your exam.")
    else:
        print(f"You earned a {grades[4]} on your exam.")

grade_conversion



# Exercise 5.4

# Write a program that allows the user to
# type in a phrase and then outputs the acronym for that phrase. Note : The
# acronym should be all uppercase, even if the words in the phrase are not
# capitalized.

def acronym():

    phrase = input("Enter the phrase you'd like to form an acronym from: ")

    words = phrase.split()
    first_letters = ""
    
    for word in words:
        first_letters += word[0]

    first_letters = first_letters.upper()

    print(f"Your acronym is {first_letters}")

acronym()



# Exercise 5.5

# Numerologists claim to be able to determine a person's character traits
# based on the "numeric value" of a name. The value of a name is determined
# by summing up the values of the letters of the name where "a" is
# 1 "b" is 2 "c" is 3 up to "z" being 26 For example the name "Zelle" ' ' ' . '
# would have the value 26 + 5 + 12 + 12 + 5 = 60 (which happens to be a
# very auspicious number, by the way). Write a program that calculates the
# numeric value of a single name provided as input.

def numeric_name_value():

    name = input("Please enter a name with no whitespace: ")

    numeric_value = 0
    
    for char in name:
        numeric_value += ord(char.lower()) - 96

    print(f"The numeric value of {name} is {numeric_value}")

numeric_name_value()



# Exercise 5.6

# Expand your solution to the previous problem to allow the calculation of
# a complete name such as '3"ohn Marvin Zelle" or '3"ohn Jacob Jingleheimer
# Smith." The total value is just the sum of the numeric values of all the
# names.

def numeric_name_value():

    name = input("Please enter a name; spaces are allowed: ")

    numeric_value = 0
    
    for char in name:
        if char != ' ':
            numeric_value += ord(char.lower()) - 96

    print(f"The numeric value of {name} is {numeric_value}")

numeric_name_value()
        


# Exercise 5.7

# A Caesar cipher is a simple substitution cipher based on the idea of shifting
# each letter of the plaintext message a fixed number (called the key) of
# positions in the alphabet. For example, if the key value is 2, the word
# "Sourpuss" would be encoded as "Uqwtrwuu." The original message can
# be recovered by "reencoding" it using the negative of the key.

# Write a program that can encode and decode Caesar ciphers. The input
# to the program will be a string of plaintext and the value of the key.
# The output will be an encoded message where each character in the original
# message is replaced by shifting it key characters in the Unicode character
# set. For example, if ch is a character in the string and key is the
# amount to shift, then the character that replaces ch can be calculated as:
# chr (ord (ch) + key)

def caesar_cipher():

    key = int(input("Enter the value of the encoding key: "))
    word = input("Enter the word you would like to encode: ")

    new_word = ""

    for char in word:
        new_char = chr(ord(char) + key)
        new_word += new_char

    print(f"Your encoded word is {new_word}")

    word = input("Enter the word you would like to decode: ")
    key = int(input("Enter the value of the decoding key: "))

    new_word = ""

    for char in word:
        new_char = chr(ord(char) - key)
        new_word += new_char

    print(f"Your decoded word is {new_word}")

caesar_cipher()


# Exercise 5.8

# One problem with the previous exercise is that it does not deal with the
# case when we "drop off the end" of the alphabet. A true Caesar cipher
# does the shifting in a circular fashion where the next character after "z" is
# "a." Modify your solution to the previous problem to make it circular. You
# may assume that the input consists only of letters and spaces. Hint : Make
# a string containing all the characters of your alphabet and use positions in
# this string as your code. You do not have to shift "z" into "a"; just make
# sure that you use a circular shift over the entire sequence of characters in
# your alphabet string.

def caesar_cipher_improved():

    key = int(input("\nWhat is the shift value key? "))

    # Get the message from the user to encode
    message = input("\nWhat is the message? ")

    # string of all characters, lowercase
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    encoded_message = ""
    
    for i in range(len(message)):

        # non-alphabets remain the same
        if not message[i].isalpha(): 
            encoded_message += message[i]
        else:
            alphabetValue = ord(message[i].lower()) - 97
            cipherValue = (alphabetValue + key) % 26
            if message[i].isupper():
                encoded_message += (alphabet[cipherValue].upper())
            else:
                encoded_message += alphabet[cipherValue]
            
    print(encoded_message)

caesar_cipher_improved()
    


# Exercise 5.9

# Write a program that counts the number of words in a sentence entered
# by the user.

def word_count():

    sentence = input("Please enter a sentence: ")

    words = sentence.split()

    print(f"Your sentence has {len(words)} words.")

word_count()


# Exercise 5.10

# Write a program that calculates the average word length in a sentence
# entered by the user.

def avg_word_length():

    sentence = input("Please enter a sentence: ")

    words = sentence.split()

    total_chars = 0
    
    for word in words:
        total_chars += len(word)

    avg_length = total_chars / len(words)

    print(f"The average word length is {avg_length}")

avg_word_length()


# Exercise 5.11

# Write an improved version of the chaos.py program from Chapter 1 that
# allows a user to input two initial values and the number of iterations,
# and then prints a nicely formatted table showing how the values change
# over time.

def chaos_table():

    x = float(input("Enter a number between 0 and 1: "))
    y = float(input("Enter a number between 0 and 1: "))

    # Save these for header purposes
    original_x = x
    original_y = y
    
    rows = []
    
    for i in range(1, 11, 1):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        rows.append([i, "{0}".format(x), "{0}".format(y)])

    print()
    print(tabulate(rows, headers=["Index", original_x, original_y],
                   colalign=("center", "center"), numalign="center"))

chaos_table()


# Exercise 5.12

# Write an improved version of the futval.py program from Chapter 2.
# Your program will prompt the user for the amount of the investment, the
# annualized interest rate, and the number of years of the investment. The
# program will then output a nicely formatted table that tracks the value of
# the investment year by year.



def future_value_table():
    
    principal = float(input("Enter the initial principal: "))
    added_investment = float(input("Enter additional amount" +
                                  " invested per year: "))
    apr = float(input("Enter the annual interest rate in decimal format: "))
    years = int(input("Enter the number of years: "))

    data = []
    
    for i in range(years + 1):
        data.append([i, "${:,.2f}".format(principal)])
        principal *= (1 + apr)
        principal += added_investment

    print("")
    print(tabulate(data, headers=["Year", "Value"],
                   colalign=("center", "center"), numalign="center"))

future_value_table()

"""

