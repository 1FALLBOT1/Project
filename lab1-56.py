import math

def task_1():
    print("\n--- Задание №1: Прямоугольник ---")
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    area = a * b
    perimeter = 2 * (a + b)
    print(f"Площадь прямоугольника: {area}")
    print(f"Периметр прямоугольника: {perimeter}")

def task_2():
    print("\n--- Задание №2: Круг ---")
    R = float(input("Введите радиус круга R: "))
    circumference = 2 * math.pi * R
    area = math.pi * (R ** 2)
    print(f"Длина окружности: {circumference:.4f}")
    print(f"Площадь круга: {area:.4f}")

def task_3():
    print("\n--- Задание №3: Температура ---")
    celsius = float(input("Введите температуру в градусах Цельсия (°C): "))
    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.15
    print(f"Температура по Фаренгейту: {fahrenheit:.2f} °F")
    print(f"Температура по Кельвину: {kelvin:.2f} K")

def task_4():
    print("\n--- Задание №4: Средние ---")
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    arithmetic_mean = (num1 + num2) / 2
    geometric_mean = math.sqrt(num1 * num2)
    print(f"Среднее арифметическое: {arithmetic_mean}")
    print(f"Среднее геометрическое: {geometric_mean:.4f}")

def task_5():
    print("\n--- Задание №5: Расстояние ---")
    km = float(input("Введите расстояние в километрах: "))
    miles = km * 0.621371
    feet = km * 3280.84
    yards = km * 1093.61
    print(f"Расстояние в милях: {miles:.4f} mi")
    print(f"Расстояние в футах: {feet:.2f} ft")
    print(f"Расстояние в ярдах: {yards:.2f} yd")

def task_6():
    print("\n--- Задание №6: Покупка ---")
    n = int(input("Введите количество товаров (n): "))
    p = float(input("Введите цену товара (p): "))
    s = float(input("Введите размер скидки в процентах (s): "))
    full_price = n * p
    discount_amount = full_price * (s / 100)
    final_price = full_price - discount_amount
    print(f"Общая стоимость без скидки: {full_price:.2f}")
    print(f"Сумма скидки: {discount_amount:.2f}")
    print(f"Итоговая стоимость к оплате: {final_price:.2f}")

def task_7():
    print("\n--- Задание №7: Треугольник ---")
    katet1 = float(input("Введите длину первого катета: "))
    katet2 = float(input("Введите длину второго катета: "))
    hypotenuse = math.sqrt(katet1**2 + katet2**2)
    area = 0.5 * katet1 * katet2
    print(f"Длина гипотенузы: {hypotenuse:.4f}")
    print(f"Площадь прямоугольного треугольника: {area}")

def task_8():
    print("\n--- Задание №8: Доли ---")
    S = float(input("Введите общую сумму для распределения (S): "))
    vklad1 = float(input("Введите вклад 1-го участника: "))
    vklad2 = float(input("Введите вклад 2-го участника: "))
    vklad3 = float(input("Введите вклад 3-го участника: "))
    total_vklad = vklad1 + vklad2 + vklad3
    share1 = (vklad1 / total_vklad) * S
    share2 = (vklad2 / total_vklad) * S
    share3 = (vklad3 / total_vklad) * S
    print(f"Доля 1-го участника: {share1:.2f}")
    print(f"Доля 2-го участника: {share2:.2f}")
    print(f"Доля 3-го участника: {share3:.2f}")

def task_9():
    print("\n--- Задание №9: Масса ---")
    kg = float(input("Введите массу в килограммах: "))
    pounds = kg * 2.20462
    ounces = kg * 35.274
    stones = kg * 0.157473
    print(f"Масса в фунтах: {pounds:.4f} lb")
    print(f"Масса в унциях: {ounces:.4f} oz")
    print(f"Масса в стоунах: {stones:.4f} st")

def task_10():
    print("\n--- Задание №10: Цилиндр ---")
    R = float(input("Введите радиус основания цилиндра (R): "))
    H = float(input("Введите высоту цилиндра (H): "))
    base_area = math.pi * (R ** 2)
    volume = base_area * H
    surface_area = 2 * math.pi * R * (R + H)
    print(f"Объём цилиндра: {volume:.4f}")
    print(f"Полная площадь поверхности: {surface_area:.4f}")

def main():
    while True:
        print("\n" + "="*30)
        print("ЛАБОРАТОРНАЯ РАБОТА №1")
        print("="*30)
        print("Выберите номер задания (1-10) или 0 для выхода:")
        
        try:
            choice = int(input("Введите номер: "))
            if choice == 0:
                print("Выход из программы. Хорошего дня!")
                break
            elif choice == 1: task_1()
            elif choice == 2: task_2()
            elif choice == 3: task_3()
            elif choice == 4: task_4()
            elif choice == 5: task_5()
            elif choice == 6: task_6()
            elif choice == 7: task_7()
            elif choice == 8: task_8()
            elif choice == 9: task_9()
            elif choice == 10: task_10()
            else:
                print("Ошибка: выберите число от 1 до 10.")
        except ValueError:
            print("Ошибка: введено не число. Попробуйте еще раз.")

if __name__ == '__main__':
    main()
