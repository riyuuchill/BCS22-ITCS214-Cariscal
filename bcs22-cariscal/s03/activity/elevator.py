import time

num_floors = 5
elevator_position = 0
elevator_direction = 1

def display_elevator(position):
    for floor in range(num_floors, 0, -1):
        if floor == position:

            print("+-----+  Elevator [0]")

            print("|  O  |  Floor {}".format(floor))

            print("|  |  |")

            print("+-----+")

        else:

            print("+-----+")

            print("|     |")

            print("|     |")

            print("+-----+")
while True:
    print("\nBuilding:")
    display_elevator(elevator_position)
    try:
        target_floor = int(input("\nEnter target floor (1 to {}): ".format(num_floors)))
    except ValueError:
        print("Invalid input. Please enter a valid floor number.")
        continue

    if 1 <= target_floor <= num_floors:
        while elevator_position != target_floor:
            if elevator_position < target_floor:
                elevator_position += 1
            else:
                elevator_position -= 1
            print("\nBuilding:")
            display_elevator(elevator_position)
            time.sleep(1)

        print("\nElevator has reached floor {}.".format(target_floor))
        choice = input("Do you want to continue (yes/no)? ").lower()
        if choice != "yes":
            break

    else:
        print("Invalid floor number. Please enter a valid floor between 1 and {}.".format(num_floors))

print("Elevator simulation terminated.")
