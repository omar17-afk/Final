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


def scene_3():
    print("\n=== Scene 3: The Abandoned Dining Hall ===")
    print("You enter a grand dining hall. The long table is covered in dust, with untouched plates of rotting food still in place.")
    print("Suddenly, you hear the sound of footsteps from the kitchen.")

    choice = input("\nDo you 'investigate' the kitchen or 'hide' under the table? ").strip().lower()

    if choice == "investigate":
        print("\nYou cautiously step into the kitchen, only to find an old, creaky door leading to an underground chamber.")
        return "scene_4"
    elif choice == "hide":
        print("\nAs you crouch under the table, your hand touches a hidden latch. A trapdoor opens beneath you!")
        return "scene_5"
    else:
        print("\nThe eerie silence continues as you hesitate. Try again.")
        return "scene_3"


def scene_4():
    print("\n=== Scene 4: The Secret Passage ===")
    print("You find yourself in a narrow tunnel, its walls carved with strange symbols that glow faintly.")
    print("At the end of the passage, you see a large wooden chest covered in cobwebs.")

    choice = input("\nDo you 'open' the chest or 'turn back'? ").strip().lower()

    if choice == "open":
        print("\nYou lift the lid and find an ancient relic pulsing with energy. You have discovered a powerful artifact!")
        return "quit"
    elif choice == "turn back":
        print("\nYou decide it's too risky and retrace your steps, ending up in the hallway again.")
        return "scene_1"
    else:
        print("\nThe passage remains still, waiting for your decision. Try again.")
        return "scene_4"


def scene_5():
    print("\n=== Scene 5: The Underground Chamber ===")
    print("You land in a cavernous underground chamber, its walls lined with glowing blue crystals.")
    print("A massive stone door stands before you, with an inscription: 'The past holds the key to the future.'")

    choice = input("\nDo you 'explore' the chamber or 'climb' back up? ").strip().lower()

    if choice == "explore":
        print("\nYou step forward and touch the door. It rumbles open, revealing a hidden realm beyond. You have unlocked a great mystery!")
        return "quit"
    elif choice == "climb":
        print("\nYou grab onto an old rope ladder and ascend, returning to the hallway.")
        return "scene_1"
    else:
        print("\nThe crystals hum softly as you hesitate. Try again.")
        return "scene_5"


def start_game():
    current_scene = "scene_1"

    while True:
        if current_scene == "scene_1":
            current_scene = scene_1()
        elif current_scene == "scene_2":
            current_scene = scene_2()
        elif current_scene == "scene_3":
            current_scene = scene_3()
        elif current_scene == "scene_4":
            current_scene = scene_4()
        elif current_scene == "scene_5":
            current_scene = scene_5()
        elif current_scene == "quit":
            print("\nThank you for playing! See you next time.")
            break
        else:
            print("\nUnknown scene. Exiting the game.")
            break

start_game()