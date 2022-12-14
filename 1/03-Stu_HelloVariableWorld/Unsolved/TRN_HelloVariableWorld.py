# Create a variable called 'name' that holds a string
name = "John Doe"

# Create a variable called 'country' that holds a string
country = "USA"

# Create a variable called 'age' that holds an integer
age = 30

# Create a variable called 'hourly_wage' that holds an integer
hourly_wage = 15

# Calculate the daily wage for the user
daily_wage = hourly_wage * 8

# Create a variable called 'satisfied' that holds a boolean
satisfied = True

# Print out "Hello <name>!"
print(f"Hello {name}")

# Print out what country the user entered
print(f"{name} is from {country}")

# Print out the user's age
print(f"{name} is {age} years old.")

# With an f-string, print out the daily wage that was calculated
print(f"{name} makes ${daily_wage} per day.")

# With an f-string, print out whether the users were satisfied
print(f"When {name} was asked if they are happy with their daily wage of ${daily_wage} they responded {satisfied}.")
