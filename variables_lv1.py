# Python Variables Practice: 30 Tasks
# Instructions: Complete each task by writing the code below the comment.

# --- Level 1: The Basics (Naming & Assignment) ---

# 1. Create a variable named 'city' and assign it the name of your hometown.
# A variable stores data, Here is city and stores text which is a string and should be in quotes.
from nbformat import convert


city = "Capetown"
print("Question 1 - City:", city)
# 2. Create a variable 'age' and set it to your age.
# This is an integer variable because it stores a whole number without decimal points.No quotes.
age = 36
print("Question 2 - Age:", age)

# 3. Assign the value 100 to a variable called 'score'.
# Same as above, this is an integer variable because it stores a whole number without decimal points.No quotes.
score = 100
print("Question 3 - Score:", score)
# 4. Create a variable 'is_sunny' and set it to True.
# Boolean variables strore either true or False values, and they are not in quotes. 
is_sunny = True
print("Question 4 - Is Sunny:", is_sunny)
# 5. Reassign the 'score' variable from task 3 to a new value: 150.
# This is updating the value of the existing variable score and assign new value.
score = 150
print("Question 5 - Updated Score:", score)
# 6. Create two variables, 'x' and 'y', and assign them both the value 5 on a single line.
x = y = 5
print("Question 6 - X:", x, "Y:", y)
# 7. Rename the illegal variable '2_cool' to something valid.
# Variable names cannot start with a number, so we can rename it to 'cool_2' or 'very_cool'.
cool_2 = "very cool"
print("Question 7 - Coolness:", cool_2)
# 8. Create a variable using snake_case (e.g., user_favorite_color).
# Snake case is a naming convention where words are separated by underscores and all letters are lowercase. This makes it easier to read and understand variable names.
user_favourite_color = "Grey"
print("Question 8 - Favourite Color:", user_favourite_color[1:3])
# 9. Swap the values of two variables, a = 10 and b = 20, so a is 20 and b is 10.
# Python allows one to swop values of two variables in a single line using tuple unpacking.
a = 10
b = 20
a , b = b , a
print("Question 9 - A:", a, "B:", b)
#a = 10
#b = 20
#swap = a,b = b,a
#print("question 9:", swap)

# 10. Create a variable 'pi' and assign it the value 3.14159.
# This is a float variable because of decimals.
pi = 3.14159
print("Question 10 - Pi:", pi)

# --- Level 2: Data Types & Conversion ---

# 11. Use the type() function to check the data type of 'age'.
# This is to distinguish the type of data stored in the variable age, which is an integer.
print("Question 11 - Data Type of Age:", type(age))
# 12. Create a string 'price_str = "19.99"' and convert it to a float.
# This is to convert the string representation of a number into an actual numeric data type that can be used for calculations. The float() function is used to convert the string "19.99" into a floating-point number.
#price_str = "19.99"
#price = float(price_str)
#print("Question 12 - Price:", price)
price = "19.99"
converted_price = float(price)
print("question 12;",type(converted_price))
# 13. Convert the float 9.99 into an integer. 
# Converting a float to an integer by removing the decimal. The int() function truncates the decimal part and returns only the whole number portion, which is 9 in this case.
int_value = int(9.99)
print("Question 13 - Integer Value:", int_value)
# 14. Create a variable 'greeting' that combines a string and your 'city' variable.
# Learning to Join strings with variables also known as string concatenation. This allows us to create a new string that includes both the text and the value of the city variable.
#greeting = "Hello, i am from Capetown"
#print("Question 14 - Greeting:", greeting)
#greeting = (city)
#print("question 14:Hello i am from",greeting)
greeting = "Welcome to " + city
print("Question 14 - Greeting:", greeting)
# 15. Use an f-string to print: "I am [age] years old and live in [city]."
# F-strings are a way to format strings in Python, allowing you to embed expressions inside string literals. By prefixing the string with 'f', you can include variables directly within the string using curly braces {}. This makes it easy to create dynamic and readable output.
print(f"I am {age} years old and live in {city}.")

# 16. Create a variable with a long string and use len() to find its length.
long_string = "This is a very long string that I will use to find its length."
print("Question 16 - Length of Long String:", len(long_string))
# 17. Use input() to store a name in a variable called 'user_name'.
# The input() function allows you to take user input from the console. When this line of code is executed, it will prompt the user to enter their name, and whatever they type will be stored in the variable user_name as a string.
user_name = input("Please enter your name: ")
print("Question 17 - User Name:", user_name)
# 18. Ask a user for their birth year, convert to int, and calculate their current age.
# This code prompts the user to enter their birth year, converts the input from a string to an integer using int(), and then calculates the current age by subtracting the birth year from the current year (2026 in this case). The result is stored in the variable current_age.
birth_year = int(input("Please enter your birth year"))
current_age =int(2026- birth_year)
print("Question 18 - Current Age:", current_age)

# 19. Create a boolean variable that checks if 10 is greater than 5.
# Comparing two numbers using the greater than operator (>) and storing the result in a boolean variable. Since 10 is indeed greater than 5, the variable is_greater will be assigned the value True.
#is_greater = 10>5
#print("Question 19 - Is 10 greater than 5?", is_greater)
N = 10<5
print("question 19:", N)
# 20. Create a variable 'nothing' and assign it the value None.
# Output no value or null result.
nothing = None
print("Question 20 - nothing:", nothing)

# --- Level 3: Basic Math with Variables ---

# 21. Create 'length = 10' and 'width = 5'. Calculate 'area' in a new variable.
width = 5
length =10
Area = width * length
print("Qustion 20: ",Area)
# 22. Create 'count = 0'. Increment it by 1 using the += operator.
# This gives us a count and adds 1 to the existing value of count.
#count = 0
#increment += 
count = 1
print(count +5)
# 23. Calculate the remainder of 10 / 3 using the modulo operator (%).
remainder = 10%3
print("Question 23 - Remainder of 10 / 3:", remainder)
# 24. Create 'base = 2' and 'exponent = 3'. Calculate 2 to the power of 3.
base = 2
exponent = 3
power = base ** exponent
print(power)

# 25. Find the average of three variables: test1, test2, and test3.
test1 = 3
test2= 4
test3= 6
average = int((test1 + test2 + test3) /3)
print (average)
# 26. Create 'price = 50'. Calculate a 10% discount and store the final price.
price = 50
discount= price * 0.10
final_price = price- discount
print (final_price)
# 27. Convert a 'fahrenheit' variable to 'celsius' using: (F - 32) * 5/9.
weather = int(input())
#fahrenheit = 500
celcius = int(weather-32* 5/9)
if celcius >= 32:
    print(celcius, "Its Hot")
elif celcius <= 10:
    print(celcius, "Its Cold")

# 28. Create 'seconds = 3660'. Convert this into minutes and remaining seconds.
seconds = 3660
minutes = seconds // 60
remaining_seconds = seconds % 60
print("Question 28 - Minutes:", minutes, ", Remaining Seconds:", remaining_seconds)
# 29. Use a variable to store the result of 10 // 3 (floor division).
floor_division = 10 // 3
print("Question 29 - Floor Division of 10 // 3:", floor_division)
# 30. Create a 'wallet' variable with 100. Subtract three 'purchase' variables from it.
wallet = 100
purchase1 = 20
purchase2 = 15
purchase3 = 30
wallet -= (purchase1 + purchase2 + purchase3)
print("Question 30 - Remaining Wallet Balance:", wallet)