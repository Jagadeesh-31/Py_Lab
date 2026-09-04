# Pattern 1

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = int(input("Enter number of rows: "))
for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()

# Pattern 2
# A
# A B
# A B C
# A B C D
# A B C D E

for i in range(ord('A'), ord('F')):

    for j in range(ord('A'), i + 1):
        print(chr(j), end=" ")

    print()

# Pattern 3
#
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):

    for j in range(1, n + 1):

        if j <= n - i:
            print(" ", end="")

        else:
            print("*", end=" ")

    print()


