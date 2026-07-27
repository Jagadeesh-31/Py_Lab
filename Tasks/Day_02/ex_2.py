# output: A B C D E F G H

start = input().upper()
end = input().upper()
for i in range(ord(start), ord(end) + 1):
    print(chr(i), end=" ")
print("\n")


# h f db (reverse letter range using for loop)

a = input().lower()
b = input().lower()
for i in range(ord(b), ord(a) - 1, -2):
    print(chr(i), end=" ")
print()
