import json

# This just makes sure everything is good before the lift moves
def SafetyChecks():
    # Opens json file 
    with open('info.json', 'r') as file:
        data = json.load(file)
    
    Weight_Limit = data["TechnicalComponents"]["Weight_Limit"]
    People_Limit = data["TechnicalComponents"]["People_Limit"]
    Total_Weight = 11000 # Create a function that calculates the weight of the people CURRENTLY in the elevator
    Total_People = 11 # Create a function that calculates how many people are in the elevator


    print("⦿The maximum weight limit is 1500kg")
    print("⦿Maximum amount of 10 people allowed at one time\n")

    print("TESTING:")
    print("Maximum Weight:", Total_Weight, "/", Weight_Limit)
    if Total_Weight <= Weight_Limit:
        print("PASSED")
    else:
        print("Failed")
    print("People in lift:", Total_People, "/", People_Limit)
    if Total_People <= People_Limit:
        print("PASSED\n")
    else:
        print("Failed\n")


# This will go to the next requested floor using the look algorithm
def look(floor,queue):
    while queue[0] != floor and queue != []:
        
        if floor >= 10 or queue[-1] < floor:
            print("Lift going down.")
            floor -= 1
            continue

        elif floor <= 1 or queue[0] > floor:
            print("Lift going up.")
            floor += 1
            continue
        
    print("Lift stopping at floor " + floor + ".")
    return floor

# This will go from floor 1 to floor 10 and back until a floor in the queue is found
def scan(floor,queue):
    while queue[0] != floor and queue != []:
        
        if floor >= 10:
            print("Lift going down.")
            floor -= 1
            continue

        elif floor <= 1:
            print("Lift going up.")
            floor += 1
            continue
        
    print("Lift stopping at floor " + floor + ".")
    return floor

def AskDirection():
    direction = input("Would you like to go 'u' or 'd'?: ")
    
    return direction.lower()

"""
Explanation of how the custom algorithm works
"""
def MyAlgorithm():
    print("")

SafetyChecks()