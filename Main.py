def scene_1():
    print("\n=== Scene 1: The Mysterious Hallway ===")
    print("You wake up in a dimly lit hallway. The walls are lined with old portraits, their eyes seemingly following your movements.")
    print("A cold breeze drifts through the corridor, and two doors stand before you.")

    choice = input("\nDo you go 'left' into the library, or 'right' into the dining hall? ").strip().lower()

    if choice == "left":
        return "scene_2"
    elif choice == "right":
        return "scene_3"
    else:
        print("\nThat doesn't seem like an option. Try again.")
        return "scene_1"


def scene_2():
    print("\n=== Scene 2: The Haunted Library ===")
    print("You step into an ancient library. Dusty bookshelves tower over you, their contents whispering as if alive.")
    print("A ghostly figure emerges from the shadows, its hollow eyes staring directly at you.")

    choice = input("\nDo you 'run' in fear or 'talk' to the spirit? ").strip().lower()

    if choice == "run":
        print("\nYou turn and sprint, but a bookshelf collapses, forcing you through a hidden door!")
        return "scene_4"
    elif choice == "talk":
        print("\nThe ghost tells you of a hidden passage behind a bookshelf. You push it open and step through.")
        return "scene_5"
    else:
        print("\nThe ghost waits, its gaze unchanging. Try again.")
        return "scene_2"
