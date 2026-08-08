# Game Generator Sequence 
from program import *


def main():
    # Tracks total plays across ALL games combined, not just one game repeated.
    # Playing Game 1 twice, then Game 2 twice, still adds up to a warning.
    count = 0

    while True:
        menu = {
            1: ("Rock Paper Scissors Game", rock_paper_scissors),
            2: ("Story Generator", story),
            3: ("Email Sender", send_email),
            4: ("BMI Calculator", bmi_calculator),
            0: ("Exit", None)
        }

        screen_time_menu = {
            1: "Continue with the same project",
            2: "Go back to Main Menu",
            3: "Take a short break and rest your eyes",
            4: "Continue learning another mini project",
            5: "Exit"
        }

        print("=" * 40)
        print("      PYTHON MINI PROJECTS")
        print("=" * 40)
        for key, value in menu.items():
            print(f"{key}. {value[0]}")
        print("=" * 40)

        try:
            choice = int(input("Enter your choice (0-4): "))
            if choice == 0:
                print("Thank You! Visit Again.")
                break
            if choice not in menu:
                print("Invalid Choice!")
                continue

            print(f"\nYou selected: {menu[choice][0]}")
            confirm = input("Is this correct? (y/n): ").lower()
            if confirm != "y":
                print("Okay, pick again.\n")
                continue

            while True:
                menu[choice][1]()
                count += 1

                if count >= 3:
                    print("\n" + "*" * 55)
                    print("              SCREEN TIME WARNING")
                    print("*" * 55)
                    print("You have used these mini projects more than 3 times.")
                    print("\nSuggestions:")
                    for key, value in screen_time_menu.items():
                        print(f"{key}. {value}")
                    print("*" * 55)

                    option = int(input("Enter your option (1-5): "))
                    count = 0  # reset after warning so it doesn't nag every play after this
                    if option == 1:
                        continue
                    elif option == 2:
                        break
                    elif option == 3:
                        print("\nPlease take a 5-10 minute break.")
                        print("Too much screen time may cause eye strain.")
                        print("Stay healthy and come back refreshed!")
                        break
                    elif option == 4:
                        print("\nReturning to Main Menu...")
                        break
                    elif option == 5:
                        print("Thank You! Visit Again.")
                        return
                    else:
                        print("Invalid Option!")
                        break

                again = input(
                    f"\nDo you want to run '{menu[choice][0]}' again? (y/n): "
                ).lower()
                if again == "y":
                    continue
                elif again == "n":
                    print("Returning to Main Menu...\n")
                    break
                else:
                    print("Invalid Choice!")
                    break

        except ValueError:
            print("Please enter numbers only.")


main()
