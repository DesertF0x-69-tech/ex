# Задание 1
while True:
    try:
        a = float(input("Введите первое число:"))
        b = float(input("Введите второе число:"))
        a = a + b
        b = a - b
        a = a - b
        print(a, b)
        break
    except:
        print("Введены неверные данные. Пожалуйста, введите числа заново.")

# Задание 2
while True:
    try:
        print(sum(map(int, list(input("Введите число:")))))
        break
    except:
        print("Введены неверные данные. Пожалуйста, введите число заново.")

# Задание 3
while True:
    try:
        a = float(input("Введите a:"))
        b = float(input("Введите b:"))
        c = float(input("Введите c:"))
        roots = list()
        d = b ** 2 - 4 * a * c
        if d < 0:
            print("Уравнение не имеет корней.")
            break
        elif d == 0:
            k = (-b) / (a * 2)
            roots.append(k)
            print("x равен:")
            print(roots)
            break
        elif a == 0:
            print("Уравнение не является квадратным. Пожалуйста, введите правильные данные.")
        else:
            k = str(((-b) + d ** 0.5) / (a * 2))
            i = str(((-b) - d ** 0.5) / (a * 2))
            roots.append(k)
            roots.append(i)
            print("x равен:")
            print('\n'.join(roots))
            break
    except:
        print("Введены неверные данные. Пожалуйста, введите числа заново.")