import time
import json
from algorithms import (
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

heap = []
floor = 1
elevator = 0

def main(heap,floor,elevator):
    enter = 1