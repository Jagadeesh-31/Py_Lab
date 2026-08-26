class StuData:
    """Student Information"""

    def __init__(self, name="", course="", branch=""):
        self.name = name
        self.course = course
        self.branch = branch

    def choice(self):
        choice = int(input("Enter your choice (1=Entry, 0=Exit, 2=Empty): "))
        if choice == 1:
            print("*" * 5, "Enter your data", "*" * 5)
            self.name = input("Enter stu_name: ")
            self.course = input("Enter stu_course: ")
            self.branch = input("Enter stu_branch: ")
        elif choice == 0:
            print("Exiting program. Goodbye!")
            exit()
        elif choice == 2:
            print("Empty data")
        else:
            print("Invalid Choice")

    def dis(self):
        if self.name == "" and self.course == "" and self.branch == "":
            print("Empty")
        else:
            print(f"Student name is: {self.name}")
            print(f"Student course is: {self.course}")
            print(f"Student branch is: {self.branch}")


print(StuData.__doc__)
stu1 = StuData()
stu1.choice()
stu1.dis()
print(stu1.__dict__)
