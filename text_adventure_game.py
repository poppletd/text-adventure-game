import random 
import time


    
def print_intro_text():
    print()
    print("----------")
    print("The Forest")
    print("----------")
    intro_art = r'''                
               ,@@@@@@@,
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
   ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
   %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
   %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
   `&%\ ` /%&'    |.|        \ '|8'
       |o|        | |         | |
       |.|        | |         | |
    \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_
'''
    print(intro_art)
    player_name = input("Enter your name: ")
    for i in range(10):
        time.sleep(0.3)
        print(".")

def intro_scene():
    print("you slowly come to consciousness and take a look around")
    print("you're surrounded by thick foliage on all sides")
    print("you're all alone lost in the middle of a forest") 
    print("you have no idea how you got there")
    print()
    print("you decide to scan your surroundings again")
    print("you need to figure out the best course of action")
    print()

def choice_one(player_score):
    print("Would you like to:")
    print("1) Climb a nearby tree and check your surroundings")
    print("2) Start walking and see where you end up")
    while True:
        try:
            player_choice = int(input("> "))
        except ValueError:
            print("That is not a valid option")
            continue
        if player_choice == 1:
            climb_tree(player_score)
        elif player_choice == 2:
            start_walking(player_score)
        else:
            print("Invalid choice")
            continue

def choice_two(player_score):
    print("Would you like to:")
    print("1) Go to the lake")
    print("2) Go to the river")
    while True:
        try:
            player_choice = int(input("> "))
        except ValueError:
            print("That is not a valid option")
            continue
        if player_choice == 1:
            lake(player_score)
        elif player_choice == 2:
            river(player_score)
        else:
            print("Invalid choice")
            continue

def choice_three(player_score):
    print("Would you like to: ")
    print("1) Try to cross the lake")
    print("2) Find a way around")
    while True:
        try:
            player_choice = int(input("> "))
        except ValueError:
            print("That is not a valid option")
            continue
        if player_choice == 1:
            cross_lake(player_score)
        elif player_choice == 2:
            go_around(player_score)
        else:
            print("Invalid choice")
            continue

def climb_tree(player_score):
    print()
    print("you find the tallest tree you can climb nearby")
    print("once you get up to the top of the tree you're able to see a decent distance through the forest")
    print("It's a great view")
    print("+1 point")
    player_score = player_score + 1
    print("on your right you can see a lake")
    print("on your left you see a river")
    print()
    choice_two(player_score)

def start_walking(player_score):
    print()
    print("you find a clear enough path through the trees and start walking")
    print("along the way you find a blackberry bush and stop to eat")
    print("+2 points")
    player_score = player_score + 2
    print("after quite a bit of walking you start to see the edge of a lake")
    print("you walk towards it")
    print()
    lake(player_score)

def river(player_score):
    print()
    print("you arrive at the river")
    print("the water is moving quickly")
    print("will you reach your hand in?")
    print("(type 1 for yes, 2 for no)")
    while True:
        try:
            player_choice = int(input("> "))
        except ValueError:
            print("That is not a valid option")
            continue
        if player_choice == 1:
            num = random.randint(1,2)
            if num == 1:
                print()
                print("you reach your hand in")
                print("a fish swims right into your hand and you manage to grab it")
                print("+2 points")
                player_score = player_score + 2
                break
            elif num == 2:
                print()
                print("you reach your hand in")
                print("you scrape your hand on a rock, it hurts really bad")
                print("-1 point")
                player_score = player_score - 1
                break
        elif player_choice == 2:
            break
        else:
            print("Invalid choice")
            continue 
    print()
    print("there is no way to cross the river and nothing else to do there")
    print("you decide to go to the lake you spotted earlier")
    lake(player_score)

def lake(player_score):
    print()
    print("you arrive at the edge of the lake")
    print("the lake is massive and you can just barely see the other side")
    print("there might be a way around the lake, but it's hard to tell because of the fog")
    print()
    choice_three(player_score)     

def cross_lake(player_score):
    print()
    print("you step foot into the lake to test how deep it is")
    print("the lake is too deep to walk through, you would have to swim all the way across")
    print()
    print("you decide to swim across and just barely have enough strength to make it to the other side")
    print("you are left exhausted and unable to move for awhile")
    print("-2 points")
    player_score = player_score - 2
    ending(player_score)

def go_around(player_score):
    print()
    print("you start walking around the edge of the lake")
    print("on the way you come across some pretty flowers")
    print("you stop to smell them and are filled with hope")
    print("+1 point")
    player_score = player_score + 1
    print("after walking for awhile you end up on the opposite side of the lake just like you planned")
    ending(player_score)

def ending(player_score):
    print()
    print(f"your final score is: {player_score}")
    print()


def main(player_score):
    player_score = 0 
    print_intro_text()
    intro_scene()
    choice_one(player_score)

main(0)
