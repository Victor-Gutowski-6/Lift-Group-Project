import json
import time


class MYLIFT:
    
    # Initalising the variables
    def __init__(self, start_floor=0):
        self.heap = []
        self.current_floor = start_floor    # This is both for MYLIFT1 & MYLIFT2
        self.direction = "up"               # This is both for MYLIFT1 & MYLIFT2
        self.FIFO_tracker = 0   # This is actually for the heap algorithm
        self.passenger_hashmap = {}

        self.queue = []

    
    def add_passenger(self,floor):
        if floor in self.passenger_hashmap:
            self.passenger_hashmap[floor] += 1  # Add 1 to people exiting on that floor, if floor already exists
        else:
            self.passenger_hashmap[floor] = 1   # If floor doesnt already exist then make the floor exist

    
    def remove_passengers(self):
        exiting_passangers = self.passenger_hashmap.pop(self.current_floor, 0)
        if exiting_passangers > 0:
            print(f"{exiting_passangers} passenger(s) got off at floor {self.current_floor}.\n")
        return exiting_passangers


    def calculate_priority(self,floor):
        if (self.direction == 'up' and floor >= self.current_floor) or (self.direction == 'down' and floor <= self.current_floor):
                direction_priority = 0
        else:
             direction_priority = 1

        distance = abs(floor - self.current_floor)
        return direction_priority*1000 + distance   # Multiplied by 100 to make sure it finishes requests in one direction before moving onto the other

    
    # This function moves elements up to maintain the min heap
    def heapify_up(self,index):
        while index > 0:
            parent = (index-1) // 2
            if self.heap[index] < self.heap[parent]:
                placeholder = self.heap[parent]
                self.heap[parent] = self.heap[index]
                self.heap[index] = placeholder

                index = parent
            
            else:
                 break
    
    
    # This function moves elements down to maintain min heap
    def heapify_down(self,index):
        size = len(self.heap)
        while True:
            smallest = index
            L_child = 2*index + 1
            R_child = 2*index + 2

            if (L_child < size) and (self.heap[L_child] < self.heap[smallest]):
                smallest = L_child
            if (R_child < size) and (self.heap[R_child] < self.heap[smallest]):
                smallest = R_child
            if smallest != index:
                placeholder = self.heap[smallest]
                self.heap[smallest] = self.heap[index]
                self.heap[index] = placeholder

                index = smallest 
            
            else:
                break

    
    def add_request(self,floor):
        self.FIFO_tracker += 1  # Makes sure floors arent ignored for too long
        priority = self.calculate_priority(floor)
        self.heap.append((priority, self.FIFO_tracker, floor))  # The request is stores as a tupple in that format
        self.heapify_up(len(self.heap) - 1)
        print(f"Request successfully added for floor {floor}.\n")
    

    def get_next_floor(self):
        with open('info.json', 'r') as file:
            data = json.load(file)    
        total_floors = data["TechnicalComponents"]["NumberOfFloors"]
        
        if not self.heap:
            return total_floors // 2    # Send the lift into the middle so it can respond to its next request the fastest
        
        # Swapping the first and last element in the heap
        placeholder = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap[-1] = placeholder

        # Removing the last element
        next_floor = self.heap.pop()

        # Restoring the heap property if it's not empty
        if self.heap:
            self.heapify_down(0)

        return next_floor[-1] if isinstance(next_floor, tuple) else next_floor  # This checks if the the next_floor is a tupple or a single value, it will be a tupple if the FIFO_tracker is being used.
    
    '''
    def direction_checker_for_lift():
    Do we even need this function? I dont think its used
    '''


    def is_empty(self):
        return len(self.heap) == 0

    # THE NEXT FEW FUNCTIONS ARE FOR THE MYLIFT2 ALGORITHM! #

    def FIFO_add_request(self,floor):
        
        self.queue.append(floor)
        print(f"Request added for floor {floor}")


    def FIFO_is_empty(self):
        return len(self.queue) == 0
    
    
    def FIFO_get_next_floor(self):
        with open('info.json', 'r') as file:
            data = json.load(file)    
        total_floors = data["TechnicalComponents"]["NumberOfFloors"]
        
        if not self.queue:
            return total_floors // 2
        
        return self.queue.pop(0)

        



