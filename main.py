from classes import lift_algorithms
from classes import General

if __name__ == "__main__":
    algo = lift_algorithms()

General.print_floors()

algorithm = input("Which algorithm would you like to use?\n •Scan\n •Look\n •MyLift1\n •MyLift2\n\n")
if algorithm.lower() == 'scan':
    General.print_floors()
    algo.SCAN_main()
elif algorithm.lower() == 'look':
    General.print_floors()
    algo.LOOK_main()
elif algorithm.lower() == 'mylift1':
    General.print_floors()
    algo.MYLIFT_main()
elif algorithm.lower() == 'mylift2':
    General.print_floors()
    algo.MYLIFT2_main()
else:
    print("Failed to select correct algorithm, please restart the program.")