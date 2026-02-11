#--------------------------------
# Name: Your Name
# Project : Personal information program
# Description: This program stores and displays 
# variable: It consists of 4 variables
# valid input formatted

print("=" *60)
print("Welcome to my Personal Information Program")
print("=" *60)

# Storing my name as a string 

name= "Palukuri Venkata Ramana Murthy"
# Storing my age as a integer
age=21
# Storing my city as a string
city="yellamanchili"
# Storing my hobby as a string
hobby="Coding"
# calculating age in months
age_in_months=age *12

# Function to validate non-empty input
def get_valid_input(prompt):
    while True:
        user_input = input(prompt).strip() 
        if user_input == "":
            print("Input cannot be empty. Please try again.")
        else:
            return user_input.title()  

#Asking user for favorite food 
favorite_food=get_valid_input=("Biriyani")
# Asking user for favorite color
favorite_color=get_valid_input=("Black")


# formatted Information
print("\n" + "-" * 50)
print("PERSONAL INFORMATION")
print("-" * 60)

print(f"Name           : {name.upper()}")
print(f"Age            : {age} years")
print(f"Age in Months  : {age_in_months} months")
print(f"City           : {city.title()}")
print(f"Hobby          : {hobby.capitalize()}")
print(f"Favorite Food  : {favorite_food}")
print(f"Favorite Color : {favorite_color}")

print("-" * 60)

# Step 6: Goodbye message
print("\nThank you for using the program!")
print("Have a great day! 😊")
print("=" * 60)