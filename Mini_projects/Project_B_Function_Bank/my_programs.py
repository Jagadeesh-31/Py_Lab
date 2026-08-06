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

Rules:
1. If either number is negative, display:
   "Enter only +ve Values"
2. If both numbers are zero, display:
   "Enter Values Greater than Zero to Swap numbers."

Logic:
Step 1: Read two numbers.
Step 2: Validate the input.
Step 3: Swap the numbers.
Step 4: Display the swapped values.

Code:
def program_1_swap_numbers():
    a, b = map(int, input("Enter a,b: ").split(","))
    print(f"\\nBefore Swap: a = {a}, b = {b}")
    if a < 0 or b < 0:
        print("Enter only +ve Values")
    elif a == 0 and b == 0:
        print("Enter Values Greater than Zero to Swap numbers.")
    else:
        a = a + b
        b = a - b
        a = a - b
        print(f"After Swap: a = {a}, b = {b}")

Sample Test Cases:

Test Case 1:
Input : 10,20
Output:
Before Swap: a = 10, b = 20
After Swap : a = 20, b = 10

Test Case 2:
Input : -5,10
Output:
Before Swap: a = -5, b = 10
Enter only +ve Values

Test Case 3:
Input : 0,0
Output:
Before Swap: a = 0, b = 0
Enter Values Greater than Zero to Swap numbers.

Explanation:
This program swaps two numbers using addition and subtraction
without using a temporary variable. It validates the input
before swapping the values.
    """
    # Print the documentation first
    print(program_1_swap_numbers.__doc__)
    # Then take input
    a, b = map(int, input("Enter a,b: ").split(","))
    print(f"\nBefore Swap: a = {a}, b = {b}")
    if a < 0 or b < 0:
        print("Enter only +ve Values")
    elif a == 0 and b == 0:
        print("Enter Values Greater than Zero to Swap numbers.")
    else:
        a = a + b
        b = a - b
        a = a - b
        print(f"After Swap: a = {a}, b = {b}")


# 2. GCD of Two Numbers
def program_2_gcd():
    """
Program: GCD of Two Numbers

Description:
Finds the Greatest Common Divisor (GCD) of two positive numbers
using the Euclidean Algorithm.

Rules:
1. If either number is negative, display:
   "Enter only +ve nums"
2. If both numbers are zero, display:
   "Enter Values Greater than Zero to Find Gcd Value of numbers."

Logic:
Step 1: Read two numbers.
Step 2: Store the original values for display.
Step 3: Validate the input.
Step 4: Apply the Euclidean Algorithm to compute the GCD.
Step 5: Display the result.

Code:
def program_2_gcd():
    a, b = map(int, input("Enter a,b: ").split(","))
    x, y = a, b
    if a < 0 or b < 0:
        result = "Enter only +ve nums"
    elif a == 0 and b == 0:
        result = "Enter Values Greater than Zero to Find Gcd Value of numbers."
    else:
        while b:
            a, b = b, a % b
        result = a
    print(f"GCD of {x} and {y} = {result}")

Sample Test Cases:

Test Case 1:
Input : 12,18
Output:
GCD of 12 and 18 = 6

Test Case 2:
Input : 25,15
Output:
GCD of 25 and 15 = 5

Test Case 3:
Input : -5,10
Output:
GCD of -5 and 10 = Enter only +ve nums

Explanation:
This program finds the GCD using the Euclidean Algorithm. It
repeatedly replaces the larger number with the remainder of
dividing it by the smaller number until the second number
becomes 0.
    """
    # Print the documentation first
    print(program_2_gcd.__doc__)
    # Then take input
    a, b = map(int, input("Enter a,b: ").split(","))
    x, y = a, b
    if a < 0 or b < 0:
        result = "Enter only +ve nums"
    elif a == 0 and b == 0:
        result = "Enter Values Greater than Zero to Find Gcd Value of numbers."
    else:
        while b:
            a, b = b, a % b
        result = a
    print(f"GCD of {x} and {y} = {result}")


# 3. Custom Sorting (Sort by String Length)
def program_3_custom_sort():
    """
Program: Custom Sorting (Sort by String Length)

Description:
Sorts a list of strings based on their length in ascending order.

Rules:
1. If the list is empty, display:
   "Add at least one element to the list"
