"""
    Title: macias_calculator.py
    Author: Andres Macias
    Date: Aug 28 2022
    Description: Week 3 exercise 3.3 Python Variables and Functions
"""


# Create a list of at least 5 hobbies.
myHobbies = ['watching movies','reading','playing video games', 'listening to music', 'Playing with my cats']

# Use a for loop to iterate over the list of hobbies and print them to the console window.
for hobby in myHobbies :
    print(hobby)
    
# create a list for days.
days = ['Monday','Tuesday','Wednesday','Thursday','Friday', 'Saturday', 'Sunday']

# use a for loop to iterate over the list of days and add an if...else statement to display what the day is.
# For saturday and sunday display a message indicating you are off and should enjoy your hobbies. 
# For all other days display a message indicating it is a work day.
for day in days:
    if day == 'Saturday' or day == 'Sunday':
        print("Today is your day off! Enjoy your hobbies!")
    else:
        print('Today is work day.')