from classes import lift_algorithms

if __name__ == "__main__":
    algo = lift_algorithms()


algorithm = input("Which algorithm would you like to use?\n •Scan\n •Look\n •MyLift1\n •MyLift2\n\n")
if algorithm.lower() == 'scan':
    algo.SCAN_main()
elif algorithm.lower() == 'look':
    algo.LOOK_main()
elif algorithm.lower() == 'mylift1':
    algo.MYLIFT_main()
elif algorithm.lower() == 'mylift2':
    algo.MYLIFT2_main()
else:
    print("Failed to select correct algorithm, please restart the program.")