2. If the list has fewer than two elements, display:
   "List Must Contain More Than One Element"

Logic:
Step 1: Read list elements.
Step 2: Display the original list.
Step 3: Validate the input.
Step 4: Sort the list by string length.
Step 5: Display the sorted list.

Code:
def program_3_custom_sort():
    l = list(input("Enter list elements separated by commas: ").split(","))
    print(f"Original List : {l}")
    if l == [''] or l == []:
        result = "Add at least one element to the list"
    elif len(l) < 2:
        result = "List Must Contain More Than One Element"
    else:
        result = sorted(l, key=len)
    print(f"Sorted by Length : {result}")

Sample Test Cases:

Test Case 1:
Input : apple,hi,banana
Output:
Original List : ['apple', 'hi', 'banana']
Sorted by Length : ['hi', 'apple', 'banana']

Test Case 2:
Input : python
Output:
Original List : ['python']
Sorted by Length : List Must Contain More Than One Element

Test Case 3:
Input : (empty)
Output:
Original List : ['']
Sorted by Length : Add at least one element to the list

Explanation:
This program uses Python's built-in sorted() function with the
key=len parameter to sort the strings according to their length.
    """
    # Print the documentation first
    print(program_3_custom_sort.__doc__)
    # Then take input
    l = list(input("Enter list elements separated by commas: ").split(","))
    print(f"Original List : {l}")
    if l == [''] or l == []:
        result = "Add at least one element to the list"
    elif len(l) < 2:
        result = "List Must Contain More Than One Element"
    else:
        result = sorted(l, key=len)
    print(f"Sorted by Length : {result}")


# 4. Reverse a Number
def program_4_reverse_number():
    """
Program: Reverse a Number

Description:
Reverses a positive integer.

Rules:
1. If the number is negative, display:
   "Enter only +ve nums"
2. If the number is zero, display:
   "Reverse not possible for zero."

Logic:
Step 1: Read a number.
Step 2: Validate the input.
Step 3: Reverse the digits using string slicing.
Step 4: Display the reversed number.

Code:
def program_4_reverse_number():
    n = int(input("Enter a number: "))
    if n < 0:
        result = "Enter only +ve nums"
    elif n == 0:
        result = "Reverse not possible for zero."
    else:
        result = str(n)[::-1]
    print(f"Reverse Number: {result}")

Sample Test Cases:

Test Case 1:
Input : 12345
Output:
Reverse Number: 54321

Test Case 2:
Input : 1000
Output:
Reverse Number: 0001

Test Case 3:
Input : -456
Output:
Reverse Number: Enter only +ve nums

Test Case 4:
Input : 0
Output:
Reverse Number: Reverse not possible for zero.

Explanation:
This program converts the number into a string, reverses it
using slicing ([::-1]), and displays the result. Since the
reversed value stays a string, a number ending in zero (like
1000) keeps its leading zero(s) when reversed (0001).
    """
    # Print the documentation first
    print(program_4_reverse_number.__doc__)
    # Then take input
    n = int(input("Enter a number: "))
    if n < 0:
        result = "Enter only +ve nums"
    elif n == 0:
        result = "Reverse not possible for zero."
    else:
        result = str(n)[::-1]
    print(f"Reverse Number: {result}")


# 5. Sum of Digits
def program_5_sum_digits():
    """
Program: Sum of Digits

Description:
Calculates the sum of digits of a positive number.

Rules:
1. If the number is negative, display:
   "Enter only +ve nums"
2. If the number is zero, display:
   "Enter Values Greater than Zero to Find Sum of Digits."

Logic:
Step 1: Read a number.
Step 2: Validate the input.
Step 3: Repeatedly extract and add the last digit until the
        number becomes zero.
Step 4: Display the sum of digits.

Code:
def program_5_sum_digits():
    n = int(input("Enter a number: "))
    if n < 0:
        result = "Enter only +ve nums"
    elif n == 0:
        result = "Enter Values Greater than Zero to Find Sum of Digits."
    else:
        result = 0
        while n > 0:
            result += n % 10
            n = n // 10
    print(f"Sum of Digits: {result}")

Sample Test Cases:

Test Case 1:
Input : 12345
Output:
Sum of Digits: 15

