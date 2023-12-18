# Multiple exceptions in a try

def check_vote():
    try:
        age = int(input("Enter your age: "))
        if age > 18:
            print("Eligible to vote")
        else:
            print("Not Eligible to vote")
    except ValueError:
        print("Input must be a number")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("Rest of the code ...")

check_vote()

