"""
Collection of 14 beginner Python practice programs.

Each concept is implemented as a SINGLE function that handles input,
logic, and output together (no separate helper function per concept).
This module only defines the functions so it can be imported with
`from my_programs import *` by a separate driver script (e.g. main.py)
that supplies its own menu.
"""


# 1. Swap Two Numbers

def program_1_swap_numbers():
    """
    Program: Swap Two Numbers

    Description:
    Swaps two positive numbers without using a temporary variable.
    If both numbers are negative, it returns "Enter only +ve Values".
    If both numbers are zeros, it returns "Enter Values Greater than Zero to Swap numbers.".

    Sample Test Cases:
    Test Case 1: swap_nums(10, 20) -> (20, 10)
    Test Case 2: swap_nums(0, 0) -> Enter Values Greater than Zero
    Test Case 3: swap_nums(-5, -1) -> Enter only +ve Values

    Explanation:
    Uses addition and subtraction to swap two numbers
    without using a temporary variable.
    """
    a, b = map(int, input("Enter a,b: ").split(","))   # read two numbers
    print(f"Before Swap: a = {a}, b = {b}")

    if a < 0 or b < 0:                                  # reject negatives
        print("Warning: Negative values detected.")
    elif a == 0 and b == 0:                              # reject both zero
        print("Enter Values Greater than Zero to Swap numbers.")
    else:
        a = a + b        # combine both values into a
        b = a - b        # extract original a into b
        a = a - b        # extract original b into a
        print(f"After Swap: a = {a}, b = {b}")

    print(program_1_swap_numbers.__doc__)


# 2. GCD of Two Numbers
def program_2_gcd():
    """
    Program: GCD of Two Numbers

    Description:
    Finds the Greatest Common Divisor (GCD) of two positive numbers
    using the Euclidean Algorithm.
    If either number is negative, it returns "Enter only +ve nums".
    If both numbers are zero, it returns
    "Enter Values Greater than Zero to Find Gcd Value of numbers."

    Sample Test Cases:
    Test Case 1: gcd(12,18) -> 6
    Test Case 2: gcd(25,15) -> 5
    Test Case 3: gcd(-5,10) -> Enter only +ve nums

    Explanation:
    Uses the Euclidean Algorithm. Repeatedly replaces the larger
    number with the remainder of dividing it by the smaller number
    until the second number becomes 0.
    """

    a, b = map(int, input("Enter a,b: ").split(","))   # Read two numbers

    x, y = a, b                                        # Store original values

    if a < 0 or b < 0:                                 # Check for negative values
        result = "Enter only +ve nums"

    elif a == 0 and b == 0:                            # Check if both numbers are zero
        result = "Enter Values Greater than Zero to Find Gcd Value of numbers."

    else:
        while b:                                       # Euclidean Algorithm
            a, b = b, a % b
        result = a

    print(f"GCD of {x} and {y} = {result}")            # Display the GCD

    print(program_2_gcd.__doc__)                       # Print the program documentation

# 3. Custom Sorting (Sort by String Length)

def program_3_custom_sort():
    """
    Program: Custom Sorting (Sort by String Length)

    Description:
    Sorts a list of strings based on their length in ascending order.
    If the list is empty or contains only one element, an appropriate
    message is displayed.

    Sample Test Cases:
    Test Case 1: custom_sort(['apple', 'hi', 'banana']) -> ['hi', 'apple', 'banana']
    Test Case 2: custom_sort(['python']) -> List Must Contain More Than One Element
    Test Case 3: custom_sort([]) -> Add at least one element to the list

    Explanation:
    Uses Python's built-in sorted() function with the key=len
    parameter to sort the strings according to their length.
    """
    l = list(input("Enter list elements separated by commas: ").split(","))  # read list
    print(f"Original List : {l}")

    if l == [''] or l == []:                     # empty input
        result = "Add at least one element to the list"
    elif len(l) < 2:                              # only one element
        result = "List Must Contain More Than One Element"
    else:
        result = sorted(l, key=len)               # sort by string length

    print(f"Sorted by Length : {result}")
    print(program_3_custom_sort.__doc__)


# 4. Reverse a Number

