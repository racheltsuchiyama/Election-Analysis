# Incorporate the random library
import random

# Print Title
#print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
#user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
#for i in options:
    #if user_choice == "r" and computer_choice == options[i]:



#start_number = 0
# Initial variable to track game play
#user_play = "y"
# While we are still playing...
#while user_play == "y":
    # Ask the user how many numbers to loop through
    #user_number = input("How many numbers?")
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    #for i in range(start_number, int(user_number)+ start_number):
        # Print each number in the range
       #print(i)
    # Once complete...
    #start_number = start_number + int(user_number)

   # user_play = input("Continue: (y)es or (n)o? ")

# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join('Resources', 'netflix_ratings.csv')
with open(csvpath, 'r') as csvfile:

    netflix_reader = csv.reader(csvfile)
    headers = next(netflix_reader)
    # Loop through looking for the video
    for row in netflix_reader:
        if row[0] == video:
            print(f"{video} is rated {row[1]} and has user rating {row[5]}")