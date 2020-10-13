#Kalkul
z = str(input("Какую операцию вы хотите провести? +,-,*,/,V,S:"))
if z == ("+"):
    a = input("Введите a:")
    b = input("Введите b:")
    a = int(a)
    b = int(b)
    print("Результат" + a + b)
elif z == ("-"):
    a = input("Введите a:")
    b = input("Введите b:")
    a = int(a)
    b = int(b)
    print("Результат:" + a - b)
elif z == ("*"):
    a = input("Введите a:")
    b = input("Введите b:")
    a = int(a)
    b = int(b)
    print("Результат" + str(a * b))
elif z == ("/"):
    a = input("Введите a:")
    b = input("Введите b:")
    a = int(a)
    b = int(b)
    print("Результат:"+ str(a / b) )
elif z == ("V"):
    a = input("Введите число для выражения корня:")
    a = int(a)
    c = str(a ** 0.5 )
    print("Результат:" + c)
elif z == ("S"):
    a = input("Введите число:")
    b = input("Введите степень")
    a = int(a)
    b = int(b)
    c = str(a ** b)
    print("Результат:" + c)
else:
    print("Сбой!...")