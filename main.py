print("------------------------------------------------")
print("Hello Friend, I will calculate anything you want")
print("------------------------------------------------")
print("What do you want to do?")
print("1.Addition")
print("2.Subtraction")
a = int(input("Pick 1 or 2\n"))
if a == 1:
    b = int(input("Enter the First Number\n"))
    c = int(input("Enter the Second Number\n"))
    s = b+c
    print("The Result is",s,"!")
if a == 2:
    d = int(input("Enter the First Number\n"))
    e = int(input("Enter the Second Number\n"))
    f = d-e
    print("The Result is",f,"!")
if a != 1 and a != 2:
    print("That's not a valid option")
g = input("Do you want to end or continue?\n")
if g == "end":
    print("Goodbye!")
while g != "end" and g != "continue":
    print("That's not a valid option")
    g = input("Do you want to end or continue?\n")
while g == "continue":
    print("What do you want to do?")
    print("1.Addition")
    print("2.Subtraction")
    a = int(input("Pick 1 or 2\n"))
    if a == 1:
        b = int(input("Enter the First Number\n"))
        c = int(input("Enter the Second Number\n"))
        s = b+c
        print("The Result is",s,"!")
    if a == 2:
        d = int(input("Enter the First Number\n"))
        e = int(input("Enter the Second Number\n"))
        f = d-e
        print("The Result is",f,"!")
    if a != 1 and a != 2:
        print("Thats not a valid option")
    g = input("Do you want to end or continue?\n")
    if g == "end":
        print("Goodbye!")
    while g != "continue" and g != "end":
        print("That's not a valid option\n")
        g = input("Do you want to end or continue?\n")