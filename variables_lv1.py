# Python Variables Practice: 30 Tasks
# Instructions: Complete each task by writing the code below the comment.

# --- Level 1: The Basics (Naming & Assignment) ---

# 1. Create a variable named 'city' and assign it the name of your hometown.
city = "Capetown"
# 2. Create a variable 'age' and set it to your age.
age = 36
# 3. Assign the value 100 to a variable called 'score'.
score = 100
# 4. Create a variable 'is_sunny' and set it to True.
is_sunny = True
# 5. Reassign the 'score' variable from task 3 to a new value: 150.
score = 150
# 6. Create two variables, 'x' and 'y', and assign them both the value 5 on a single line.
x = y = 5
# 7. Rename the illegal variable '2_cool' to something valid.
cool_2 = "very cool"
# 8. Create a variable using snake_case (e.g., user_favorite_color).
user_favourite_color = "Grey"
# 9. Swap the values of two variables, a = 10 and b = 20, so a is 20 and b is 10.
a = 10
b = 20
a , b = b , a
# 10. Create a variable 'pi' and assign it the value 3.14159.
pi = 3.14159
# --- Level 2: Data Types & Conversion ---

# 11. Use the type() function to check the data type of 'age'.
print(type(age))
# 12. Create a string 'price_str = "19.99"' and convert it to a float.
price_str = "19.99"
# 13. Convert the float 9.99 into an integer. 
int_value = int(9.99)
# 14. Create a variable 'greeting' that combines a string and your 'city' variable.
greeting = "Hello, i am from Capetown"

# 15. Use an f-string to print: "I am [age] years old and live in [city]."
print(f"I am 36 years old and live in Capetown.")
# 16. Create a variable with a long string and use len() to find its length.
long_string = "This is a very long string that I will use to find its length."
print(len(long_string))
# 17. Use input() to store a name in a variable called 'user_name'.
user_name = input("Please enter your name: ")
# 18. Ask a user for their birth year, convert to int, and calculate their current age.
birth_year = int(input("Please enter your birth year: "))
current_age = 2026 - birth_year
print(f"You are {current_age} years old.")

# 19. Create a boolean variable that checks if 10 is greater than 5.
is_greater = 10>5
# 20. Create a variable 'nothing' and assign it the value None.
nothing = None

# --- Level 3: Basic Math with Variables ---

# 21. Create 'length = 10' and 'width = 5'. Calculate 'area' in a new variable.
length = 10
width = 5
area = length * width
# 22. Create 'count = 0'. Increment it by 1 using the += operator.
count = 0
count += 1
# 23. Calculate the remainder of 10 / 3 using the modulo operator (%).
remainder = 10 % 3
# 24. Create 'base = 2' and 'exponent = 3'. Calculate 2 to the power of 3.
base = 2
exponent = 3
power = base ** exponent
# 25. Find the average of three variables: test1, test2, and test3.
test1 = 85
test2 = 90
test3 =85
average = (test1 + test2 + test3)/3
# 26. Create 'price = 50'. Calculate a 10% discount and store the final price.
price = 50
discount = price * 0.10
final_price = price - discount
# 27. Convert a 'fahrenheit' variable to 'celsius' using: (F - 32) * 5/9.
fahrenheit = 100
celsius = (fahrenheit - 32) * 5/9
# 28. Create 'seconds = 3660'. Convert this into minutes and remaining seconds.
seconds = 3660
minutes = seconds // 60
remaining_seconds = seconds % 60
# 29. Use a variable to store the result of 10 // 3 (floor division).
floor_division = 10 // 3
# 30. Create a 'wallet' variable with 100. Subtract three 'purchase' variables from it.
wallet = 100
purchase1 = 20
purchase2 = 15
purchase3 = 30
wallet -= (purchase1 + purchase2 + purchase3)