Test Case 2:
Input : 0
Output:
Sum of Digits: Enter Values Greater than Zero to Find Sum of Digits.

Test Case 3:
Input : -123
Output:
Sum of Digits: Enter only +ve nums

Explanation:
This program repeatedly extracts the last digit using the
modulus (%) operator, adds it to the running total, and removes
the last digit using integer division until the number becomes
zero.
    """
    # Print the documentation first
    print(program_5_sum_digits.__doc__)
    # Then take input
    n = int(input("Enter a number: "))
    if n < 0:
        result = "Enter only +ve nums"
    elif n == 0:
        result = "Enter Values Greater than Zero to Find Sum of Digits."
    else:
        result = 0
        while n > 0:
            result += n % 10
            n = n // 10
    print(f"Sum of Digits: {result}")


# 6. Count Vowels in a String
def program_6_count_vowels():
    """
Program: Count Vowels in a String

Description:
Counts the total number of vowels (a, e, i, o, u) present in a
given string.

Rules:
1. If the string is empty, display:
   "Enter a valid string."

Logic:
Step 1: Read a string.
Step 2: Validate the input.
Step 3: Check each character and count the vowels.
Step 4: Display the vowel count.

Code:
def program_6_count_vowels():
    s = input("Enter a string: ")
    if s == "":
        result = "Enter a valid string."
    else:
        count = 0
        for ch in s.lower():
            if ch in "aeiou":
                count += 1
        result = count
    print(f"Number of Vowels: {result}")

Sample Test Cases:

Test Case 1:
Input : Python
Output:
Number of Vowels: 1

Test Case 2:
Input : Education
Output:
Number of Vowels: 5

Test Case 3:
Input : (empty)
Output:
Number of Vowels: Enter a valid string.

Explanation:
This program traverses each character in the string (converted
to lowercase) and checks whether it is a vowel. If it is, the
counter is incremented and the total count is displayed.
    """
    # Print the documentation first
    print(program_6_count_vowels.__doc__)
    # Then take input
    s = input("Enter a string: ")
    if s == "":
        result = "Enter a valid string."
    else:
        count = 0
        for ch in s.lower():
            if ch in "aeiou":
                count += 1
        result = count
    print(f"Number of Vowels: {result}")


# 7. Count Words in a Sentence
def program_7_count_words():
    """
Program: Count Words in a Sentence

Description:
Counts the total number of words in a given sentence.

Rules:
1. If the sentence is empty, display:
   "Enter a valid sentence."

Logic:
Step 1: Read a sentence.
Step 2: Validate the input.
Step 3: Split the sentence into words.
Step 4: Display the word count.

Code:
def program_7_count_words():
    sentence = input("Enter a sentence: ")
    if sentence.strip() == "":
        result = "Enter a valid sentence."
    else:
        result = len(sentence.split())
    print(f"Number of Words: {result}")

Sample Test Cases:

Test Case 1:
Input : Python is easy
Output:
Number of Words: 3

Test Case 2:
Input : Hello World
Output:
Number of Words: 2

Test Case 3:
Input : (empty)
Output:
Number of Words: Enter a valid sentence.

Explanation:
This program splits the sentence into individual words using
the split() method and displays the total number of words
present in the sentence.
    """
    # Print the documentation first
    print(program_7_count_words.__doc__)
    # Then take input
    sentence = input("Enter a sentence: ")
    if sentence.strip() == "":
        result = "Enter a valid sentence."
    else:
        result = len(sentence.split())
    print(f"Number of Words: {result}")


# 8. Convert String to Title Case
def program_8_title_case():
    """
Program: Convert String to Title Case

Description:
Converts the first letter of every word in a string to uppercase.

Rules:
1. If the string is empty, display:
   "Enter a valid string."

Logic:
Step 1: Read a string.
Step 2: Validate the input.
Step 3: Convert the string to title case.
Step 4: Display the converted string.

Code:
def program_8_title_case():
    s = input("Enter a string: ")
    if s.strip() == "":
        result = "Enter a valid string."
    else:
        result = s.title()
    print(f"Title Case String: {result}")

Sample Test Cases:

Test Case 1:
Input : python programming
Output:
Title Case String: Python Programming

Test Case 2:
Input : welcome to codegnan
Output:
Title Case String: Welcome To Codegnan

