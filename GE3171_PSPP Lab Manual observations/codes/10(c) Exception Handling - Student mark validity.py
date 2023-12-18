# 10(c) Program to check the validity of the student mark entry
def checkmark():
    try:
        mark = int(input("Enter student mark : "))
        if mark > 0 and mark <= 100:
            print("Marks Entered is ", mark)
        else:
            raise NameError("Invalid mark ")
    except ValueError:
        print("Input must be number")
    except IOError:
        print("IO Error")
    print("successfull")


checkmark()
