import time

 

# Define the number of floors in the building

num_floors = 5

 

# Initialize elevator position and direction

elevator_position = 0  # Starting on the ground floor

elevator_direction = 1  # 1 for up, -1 for down

 

# Function to display the elevator's position using ASCII art

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

 

# Main simulation loop

while True:

    # Display the building and elevator

    print("\nBuilding:")

    display_elevator(elevator_position)

 

    # Get user input for the target floor

    try:

        target_floor = int(input("\nEnter target floor (1 to {}): ".format(num_floors)))

    except ValueError:

        print("Invalid input. Please enter a valid floor number.")

        continue

 

    # Check if the target floor is within bounds

    if 1 <= target_floor <= num_floors:

        # Move the elevator

        while elevator_position != target_floor:

            if elevator_position < target_floor:

                elevator_position += 1

            else:

                elevator_position -= 1

            # Display the building and elevator after each move

            print("\nBuilding:")

            display_elevator(elevator_position)

            # Sleep for a moment to make it visible

            time.sleep(1)

 

        print("\nElevator has reached floor {}.".format(target_floor))

 

        # Ask the user if they want to continue

        choice = input("Do you want to continue (yes/no)? ").lower()

        if choice != "yes":

            break

    else:

        print("Invalid floor number. Please enter a valid floor between 1 and {}.".format(num_floors))

 

print("Elevator simulation terminated.")