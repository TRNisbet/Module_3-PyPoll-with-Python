# Initial variable to track game play
user_play = "y"

# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    user_input = int(input("How many numbers do you want to loop through? "))
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for x in range(user_input):
        # Print each number in the range
       print(x)
       print("********") 
       #the postion of the above print statement will determine where it displays 

    # Once complete...
 