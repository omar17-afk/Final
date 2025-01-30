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