class General:  # This will be used in every algorithm so we dont care about its time complexity

    @staticmethod
    def print_floors():
        with open('info.json', 'r') as file:
            data = json.load(file)
        total_floors = data["TechnicalComponents"]["NumberOfFloors"]
        print("\n")
        for f in range(1,total_floors+1):
            print(f,"\n")
    
    @staticmethod
    def safety_checks(people_in_lift):
        with open('info.json', 'r') as file:
            data = json.load(file)
        people_limit = data["TechnicalComponents"]["People_Limit"]

        print(f"Maximum amount of {people_limit} people allowed at one time \n")
        print("TESTING:")
        print("People in lift:", people_in_lift, "/", people_limit) 
        if people_in_lift <= people_limit:
            print("PASSED! \n")
            return True
        else:
            print("Failed :( \n")
            return False
        
    
    @staticmethod
    def moving(current_floor, target_floor, delay=3):
        step = 1 if target_floor > current_floor else -1    # This is just so it doesn't repeat the floor its already on and enforces the direction its going in
        for floor in range(current_floor + step, target_floor + step, step):
            time.sleep(delay)
            print(f"The lift is now on floor: {floor}")
    
    
    @staticmethod
    def requests(lift,people_in_lift):
        with open('info.json', 'r') as file:
            data = json.load(file)
        total_floors = data["TechnicalComponents"]["NumberOfFloors"]
        people_limit = data["TechnicalComponents"]["People_Limit"]

        try:
            Internal_GettingOn = '0'
            while Internal_GettingOn.lower() != 'yes' and Internal_GettingOn.lower() != 'no':
                Internal_GettingOn = input("Are there people getting on, on this floor? ('yes' or 'no'): ")
                continue
            if Internal_GettingOn.lower() == 'yes':
                Internal_People = int(input("How many people are getting on?: "))
                
                while True:
                    if not General.safety_checks(people_in_lift + Internal_People):
                        print("Doors reopening - Too many people!\n")
                        break
                    else:
                        total_people = people_in_lift + Internal_People

                    for i in range(1,Internal_People+1):
                        while True:
                            try:
                                Internal_Floor = int(input(f"Which floor is person {i} going to?: "))
                                if Internal_Floor < 0 or Internal_Floor > total_floors:
                                    print(f"Floor must be non negative and below floor {total_floors}" )
                                    continue
                                lift.add_request(Internal_Floor)
                                lift.add_passenger(Internal_Floor)
                                break
                            except ValueError:
                                print("Invalid floor number. Please enter an integer.\n")
                    
                    people_in_lift = total_people
                    print(f"{Internal_People} people got on. Total people now: {total_people}\n")
                    break
            
            else:
                print("No people boarding on this floor.\n")    

        except ValueError:
            print("Invalid input. Please enter number values where required.")
        

        try:
            if people_in_lift <= people_limit:  # Making sure there's even more space for more requests
                External_GettingOn = '0'
                while External_GettingOn != 'yes' and External_GettingOn != 'no':
                    External_GettingOn = input("Are there people requesting the lift from other floors? ('yes' or 'no'): ")
                    continue
                if External_GettingOn == 'yes':
                    while True:
                        try:
                            External_People = int(input("How many floors have people waiting?: "))
                            break
                        except ValueError:
                            print("Invalid input. Please enter a number.\n")
                    
                    for f in range(1,External_People+1):
                        if people_in_lift >= people_limit:
                            print("Lift is at full capacity. Remaining requests cannot be processed.\n"  )
                            break

                        while True:
                            try:
                                pickup_floor = int(input(f"\nFloor {f}: Which floor are people waiting on?: " ))
                                if pickup_floor < 0 or pickup_floor > total_floors:
                                    print(f"Floor must be non-negative and below floor {total_floors}. Please try again.\n")
                                    continue
                                lift.add_request(pickup_floor)
                                people_in_lift += 1
                                break
                            except ValueError:
                                print("Invalid floor number. Please enter an integer.\n")

                            lift.add_request(pickup_floor)
                            people_in_lift += 1
                            break

        except ValueError:
            print("Invalid input. Please enter number values where required.")

        return people_in_lift
    

    # This is now the request function for the FIFO algortihm
    @ staticmethod
    def FIFO_requests(lift,people_in_lift):
        with open('info.json', 'r') as file:
            data = json.load(file)
        total_floors = data["TechnicalComponents"]["NumberOfFloors"]
        people_limit = data["TechnicalComponents"]["People_Limit"]

        try:
            Internal_GettingOn = '0'
            while Internal_GettingOn.lower() != 'yes' and Internal_GettingOn.lower() != 'no':
                Internal_GettingOn = input("Are there people getting on, on this floor? ('yes' or 'no'): ")
                continue
            if Internal_GettingOn.lower() == 'yes':
                Internal_People = int(input("How many people are getting on?: "))

                while True:
                    if not General.safety_checks(people_in_lift + Internal_People):
                        print("Doors reopening - Too many people!\n")
                        break
                    else:
                        total_people = people_in_lift + Internal_People

                    for i in range(1,Internal_People+1):
                        while True:
                            try:
                                Internal_Floor = int(input(f"Which floor is person {i} going to?: "))
                                if Internal_Floor < 0 or Internal_Floor > total_floors:
                                    print(f"Floor must be non negative and below floor {total_floors}" )
                                    continue
                                lift.FIFO_add_request(Internal_Floor)
                                lift.add_passenger(Internal_Floor)
                                break
                            except ValueError:
                                print("Invalid floor number. Please enter an integer.\n")
                    
                    people_in_lift = total_people
                    print(f"{Internal_People} people got on. Total people now: {total_people}\n")
                    break
            
            else:
                print("No people boarding on this floor.\n")    

        except ValueError:
            print("Invalid input. Please enter number values where required.")


        try:
            if people_in_lift <= people_limit:  # Making sure there's even more space for more requests
                External_GettingOn = '0'
                while External_GettingOn != 'yes' and External_GettingOn != 'no':
                    External_GettingOn = input("Are there people requesting the lift from other floors? ('yes' or 'no'): ")
                    continue
                if External_GettingOn == 'yes':
                    while True:
                        try:
                            External_People = int(input("How many floors have people waiting?: "))
                            break
                        except ValueError:
                            print("Invalid input. Please enter a number.\n")
                    
                    for f in range(1,External_People+1):
                        if people_in_lift >= people_limit:
                            print("Lift is at full capacity. Remaining requests cannot be processed.\n"  )
                            break

                        while True:
                            try:
                                pickup_floor = int(input(f"\nFloor {f}: Which floor are people waiting on?: " ))
                                if pickup_floor < 0 or pickup_floor > total_floors:
                                    print(f"Floor must be non-negative and below floor {total_floors}. Please try again.\n")
                                    continue
                                lift.FIFO_add_request(pickup_floor)
                                people_in_lift += 1
                                break
                            except ValueError:
                                print("Invalid floor number. Please enter an integer.\n")

                            lift.FIFO_add_request(pickup_floor)
                            people_in_lift += 1
                            break

        except ValueError:
            print("Invalid input. Please enter number values where required.")

        return people_in_lift




