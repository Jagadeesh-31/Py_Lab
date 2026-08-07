severity = input().lower()
wait_time = int(input())
if wait_time < 0 :
    print("Value must  be in +ve")
elif wait_time==0:
    print("Value  must be greater than 0")
else:
    if severity == 'critical':
        if wait_time > 30 and wait_time < 60:
            print("Emergency Priority")
        else:
            print("High Priority")
    elif severity  == 'serious':
        if wait_time > 60 and wait_time < 120:
            print("High Priority")
        else:
            print("Medium Priority")
    elif severity=='stable':
        if wait_time >120:
            print("Medium Priority")
        else:
            print("Low Priority")
    else:
        print("Invalid Severity Level")

