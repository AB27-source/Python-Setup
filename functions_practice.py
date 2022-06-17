def hello():
    return

def pack(arg1, arg2, arg3):
    singleList = [arg1, arg2, arg3]
    return singleList


def eat_lunch(listVar):
    if len(listVar) == 0:
        print("My lunchbox is empty!")
    else:
        print("First I eat %s\nNext I eat %s\nLastly I eat %s\n" %(listVar[0], listVar[1], listVar[2]))

# Calling hello function, does not return anything
hello()

# printing new line
print("\n")

# Example of running eat_lunch with empty list
print("Passing an empty list to function:\n----------------------------------")
listVar = []
eat_lunch(listVar)

# printing new line
print("\n")

# Example of running eat_lunch with pack function
print("Passing pack function to function:\n----------------------------------")
eat_lunch(pack("Apple", "Sandwhich", "Chips"))