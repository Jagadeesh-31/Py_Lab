from my_programs import *   # import all 14 program functions from my_programs.py

# Dictionary mapping menu number -> (display name, function to run)
MENU = {
    1: ("Swap Two Numbers", program_1_swap_numbers),
    2: ("GCD of Two Numbers", program_2_gcd),
    3: ("Custom Sorting", program_3_custom_sort),
    4: ("Reverse Number", program_4_reverse_number),
    5: ("Sum of Digits", program_5_sum_digits),
    6: ("Count Vowels", program_6_count_vowels),
    7: ("Count Words", program_7_count_words),
    8: ("Title Case", program_8_title_case),
    9: ("Palindrome", program_9_palindrome),
    10: ("Prime Number", program_10_prime_number),
    11: ("Factorial", program_11_factorial),
    12: ("Decimal to Binary", program_12_decimal_to_binary),
    13: ("Largest of Three Numbers", program_13_largest_of_three),
    14: ("Remove Duplicates", program_14_remove_duplicates)
}


def display_menu():
    print("\n== PYTHON FUNCTION BANK ==")
    for key, value in MENU.items():          # loop through menu items
        print(f"{key}. {value[0]}")          # print number and program name
    print("0. Exit")                         # option to quit
    print(" ")


# Driver Code 
execution = int(input("Enter Number of Executions: "))  # how many programs to run
count = 0                                                # tracks completed runs

while count < execution:        # keep looping until execution count is reached
    display_menu()               # show the menu each time
    choice = int(input("Enter Your Choice: "))  # get user's menu choice

    if choice == 0:              # user chose to exit
        print("Exit...")
        break                    # stop the loop early

    elif choice in MENU:         # valid menu choice
        print("\nRunning:", MENU[choice][0])
        print("-" * 50)
        MENU[choice][1]()        # call the selected function
        print("-" * 50)
        count += 1                # increment successful run count
        print(f"Execution : {count}/{execution}")

    else:                        # invalid number entered
        print("Invalid Choice!")

print("\nProgram Ended.")   # final message after loop ends