Test Case 3:
Input : (empty)
Output:
Title Case String: Enter a valid string.

Explanation:
This program uses the title() method to capitalize the first
letter of each word in the given string and displays the
converted string.
    """
    # Print the documentation first
    print(program_8_title_case.__doc__)
    # Then take input
    s = input("Enter a string: ")
    if s.strip() == "":
        result = "Enter a valid string."
    else:
        result = s.title()
    print(f"Title Case String: {result}")


# 9. Check for Palindrome
def program_9_palindrome():
    """
Program: Check for Palindrome

Description:
Checks whether the given input is a palindrome. The user can
choose to check a Number, a String, or both Number and String.

Rules:
1. If the number is negative, display:
   "Enter only +ve nums"
2. If the number is zero, display:
   "Palindrome check not possible for zero."
3. If the string is empty, display:
   "Palindrome check not possible for an empty string."

Logic:
Step 1: Display the palindrome sub-menu.
Step 2: Read the user's choice.
Step 3: Read the number and/or string based on the choice.
Step 4: Validate the input.
Step 5: Check whether the value(s) read equal their own reverse.
Step 6: Display the result.

Code:
def program_9_palindrome():
    print("===== PALINDROME MENU =====")
    print("1. Check Number Palindrome")
    print("2. Check String Palindrome")
    print("3. Check Both Number and String Palindrome")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        n = int(input("Enter a number: "))
        if n < 0:
            result = "Enter only +ve nums"
        elif n == 0:
            result = "Palindrome check not possible for zero."
        else:
            result = "Palindrome" if str(n) == str(n)[::-1] else "Not a Palindrome"
        print(f"Number '{n}' : {result}")
    elif choice == 2:
        s = input("Enter a string: ")
        if s.strip() == "":
            result = "Palindrome check not possible for an empty string."
        else:
            result = "Palindrome" if s.lower() == s.lower()[::-1] else "Not a Palindrome"
        print(f"String '{s}' : {result}")
    elif choice == 3:
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
    else:
        print("Invalid Choice! Please enter 1, 2 or 3.")

Sample Test Cases:

Test Case 1:
Input : choice=1, number=121
Output:
Number '121' : Palindrome

Test Case 2:
Input : choice=2, string=madam
Output:
String 'madam' : Palindrome

Test Case 3:
Input : choice=3, number=123, string=hello
Output:
Number '123' : Not a Palindrome
String 'hello' : Not a Palindrome

Explanation:
This program uses string slicing ([::-1]) to reverse the number
or string and compares it with the original value to determine
whether it is a palindrome.
    """
    # Print the documentation first
    print(program_9_palindrome.__doc__)
    # Then take input
    print("===== PALINDROME MENU =====")
    print("1. Check Number Palindrome")
    print("2. Check String Palindrome")
    print("3. Check Both Number and String Palindrome")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        n = int(input("Enter a number: "))
        if n < 0:
            result = "Enter only +ve nums"
        elif n == 0:
            result = "Palindrome check not possible for zero."
        else:
            result = "Palindrome" if str(n) == str(n)[::-1] else "Not a Palindrome"
        print(f"Number '{n}' : {result}")
    elif choice == 2:
        s = input("Enter a string: ")
        if s.strip() == "":
            result = "Palindrome check not possible for an empty string."
        else:
            result = "Palindrome" if s.lower() == s.lower()[::-1] else "Not a Palindrome"
        print(f"String '{s}' : {result}")
    elif choice == 3:
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
    else:
        print("Invalid Choice! Please enter 1, 2 or 3.")


# 10. Check for Prime Number
def program_10_prime_number():
    """
Program: Check for Prime Number

Description:
Checks whether a given positive integer is a Prime Number.

Rules:
1. If the number is negative, display:
   "Enter only +ve nums"
2. If the number is 0 or 1, display:
   "Prime check not possible for 0 and 1."

Logic:
Step 1: Read a number.
Step 2: Validate the input.
Step 3: Check divisibility by every number from 2 up to n-1.
Step 4: Display whether the number is prime.

Code:
def program_10_prime_number():
    n = int(input("Enter a number: "))
    if n < 0:
        result = "Enter only +ve nums"
    elif n == 0 or n == 1:
        result = "Prime check not possible for 0 and 1."
    else:
        result = "Prime Number"
        for i in range(2, n):
            if n % i == 0:
                result = "Not a Prime Number"
                break
    print(f"Result of {n}: {result}")

