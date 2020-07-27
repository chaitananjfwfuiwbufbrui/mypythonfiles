def cal(a):
    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y

    print("welcome")
    print("1 -add")
    print("2 - sub")
    print("3 - multiply")
    print(" 4  - divide")
    a = input("enter the function you want")
    x = int(input("enter the first number"))
    y = int(input("enter the second number"))
    if a == "1":
        print(x, "+", y, "=", add(x, y))
    elif a == "2":
        print(x, "-", y, "=", sub(x, y))
    elif a == "3":
        print(x, "*", y, "=", multiply(x, y))
    elif a == "4":
        print(x, "/", y, "=", divide(x, y))
    else:
        print("invalid input")
    return
print(cal(12))
