def start():
    print("You're in a dark room. There's a door to your right and left.")
    choice = input("Which door? (left/right): ")
    if choice == 'left':
        treasure_room()
    else:
        monster_room()

def treasure_room():
    print("You found treasure!")
    play_again()

def monster_room():
    print("A monster attacks you! Game Over.")
    play_again()

def play_again():
    if input("Play again? (yes/no): ").lower() == 'yes':
        start()

start()