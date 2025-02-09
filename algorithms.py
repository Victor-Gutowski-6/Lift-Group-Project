import json
from main import elevator

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


# This just makes sure everything is good before the lift moves
def SafetyChecks(total_people):
    # Opens json file 
    with open('info.json', 'r') as file:
        data = json.load(file)
    
    People_Limit = data["TechnicalComponents"]["People_Limit"]
    Total_People = elevator


    print("Maximum amount of 10 people allowed at one time\n")

    print("TESTING:")
    print("People in lift:", Total_People, "/", People_Limit)
    if Total_People <= People_Limit:
        print("PASSED\n")
        return True
    else:
        print("Failed\n")
        return False

    


def AskDirection():
    direction = input("Would you like to go 'u' or 'd'?: ") 
    return direction.lower()


def init_heap():
    heap = []
    return heap


def heapify_up(heap,index):
    while index > 0:
        parent = (index - 1) // 2
        if heap [parent] > heap [index]:

            x = heap[parent]
            heap[parent] = heap[index]
            heap[index] = x

            index = parent
        else:
            break


def heapify_down(heap,index):
    size = len(heap)
    while True:
        smallest = index
        L_child = 2*index + 1
        R_child = 2*index + 2

        if L_child < size and heap[L_child] < heap[smallest]:
            smallest = L_child

        if R_child < size and heap[R_child] < heap[smallest]:
            smallest = R_child

        if smallest != index:

            x = heap[index]
            heap[index] = heap[smallest]
            heap[smallest] = x

            index = smallest

        else:
            break

# the priortiy will be input looking something like dictionary[value[i]]
def insert(heap,priority_level): # The priority will be a dictionary value; the floor will be the key
    heap.append(priority_level)
    heapify_up(heap, heap[-1])  #There may be some issues with calling the function, look into this if any errors occur 


def is_empty(heap):
    return len(heap) == 0 


def remove(heap):
    if is_empty(heap):
        return None

    top_value = heap[0]

    x = heap[0]
    heap[0] = heap[-1]
    heap[-1] = x
    heap.pop()

    heapify_down(heap,0)
    return top_value


def peek(heap):
    if is_empty(heap):
        return None
    
    return heap[0]


def build_heap(heap): # Note: this isnt a heap yet, just an unsorted array
    for i in range(len(heap)//2 ,-1,0): # 0 could be -1?
        heapify_down(heap,i)
    return heap