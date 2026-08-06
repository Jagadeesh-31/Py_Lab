from my_programs import *

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


def display_menu():
    print("\n========== FUNCTION MENU ==========")
    for key, value in MENU.items():
        print(f"{key}. {value[0]}")
    print("0. Exit")
    print("===================================")


def main():

    n = int(input("Enter No. of Executions: "))

    for i in range(n):

        print(f"\nExecution {i+1} of {n}")

        display_menu()

        choice = int(input("Enter Your Choice: "))

        if choice == 0:
            print("Thank You...")
            break

        elif choice in MENU:
            print("-" * 40)
            MENU[choice][1]()       # Function Calling
            print("-" * 40)

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()
