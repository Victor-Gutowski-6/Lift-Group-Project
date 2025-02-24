import time
import json
import sys
from algorithms import (
    printfloors,    
    SafetyChecks,
    AskDirection, # Need to make a feature that lets people request the lift on the floor.
    init_heap,
    insert,
    remove,
    peek,
    build_heap,
    moving
)


#The floors start from floor 1 and go to floor 10. There is no Ground floor.
# We assume the weight limit of the lift is far above any achievable amount.
# We assume each person only chooses ONE floor

heap = init_heap()
floor = 1
people = 0

def My_Algorithm(heap,people): # the F is just to make it easier to tell which the function variable is.
    # Performs safety checks
    while SafetyChecks(people) == False:
        sys.exit() # Terminates the function if not safe
    
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

    # Increases the priority of every unvisited floor by 1 
    for sub in heap:
        sub[0] += 1

    
    people = people + 1 #NEED TO REMEMBER TO RETURN GLOBAL PEOPLE COUNT AT THE END 

    if any(sub[1] == exit for sub in heap):
        repeats = [] 
        # is it possible to add a third like variable? in the heap to log number of requests per floor?
        # may have done that? but now need to figure out how to access and increment it here
    else:
        insert(heap,0,exit, 1) # [priority,exit floor]
    print(heap)



    return heap,people



heap, people = My_Algorithm(heap,people)


# This will control which floor the lift is on, people exiting, and the amoint of people in the lift
def My_Algorithm_exits(heap,floor,people): #floor is just the current floor the lift is on.
    while heap:
        heap = build_heap(heap)
        if not heap:
            break
        next_floor = remove(heap)
        floor = next_floor[1]
        requests = next_floor[2]

        moving(floor,heap)
        people -= requests # handles multiple people leaving the lift???
        print(f"{people} remaining in the lift.")
    
    return heap,floor,people

heap,floor,people = My_Algorithm_exits(heap,floor,people)
