import random 

def print_intro_text():
    Print("intro")


def print_player_status(player_info:dict)->None:
    print(f"Your current health is {player_info['health']}")

initial_health = random.randint(30,50)
player_info = {
    'name':' ',
    'health': initial_health
}

def choice_one():
    print("1) Climb a nearby tree and check your surroundings")
    print("2) Start walking and see where you end up")
    while True:
        try:
            player_choice = int(input("> "))
        except ValueError:
            print("That is not a valid option")
            continue
        if player_choice == 1:
            climb_tree()
        elif player_choice == 2:
            start_walking()
        else:
            print("Invalid choice")
            continue

def choice_two():
    print("1) Go to the lake")
    print("2) Go to the river")
    while True:
        try:
            player_choice = int(input("> "))
        except ValueError:
            print("That is not a valid option")
            continue
        if player_choice == 1:
            lake()
        elif player_choice == 2:
            river()
        else:
            print("Invalid choice")
            continue

def choice_three():
    print("1) Try to cross the lake")
    print("2) Find a way around")
    while True:
        try:
            player_choice = int(input("> "))
        except ValueError:
            print("That is not a valid option")
            continue
        if player_choice == 1:
            cross_lake()
        elif player_choice == 2:
            go_around()
        else:
            print("Invalid choice")
            continue
