while True:
    num = int(input("Введите число: "))
    if num == 7:
        print("Good bye!")
    elif num > 0:
        print("Number is positive")
    elif num < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")
    break