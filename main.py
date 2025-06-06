# Fox Chicken Grain Program

# Variables initialization
fox = 0
chicken = 0
grain = 0
farmer = 0
maybe = False
response = ""

def Grouping():
    '''
    Returns two lists: positions1 for items on far side (value=1),
    positions0 for items on near side (value=0).
    Uses enumerate to get indices and values from variables.
    '''
    target_1 = 1
    target_0 = 0
    positions1 = []
    positions0 = []

    for index, value in enumerate([fox, chicken, grain, farmer]):
        if value == target_1:
            positions1.append(index)
        elif value == target_0:
            positions0.append(index)
    return positions1, positions0

def puzzle_solved():
    '''
    Checks if fox, chicken, and grain are all on far side (value=1).
    Returns True if solved, False otherwise.
    '''
    items = [fox, chicken, grain]
    return items.count(1) == 3

def wrong_move():
    '''
    Checks if the puzzle is lost.
    Returns (True, message) if lost, (False, "") otherwise.
    Checks both sides of the river.
    '''
    Response1 = "The fox ate the chicken."
    Response2 = "The chicken ate the grain."
    Response3 = ""

    # Farmer on far side, check near side for danger
    if farmer == 1:
        if fox == 0 and chicken == 0:
            return True, Response1
        if chicken == 0 and grain == 0:
            return True, Response2

    # Farmer on near side, check far side for danger
    if farmer == 0:
        if fox == 1 and chicken == 1:
            return True, Response1
        if chicken == 1 and grain == 1:
            return True, Response2

    return False, Response3

def Output(positions1, positions0, maybe, response):
    '''
    Prints the current state of the river crossing.
    Items on near side (value=0) and far side (value=1).
    If maybe is True, also prints the losing response.
    '''
    items = ['Fox', 'Chicken', 'Grain', 'Farmer']

    print("-----------------------")
    print("This side of the river:")
    for pos in positions0:
        print(items[pos])
    print("\nThe other side of the river:")
    for pos in positions1:
        print(items[pos])
    print("-----------------------")

    if maybe:
        print(response)

print("A fox, chicken and a bag of grain wait by the side of a river.\n")

# Main loop - continue until solved or lost
while True:
    choice = input("Which item will you take in your rowboat to the other side?\n\nfox, chicken, grain or farmer?\n\nChoose: ").lower().strip()

    # Move logic: only move item if farmer and item are on same side (both 0 or both 1)
    # Farmer moves alone too

    # Farmer's current side (0 or 1)
    current_side = farmer

    if choice == 'farmer':
        # Farmer crosses alone - toggle side
        farmer = 1 - farmer

    elif choice == 'fox':
        if fox == current_side:
            # Move farmer and fox to other side
            fox = 1 - fox
            farmer = 1 - farmer
        else:
            print("\nYou can't take that item because the farmer is not on the same side.")
            continue

    elif choice == 'chicken':
        if chicken == current_side:
            chicken = 1 - chicken
            farmer = 1 - farmer
        else:
            print("\nYou can't take that item because the farmer is not on the same side.")
            continue

    elif choice == 'grain':
        if grain == current_side:
            grain = 1 - grain
            farmer = 1 - farmer
        else:
            print("\nYou can't take that item because the farmer is not on the same side.")
            continue

    else:
        print("\nInvalid choice. Please type fox, chicken, grain or farmer.")
        continue

    # Show current state
    positions1, positions0 = Grouping()
    maybe, response = wrong_move()
    Output(positions1, positions0, maybe, response)

    # Check if lost
    if maybe:
        break

    # Check if solved
    if puzzle_solved():
        print("You solved the puzzle.")
        break