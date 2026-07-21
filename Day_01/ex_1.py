# student marks gradeb checker

marks = int(input("Enter marks: "))
if marks > 100 or marks >0:
    if marks >= 90:
        print("Grade: A")
        print("Remark: Outstanding!")
    elif marks >= 80:
            print("Grade: B")
            print("Remark: Excellent!")
    elif marks >= 70:
                print("Grade: C")
                print("Remark: Good")
    elif marks >= 60:
                    print("Grade: D")
                    print("Remark: Fair, needs improvement")
    elif marks >= 50:
                        print("Grade: E")
                        print("Remark: Poor, needs serious improvement")
    elif marks >= 0:
                            print("Grade: F")
                            print("Remark: Failed, needs to reappear")
else:
    print("Invalid marks entered")