from collections import deque
class lift_algorithms:
    
    def __init__(self):
        self.people_in_lift = 0

        # These are for the Scan and Look
        with open('info.json', 'r') as file:
            data = json.load(file)
        
        self.total_floors = data["TechnicalComponents"]["NumberOfFloors"]
        self.lift_queue = deque()


    def MYLIFT_main(self):

        # Creating instances
        general = General()
        lift = MYLIFT()

        while True:
            self.people_in_lift = general.requests(lift,self.people_in_lift)
            if lift.is_empty():
                print("No requests.")

            while not lift.is_empty():
                next_floor = lift.get_next_floor()
                general.moving(lift.current_floor, next_floor)
                lift.current_floor = next_floor
                print(f"Lift has arrived at floor {next_floor}.\n")

                exiting = lift.remove_passengers()
                self.people_in_lift -= exiting

                self.people_in_lift = general.requests(lift, self.people_in_lift)

                if lift.is_empty():
                    break

    
    def MYLIFT2_main(self):
        
        # Creating instances
        general = General()
        lift = MYLIFT()

        while True:
            self.people_in_lift = general.FIFO_requests(lift,self.people_in_lift)
            if lift.FIFO_is_empty():
                print("No requests.")

            while not lift.FIFO_is_empty():
                next_floor = lift.FIFO_get_next_floor()
                general.moving(lift.current_floor, next_floor)
                lift.current_floor = next_floor
                print(f"Lift has arrived at floor {next_floor}.\n")

                exiting = lift.remove_passengers()
                self.people_in_lift -= exiting

                self.people_in_lift = general.FIFO_requests(lift, self.people_in_lift)

                if lift.FIFO_is_empty():
                    break
        
    # These next few functions are strictly for the Scan & Look algorithms
    
    def process_requests(self):
    # goes from first floor to last and then back down

        # Going up:
        for floor in range(1, self.total_floors + 1):
            self.process_floor(floor)

        # Going down:
        for floor in range(self.total_floors, 0, -1):
            self.process_floor(floor)


    def unload_passangers(self,floor):
        initial_count = len(self.lift_queue)
        self.lift_queue = deque(dest for dest in self.lift_queue if dest != floor)
        removed_count = initial_count - len(self.lift_queue)

        if removed_count > 0:
            print(f"{removed_count} passenger(s) got off at floor {floor}.")
        else:
            print(f"No passengers getting off at floor {floor}.")

    
    def process_floor(self,floor):

        print(f"Lift has arrived at floor {floor}.")
        self.unload_passangers(floor)

        people_entering = int(input(f"How many people are entering at floor {floor}? "))
        for i in range(people_entering):
            while True:
                destination = int(input(f"Which floor does person {i+1} want to go to?: "))
                if 1 <= destination <= self.total_floors and destination != floor:
                    self.lift_queue.append(destination)
                    print(f"Person {i+1} added with destination floor {destination}.")
                    break
                else:
                    print(f"Invalid floor. Please enter a floor between 1 and {self.total_floors}, different from {floor}.")

        print(f"Current passengers' destinations: {list(self.lift_queue)}")


    def SCAN_main(self):
        direction = "up"
        current_floor = 1

        # Start SCAN algorithm (up then down)
        while True:
            if direction == "up":
                for floor in range(current_floor, self.total_floors + 1):
                    current_floor = floor
                    self.process_floor(floor)
                direction = "down"

            elif direction == "down":
                for floor in range(current_floor, 0, -1):
                    current_floor = floor
                    self.process_floor(floor)
                direction = "up"

        
