# Задание 1
try:
    x = int(input())
    y = int(input())
    # Сторона света, куда мы смотрим
    side = "север"
    # Минимальное количество указаний, чтобы достичь клада
    min = 0
    # Ввод направления движения ("вперёд", "разворот", "налево", "направо")
    napr = input()
    while True:
        # Если заданные координаты совпадают с начальными, то выводится 0 указаний и начальная сторона света
        if x == 0 and y == 0:
            print(min)
            print(side)
            break
        # Вывод кол-ва указаний и стороны света после слова "стоп"
        if napr == "стоп":
            print(min)
            print(side)
            break
        else:
            # Добавление 1 к минимальномым указаниям
            min += 1
            # При вводе "вперёд" необходимо ввести количество шагов
            if napr == "вперёд":
                steps = int(input())
            # При повороте на налево строна света, куда направлен взгляд, меняется в соответствии с текущем направлением
            elif napr == "налево":
                if side == "север":
                    side = "запад"
                elif side == "запад":
                    side = "юг"
                elif side == "юг":
                    side = "восток"
                elif side == "восток":
                    side = "север"
            # При повороте на направо строна света меняется в соответствии с текущем направлением
            elif napr == "направо":
                if side == "север":
                    side = "восток"
                if side == "восток":
                    side = "юг"
                if side == "юг":
                    side = "запад"
                if side == "запад":
                    side = "север"
            # При развороте сторона света меняется на противоположную
            elif napr == "разворот":
                if side == "север":
                    side = "юг"
                if side == "юг":
                    side = "север"
                if side == "восток":
                    side = "запад"
                if side == "запад":
                    side = "восток"
            napr = input()
except:
    print("Error")

# Задание 2
try:
    d = int(input())
    m = int(input())
    g = int(input())
    # Если номер месяца больше 2, то значение по Древне Римскому календарю будет на 2 меньше
    if m > 2:
        m -= 2
    # В Древнем Риме январь - 11 число, февраль - 12, добавляем к каждому значению 10 и возвращаемся на год назад
    else:
        m += 10
        g -= 1
    # Находим номер года в столетии
    y = g % 100
    # Находим кол-во столетий
    c = g // 100
    num = d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)
    # Нахождение остатка от результата по формуле выше, вывод дня недели, в который родился абориген
    print(num % 7)
except:
    print("Error")

# Задание 3
try:
    a = str(input())
    # Вывод третьего символа строки
    print(a[2])
    # Вывод предпоследнего символа строки
    print(a[-2])
    # Вывод символом с первого по пятый
    print(a[0:5])
    # Вывод символов строки, кроме двух последних
    print(a[0:-2])
    # Вывод символов с чётным индексом
    print(a[0::2])
    # Вывод символов строки с нечётным индексом
    print(a[1::2])
    # Вывод строки в обратном порядке
    print(a[::-1])
    # Вывод строки в обратном порядке через один символ
    print(a[::-2])
    print(len(a))
except:
    print("Error")