def program_4_reverse_number():
    """
    Program: Reverse a Number

    Description:
    Reverses a positive integer.
    If the entered number is negative, it returns
    "Enter only +ve nums".

    Sample Test Cases:
    Test Case 1: res_num(12345) -> 54321
    Test Case 2: res_num(1000) -> 1
    Test Case 3: res_num(-456) -> Enter only +ve nums

    Explanation:
    Converts the number into a string,
    reverses it using slicing ([::-1]),
    and converts it back into an integer.
    """
    n = int(input("Enter a number: "))    # read number

    if n < 0:                              # reject negative
        result = "Enter only +ve nums"
    elif n == 0:                           # reject zero
        result = "Reverse not possible for zero."
    else:
        result = str(n)[::-1]              # reverse digits via string slicing

    print(f"Reverse Number: {result}")
    print(program_4_reverse_number.__doc__)


# 5. Sum of Digits
def program_5_sum_digits():
    """
    Program: Sum of Digits

    Description:
    Calculates the sum of digits of a positive number.
    If the number is negative, it returns "Enter only +ve nums".
    If the number is zero, it returns
    "Enter Values Greater than Zero to Find Sum of Digits."

    Sample Test Cases:
    Test Case 1: sum_digits(12345) -> 15
    Test Case 2: sum_digits(0) -> Enter Values Greater than Zero to Find Sum of Digits.
    Test Case 3: sum_digits(-123) -> Enter only +ve nums

    Explanation:
    Repeatedly extracts the last digit using the modulus (%)
    operator, adds it to the sum, and removes the last digit
    until the number becomes zero.
    """

    n = int(input("Enter a number: "))      # Read number

    if n < 0:                               # Check for negative number
        result = "Enter only +ve nums"

    elif n == 0:                            # Check if number is zero
        result = "Enter Values Greater than Zero to Find Sum of Digits."

    else:
        result = 0                          # Initialize sum

        while n > 0:                        # Repeat until number becomes 0
            result += n % 10                # Add last digit
            n = n // 10                     # Remove last digit

    print(f"Sum of Digits: {result}")       # Display result

    print(program_5_sum_digits.__doc__)     # Print program documentation

# 6. Count Vowels in a String

def program_6_count_vowels():
    """
    Program: Count Vowels in a String

    Description:
    Counts the total number of vowels (a, e, i, o, u)
    present in a given string.
    If the string is empty, it returns
    "Enter a valid string."

    Sample Test Cases:
    Test Case 1: count_vowels("Python") -> 1
    Test Case 2: count_vowels("Education") -> 5
    Test Case 3: count_vowels("") -> Enter a valid string.

    Explanation:
    Traverses each character in the string and checks
    whether it is a vowel. If it is, the counter is
    incremented and the total count is returned.
    """
    s = input("Enter a string: ")    # read string

    if s == "":                       # reject empty string
        result = "Enter a valid string."
    else:
        count = 0
        for ch in s.lower():           # check each character (case-insensitive)
            if ch in "aeiou":
                count += 1              # increment on vowel match
        result = count

    print(f"Number of Vowels: {result}")
    print(program_6_count_vowels.__doc__)


# 7. Count Words in a Sentence

def program_7_count_words():
    """
    Program: Count Words in a Sentence

    Description:
    Counts the total number of words in a given sentence.
    If the sentence is empty, it returns
    "Enter a valid sentence."

    Sample Test Cases:
    Test Case 1: count_words("Python is easy") -> 3
    Test Case 2: count_words("Hello World") -> 2
    Test Case 3: count_words("") -> Enter a valid sentence.

    Explanation:
    Splits the sentence into individual words using
    the split() method and returns the total number
    of words present in the sentence.
    """
    sentence = input("Enter a sentence: ")   # read sentence

    if sentence.strip() == "":                # reject empty/whitespace-only
        result = "Enter a valid sentence."
    else:
        result = len(sentence.split())         # split on whitespace, count words

    print(f"Number of Words: {result}")
    print(program_7_count_words.__doc__)


# 8. Convert String to Title Case

def program_8_title_case():
    """
    Program: Convert String to Title Case

    Description:
    Converts the first letter of every word in a string to uppercase.
    If the string is empty, it returns
    "Enter a valid string."

    Sample Test Cases:
    Test Case 1: title_case("python programming") -> Python Programming
    Test Case 2: title_case("welcome to codegnan") -> Welcome To Codegnan
    Test Case 3: title_case("") -> Enter a valid string.

    Explanation:
    Uses the title() method to capitalize the first
    letter of each word in the given string and
    returns the converted string.
    """
    s = input("Enter a string: ")   # read string

    if s.strip() == "":              # reject empty/whitespace-only
        result = "Enter a valid string."
    else:
        result = s.title()           # capitalize first letter of each word

    print(f"Title Case String: {result}")
    print(program_8_title_case.__doc__)


