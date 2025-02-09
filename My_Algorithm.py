import time
import json
from algorithms import (
    printfloors,    
    look,
    scan,
    SafetyChecks,
    AskDirection,
    init_heap,
    insert,
    remove,
    peek,
    build_heap
)


#The floors start from floor 1 and go to floor 10. There is no Ground floor.
# We assume the weight limit of the lift is far above any achievable amount.

dictionary = {}
heap = []
floor = 1
people = 0

def My_Algorithm(dictionary,heap,floor,peopleF): # the F is just to make it easier to tell which the function variable is.
    printfloors()
    
    while True:
        try:
            exit = int(input("Which floor would you like to go to?: ")) # exit being the floor they want to exit on.
            if exit <= 10 and exit >= 1:
                break
            else:
                print("Invalid floor. Please select a floor between 1-10.")
        except ValueError:
            print("Invalid input. Please enter a floor.")

    
    peopleF = peopleF + 1
    name = "person" + str(peopleF) #giving the person a 'name' to keep track of in the dictionary??

    dictionary[exit] = 0 #Every value will increase with every stop the lift makes that isnt the exit value.
    print(dictionary)
     






My_Algorithm(dictionary,heap,floor,people)