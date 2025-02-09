import time
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


heap = []
floor = 1
elevator = {}