# 9. Check for Palindrome

def program_9_palindrome():
    """
    Program: Check for Palindrome

    Description:
    Checks whether the given input is a palindrome.
    The user can choose to check a Number, a String,
    or both Number and String.
    If the number is zero, it returns
    "Palindrome check not possible for zero."
    If the string is empty, it returns
    "Palindrome check not possible for an empty string."

    Sample Test Cases:
    Test Case 1: Choice=1, Input=121 -> Palindrome
    Test Case 2: Choice=2, Input=madam -> Palindrome
    Test Case 3: Choice=3, Number=123, String=hello
                 -> Number: Not a Palindrome
                 -> String: Not a Palindrome

    Explanation:
    Uses string slicing ([::-1]) to reverse the
    number or string and compares it with the
    original value to determine whether it is
    a palindrome.
    """
    print("===== PALINDROME MENU =====")
    print("1. Check Number Palindrome")
    print("2. Check String Palindrome")
    print("3. Check Both Number and String Palindrome")

    choice = int(input("Enter your choice: "))   # sub-menu choice

    if choice == 1:                                # number palindrome check
        n = int(input("Enter a number: "))
        if n < 0:
            result = "Enter only +ve nums"
        elif n == 0:
            result = "Palindrome check not possible for zero."
        else:
            result = "Palindrome" if str(n) == str(n)[::-1] else "Not a Palindrome"
        print(f"Number '{n}' : {result}")

    elif choice == 2:                               # string palindrome check
        s = input("Enter a string: ")
        if s.strip() == "":
            result = "Palindrome check not possible for an empty string."
        else:
            result = "Palindrome" if s.lower() == s.lower()[::-1] else "Not a Palindrome"
        print(f"String '{s}' : {result}")

    elif choice == 3:                               # both number and string
        n = int(input("Enter a number: "))
        s = input("Enter a string: ")

        if n < 0:
            n_result = "Enter only +ve nums"
        elif n == 0:
            n_result = "Palindrome check not possible for zero."
        else:
            n_result = "Palindrome" if str(n) == str(n)[::-1] else "Not a Palindrome"

        if s.strip() == "":
            s_result = "Palindrome check not possible for an empty string."
        else:
            s_result = "Palindrome" if s.lower() == s.lower()[::-1] else "Not a Palindrome"

        print(f"Number '{n}' : {n_result}")
        print(f"String '{s}' : {s_result}")

    else:                                            # invalid sub-menu choice
        print("Invalid Choice! Please enter 1, 2 or 3.")

    print(program_9_palindrome.__doc__)


# 10. Check for Prime Number

def program_10_prime_number():
    """
    Program: Check for Prime Number

    Description:
    Checks whether a given positive integer is a Prime Number.
    If the number is negative, it returns "Enter only +ve nums".
    If the number is 0 or 1, it returns
    "Prime check not possible for 0 and 1."

    Sample Test Cases:
    Test Case 1: check_prime(7) -> Prime Number
    Test Case 2: check_prime(10) -> Not a Prime Number
    Test Case 3: check_prime(0) -> Prime check not possible for 0 and 1.
    Test Case 4: check_prime(-5) -> Enter only +ve nums

    Explanation:
    Checks whether the given number is divisible
    by any number from 2 to n-1.
    If it has no divisors, it is a Prime Number.
    """
    n = int(input("Enter a number: "))    # read number

    if n < 0:                              # reject negative
        result = "Enter only +ve nums"
    elif n == 0 or n == 1:                 # 0 and 1 are not defined as prime
        result = "Prime check not possible for 0 and 1."
    else:
        result = "Prime Number"
        for i in range(2, n):              # test divisors from 2 to n-1
            if n % i == 0:
                result = "Not a Prime Number"
                break                       # divisor found, stop checking

    print(f"Result of {n}: {result}")
    print(program_10_prime_number.__doc__)


# 11. Find Factorial of a Number

