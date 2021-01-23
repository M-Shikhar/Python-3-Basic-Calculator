print("------------------------------------------------")
print("Hello Friend, I will calculate anything you want")
print("------------------------------------------------")
print("What do you want to do?")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
a = int(input("Pick 1, 2, 3 or 4\n"))
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
if a == 3:
    h = int(input("Enter the First Number\n"))
    i = int(input("Enter the second Number\n"))
    j = h*i
    print("The Result is",j,"!")
if a == 4:
    k = int(input("Enter the First Number\n"))
    l = int(input("Enter the Second Number\n"))
    m = k/l
    print("The Result is",m,"!")
if a != 1 and a != 2 and a != 3 and a!= 4:
    print("That's not a valid option")
g = input("Do you want to end or continue?\n")
while g != "end" and g != "continue":
    print("That's not a valid option")
    g = input("Do you want to end or continue?\n")
if g == "end":
    print("Goodbye!")
while g == "continue":
    print("What do you want to do?")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    a = int(input("Pick 1, 2, 3 or 4\n"))
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
    if a == 3:
        h = int(input("Enter the First Number\n"))
        i = int(input("Enter the second Number\n"))
        j = h*i
        print("The Result is",j,"!")
    if a == 4:
        k = int(input("Enter the First Number\n"))
        l = int(input("Enter the Second Number\n"))
        m = k/l
        print("The Result is",m,"!")
    if a != 1 and a != 2 and a != 3 and a != 4:
        print("Thats not a valid option")
    g = input("Do you want to end or continue?\n")
    while g != "continue" and g != "end":
        print("That's not a valid option\n")
        g = input("Do you want to end or continue?\n")
    if g == "end":
        print("Goodbye!")
