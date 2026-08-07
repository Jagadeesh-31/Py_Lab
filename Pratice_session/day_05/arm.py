start = int(input())
end = int(input())

num = start

while num <= end:
    tmp = num
    digits = 0

    while tmp > 0:
        digits += 1
        tmp = tmp // 10

    tmp = num
    total = 0

    while tmp > 0:
        dg = tmp % 10
        total += dg ** digits
        tmp = tmp // 10

    if total == num:
        print(num, end=" ")

    num += 1
