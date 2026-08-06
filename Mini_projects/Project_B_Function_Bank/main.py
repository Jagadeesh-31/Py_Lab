# Import all functions from my_programs module
from my_programs import *

# Store menu options with their corresponding function names
MENU = {
    1: ("Swap Two Numbers", program_1_swap_numbers),
    2: ("GCD of Two Numbers", program_2_gcd),
    3: ("Custom Sorting", program_3_custom_sort),
    4: ("Reverse a Number", program_4_reverse_number),
    5: ("Sum of Digits", program_5_sum_digits),
    6: ("Count Vowels", program_6_count_vowels),
    7: ("Count Words", program_7_count_words),
    8: ("Title Case", program_8_title_case),
    9: ("Palindrome", program_9_palindrome),
    10: ("Prime Number", program_10_prime_number),
    11: ("Factorial", program_11_factorial),
    12: ("Decimal to Binary", program_12_decimal_to_binary),
    13: ("Largest of Three", program_13_largest_of_three),
    14: ("Remove Duplicates", program_14_remove_duplicates),
}


# Function to display the menu
def display_menu():
    # Print menu heading
    print("\n========== FUNCTION MENU ==========")

    # Display all menu options
    for key, value in MENU.items():
        print(f"{key}. {value[0]}")

    # Display exit option
    print("0. Exit")

    # Print menu footer
    print("===================================")


# Main function
def main():

    # Read the number of executions from the user
    n = int(input("Enter No. of Executions: "))

    # Repeat menu based on user input
    for i in range(n):

        # Display current execution count
        print(f"\nExecution {i+1} of {n}")

        # Show the menu
        display_menu()

        # Read user's choice
        choice = int(input("Enter Your Choice: "))

        # Exit if user selects 0
        if choice == 0:
            print("Thank You...")
            break

        # Execute the selected function if the choice is valid
        elif choice in MENU:
            print("-" * 40)

            # Call the selected function
            MENU[choice][1]()

            print("-" * 40)

        # Display error for invalid choice
        else:
            print("Invalid Choice!")


# Start program execution
if __name__ == "__main__":
    # Call the main function
    main()