Sample Test Cases:

Test Case 1:
Input : 7
Output:
Result of 7: Prime Number

Test Case 2:
Input : 10
Output:
Result of 10: Not a Prime Number

Test Case 3:
Input : 0
Output:
Result of 0: Prime check not possible for 0 and 1.

Test Case 4:
Input : -5
Output:
Result of -5: Enter only +ve nums

Explanation:
This program checks whether the given number is divisible by
any number from 2 to n-1. If it has no divisors in that range,
it is a Prime Number.
    """
    # Print the documentation first
    print(program_10_prime_number.__doc__)
    # Then take input
    n = int(input("Enter a number: "))
    if n < 0:
        result = "Enter only +ve nums"
    elif n == 0 or n == 1:
        result = "Prime check not possible for 0 and 1."
    else:
        result = "Prime Number"
        for i in range(2, n):
            if n % i == 0:
                result = "Not a Prime Number"
                break
    print(f"Result of {n}: {result}")


# 11. Find Factorial of a Number
def program_11_factorial():
    """
Program: Find Factorial of a Number

Description:
Finds the factorial of a positive integer.

Rules:
1. If the number is negative, display:
   "Enter only +ve nums"
2. If the number is zero, display:
   "The factorial of 0 is 1."

Logic:
Step 1: Read a number.
Step 2: Validate the input.
Step 3: Multiply the numbers from 1 up to n together.
Step 4: Display the factorial.

Code:
def program_11_factorial():
    n = int(input("Enter a number: "))
    if n < 0:
        result = "Enter only +ve nums"
    elif n == 0:
        result = "The factorial of 0 is 1."
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        result = fact
    print(f"Factorial of {n}: {result}")

Sample Test Cases:

Test Case 1:
Input : 5
Output:
Factorial of 5: 120

Test Case 2:
Input : 0
Output:
Factorial of 0: The factorial of 0 is 1.

Test Case 3:
Input : -4
Output:
Factorial of -4: Enter only +ve nums

Explanation:
This program multiplies the numbers from 1 through n together
in a loop to compute the factorial.
    """
    # Print the documentation first
    print(program_11_factorial.__doc__)
    # Then take input
    n = int(input("Enter a number: "))
    if n < 0:
        result = "Enter only +ve nums"
    elif n == 0:
        result = "The factorial of 0 is 1."
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        result = fact
    print(f"Factorial of {n}: {result}")


# 12. Convert Decimal to Binary
def program_12_decimal_to_binary():
    """
Program: Convert Decimal to Binary

Description:
Converts a positive decimal number into its binary equivalent.

Rules:
1. If the number is negative, display:
   "Enter only +ve nums"
2. If the number is zero, display:
   "Binary of 0 is 0."

Logic:
Step 1: Read a decimal number.
Step 2: Validate the input.
Step 3: Repeatedly divide the number by 2 and collect the
        remainders.
Step 4: Display the binary equivalent.

Code:
def program_12_decimal_to_binary():
    n = int(input("Enter a decimal number: "))
    if n < 0:
        result = "Enter only +ve nums"
    elif n == 0:
        result = "Binary of 0 is 0."
    else:
        binary = ""
        temp = n
        while temp > 0:
            binary = str(temp % 2) + binary
            temp //= 2
        result = binary
    print(f"Binary Number of {n}: {result}")

Sample Test Cases:

Test Case 1:
Input : 10
Output:
Binary Number of 10: 1010

Test Case 2:
Input : 25
Output:
Binary Number of 25: 11001

Test Case 3:
Input : 0
Output:
Binary Number of 0: Binary of 0 is 0.

Test Case 4:
Input : -8
Output:
Binary Number of -8: Enter only +ve nums

Explanation:
This program repeatedly divides the decimal number by 2 and
stores the remainders. The binary number is obtained by
prepending each new remainder ahead of the ones already
collected.
    """
    # Print the documentation first
    print(program_12_decimal_to_binary.__doc__)
    # Then take input
    n = int(input("Enter a decimal number: "))
    if n < 0:
        result = "Enter only +ve nums"
    elif n == 0:
        result = "Binary of 0 is 0."
    else:
        binary = ""
        temp = n
        while temp > 0:
            binary = str(temp % 2) + binary
            temp //= 2
        result = binary
    print(f"Binary Number of {n}: {result}")


# 13. Find the Largest of Three Numbers
def program_13_largest_of_three():
    """
