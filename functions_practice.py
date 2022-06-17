def hello():
    print("Greetings!\n")
    return

def pack(arg1, arg2, arg3):
    singleList = [arg1, arg2, arg3]
    return singleList


def eat_lunch(listVar):
    if len(listVar) == 0:
        print("My lunchbox is empty!\n")
        return
    
    else:
        for i in range(len(listVar)):
            if i == 0:
                print("%d. First I eat %s\n" %(i+1, listVar[0]))
            else:
                print("%d. Next I eat %s\n" %(i+1, listVar[i]))
    return

# Calling hello function, does not return anything
print("\nHello Function:\n----------------------------------")
hello()


# Example of running eat_lunch with empty list
print("\nPassing an empty list to function:\n----------------------------------")
listVar = []
eat_lunch(listVar)


# Example of running eat_lunch with pack function
print("\nPassing pack function to function:\n----------------------------------")
eat_lunch(pack("Apple", "Sandwhich", "Chips"))


# Example of running eat_lunch with only 1 list item
print("\nPassing list of 1 item to function:\n-----------------------------------")
eat_lunch(["Cake"])

# Example of running eat_lunch with only 5 list item
print("\nPassing list of 5 item to function:\n-----------------------------------")
eat_lunch(["Cake", "Apple", "Cookie", "Sandwhich", "Chips"])