#Collecting the user Personal Data

name = input("Enter your name : ")
hometown=input("Enter your hometown")

while True: #Using while loop and boolean function
    age_input = input("Enter your age: ") #Check if the input is age
    if age_input.isdigit():  # Check if the input is a number
        age = int(age_input) 
        break                 #If the age_input is Right then it will break and stop the loop
    else:                     #if the age is invalid the loop will run again once more until right age is written
        print("Looks like that’s not a number. Please enter your age again!v") #will stop after entering your correct age







    



