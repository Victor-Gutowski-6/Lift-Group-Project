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