def program_11_factorial():
    """
    Program: Find Factorial of a Number

    Description:
    Finds the factorial of a positive integer.
    If the number is negative, it returns
    "Enter only +ve nums".
    If the number is zero, it returns
    "The factorial of 0 is 1."

    Sample Test Cases:
    Test Case 1: factorial(5) -> 120
    Test Case 2: factorial(0) -> The factorial of 0 is 1.
    Test Case 3: factorial(-4) -> Enter only +ve nums

    Explanation:
    Multiplies the numbers from 1 up to n together
    to compute the factorial.
    """
    n = int(input("Enter a number: "))    # read number

    if n < 0:                              # reject negative
        result = "Enter only +ve nums"
    elif n == 0:                           # 0! is defined as 1
        result = "The factorial of 0 is 1."
    else:
        fact = 1
        for i in range(1, n + 1):          # multiply 1 through n
            fact *= i
        result = fact

    print(f"Factorial of {n}: {result}")
    print(program_11_factorial.__doc__)


# 12. Convert Decimal to Binary

def program_12_decimal_to_binary():
    """
    Program: Convert Decimal to Binary

    Description:
    Converts a positive decimal number into its binary equivalent.
    If the number is negative, it returns
    "Enter only +ve nums".
    If the number is zero, it returns
    "Binary of 0 is 0."

    Sample Test Cases:
    Test Case 1: decimal_to_binary(10) -> 1010
    Test Case 2: decimal_to_binary(25) -> 11001
    Test Case 3: decimal_to_binary(0) -> Binary of 0 is 0.
    Test Case 4: decimal_to_binary(-8) -> Enter only +ve nums

    Explanation:
    Repeatedly divides the decimal number by 2 and
    stores the remainders. The binary number is
    obtained by reversing the collected remainders.
    """
    n = int(input("Enter a decimal number: "))   # read decimal number

    if n < 0:                                      # reject negative
        result = "Enter only +ve nums"
    elif n == 0:                                   # special case zero
        result = "Binary of 0 is 0."
    else:
        binary = ""
        temp = n
        while temp > 0:                            # divide by 2 repeatedly
            binary = str(temp % 2) + binary         # prepend remainder
            temp //= 2
        result = binary

    print(f"Binary Number of {n}: {result}")
    print(program_12_decimal_to_binary.__doc__)


# 13. Find the Largest of Three Numbers

def program_13_largest_of_three():
    """
    Program: Find the Largest of Three Numbers

    Description:
    Finds the largest among three positive numbers.
    If any one of the numbers is negative, it returns
    "Enter only +ve nums".
    If all three numbers are zero, it returns
    "Enter Values Greater than Zero."

    Sample Test Cases:
    Test Case 1: largest_num(10, 20, 30) -> 30
    Test Case 2: largest_num(50, 25, 40) -> 50
    Test Case 3: largest_num(0, 0, 0) -> Enter Values Greater than Zero.
    Test Case 4: largest_num(-5, 10, 20) -> Enter only +ve nums

    Explanation:
    Compares the three numbers using conditional
    statements and returns the largest value.
    """
    a, b, c = map(int, input("Enter three numbers (a,b,c): ").split(","))   # read 3 numbers
    if a < 0 or b < 0 or c < 0:              # Check for negative numbers
        result = "Enter only +ve nums"

    elif a == 0 and b == 0 and c == 0:       # Check if all numbers are zero
        result = "Enter Values Greater than Zero."

    else:
        result = max(a, b, c)                # Find the largest number

    print(f"Largest Number of {a, b, c}: {result}")
    print(program_13_largest_of_three.__doc__)


# 14. Remove Duplicates from a List

def program_14_remove_duplicates():
    """
    Program: Remove Duplicates from a List

    Description:
    Removes duplicate elements from a list while preserving
    the original order of elements.
    If the list is empty, it returns
    "Enter at least one element."

    Sample Test Cases:
    Test Case 1: remove_duplicates([1,2,2,3,4,4]) -> [1, 2, 3, 4]
    Test Case 2: remove_duplicates(['a','b','a','c']) -> ['a', 'b', 'c']
    Test Case 3: remove_duplicates([]) -> Enter at least one element.

    Explanation:
    Traverses the list one element at a time.
    If an element is not already present in the new list,
    it is added. Thus, duplicate elements are removed
    while maintaining the original order.
    """
    l = input("Enter list elements separated by commas: ").split(",")   # read list
    print(f"Original List: {l}")

    if l == [''] or l == []:                    # reject empty list
        result = "Enter at least one element."
    else:
        unique_list = []
        for i in l:                              # check each element
            if i not in unique_list:             # add only if not seen before
                unique_list.append(i)
                unique_list.sort()
        result = unique_list

    print(f"List After Removing Duplicates: {result}")
    print(program_14_remove_duplicates.__doc__)