Program: Find the Largest of Three Numbers

Description:
Finds the largest among three positive numbers.

Rules:
1. If any one of the numbers is negative, display:
   "Enter only +ve nums"
2. If all three numbers are zero, display:
   "Enter Values Greater than Zero."

Logic:
Step 1: Read three numbers.
Step 2: Validate the input.
Step 3: Compare the three numbers.
Step 4: Display the largest number.

Code:
def program_13_largest_of_three():
    a, b, c = map(int, input("Enter three numbers (a,b,c): ").split(","))
    if a < 0 or b < 0 or c < 0:
        result = "Enter only +ve nums"
    elif a == 0 and b == 0 and c == 0:
        result = "Enter Values Greater than Zero."
    else:
        result = max(a, b, c)
    print(f"Largest Number of {a, b, c}: {result}")

Sample Test Cases:

Test Case 1:
Input : 10,20,30
Output:
Largest Number of (10, 20, 30): 30

Test Case 2:
Input : 50,25,40
Output:
Largest Number of (50, 25, 40): 50

Test Case 3:
Input : 0,0,0
Output:
Largest Number of (0, 0, 0): Enter Values Greater than Zero.

Test Case 4:
Input : -5,10,20
Output:
Largest Number of (-5, 10, 20): Enter only +ve nums

Explanation:
This program compares the three numbers using conditional
statements and the built-in max() function to find and display
the largest value.
    """
    # Print the documentation first
    print(program_13_largest_of_three.__doc__)
    # Then take input
    a, b, c = map(int, input("Enter three numbers (a,b,c): ").split(","))
    if a < 0 or b < 0 or c < 0:
        result = "Enter only +ve nums"
    elif a == 0 and b == 0 and c == 0:
        result = "Enter Values Greater than Zero."
    else:
        result = max(a, b, c)
    print(f"Largest Number of {a, b, c}: {result}")


# 14. Remove Duplicates from a List
def program_14_remove_duplicates():
    """
Program: Remove Duplicates from a List

Description:
Removes duplicate elements from a list while keeping only the
first occurrence of each value.

Rules:
1. If the list is empty, display:
   "Enter at least one element."

Logic:
Step 1: Read list elements.
Step 2: Display the original list.
Step 3: Validate the input.
Step 4: Traverse the list, adding each element to a new list
        only if it hasn't been added before, then sort.
Step 5: Display the list after removing duplicates.

Code:
def program_14_remove_duplicates():
    l = input("Enter list elements separated by commas: ").split(",")
    print(f"Original List: {l}")
    if l == [''] or l == []:
        result = "Enter at least one element."
    else:
        unique_list = []
        for i in l:
            if i not in unique_list:
                unique_list.append(i)
                unique_list.sort()
        result = unique_list
    print(f"List After Removing Duplicates: {result}")

Sample Test Cases:

Test Case 1:
Input : 1,2,2,3,4,4
Output:
Original List: ['1', '2', '2', '3', '4', '4']
List After Removing Duplicates: ['1', '2', '3', '4']

Test Case 2:
Input : a,b,a,c
Output:
Original List: ['a', 'b', 'a', 'c']
List After Removing Duplicates: ['a', 'b', 'c']

Test Case 3:
Input : (empty)
Output:
Original List: ['']
List After Removing Duplicates: Enter at least one element.

Explanation:
This program traverses the list one element at a time. If an
element is not already present in the new list, it is added and
the new list is re-sorted, so duplicates never appear in the
final result.
    """
    # Print the documentation first
    print(program_14_remove_duplicates.__doc__)
    # Then take input
    l = input("Enter list elements separated by commas: ").split(",")
    print(f"Original List: {l}")
    if l == [''] or l == []:
        result = "Enter at least one element."
    else:
        unique_list = []
        for i in l:
            if i not in unique_list:
                unique_list.append(i)
                unique_list.sort()
        result = unique_list
    print(f"List After Removing Duplicates: {result}")
