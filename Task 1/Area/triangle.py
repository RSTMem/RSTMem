import math

# В этой функции мы вычисляем площадь треугольника
def area(a1, a2, a3):
    p = (a1 + a2 + a3) / 2
    return math.sqrt(p * (p - a1) * (p - a2) * (p - a3))

# В этой функции мы проверяем, ввёл ли пользователь именно цифры
def check_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# В этой функции мы проверяем, ввёл ли пользователь такие длины сторон, из которых реально построить треугольник
def is_triangle(a1, a2, a3): 
    return a1 + a2 > a3 and a1 + a3 > a2 and a2 + a3 > a1

# В этой функции мы проверяем, прямоугольный ли треугольник
def check_right(a1, a2, a3):
    a1, a2, a3 = sorted([a1, a2, a3])
    return math.isclose(a1**2 + a2**2, a3**2)

# Основная функция
def triangle():
    a1 = input("\nВведите длину первой стороны треугольника: ")
    a2 = input("Введите длину второй стороны треугольника: ")
    a3 = input("Введите длину третьей стороны треугольника: ")

    if check_number(a1) and check_number(a2) and check_number(a3):
        a1, a2, a3 = float(a1), float(a2), float(a3)
        if is_triangle(a1, a2, a3):
            triangle_area = area(a1, a2, a3)
            if check_right(a1, a2, a3):
                print(f"\nПлощадь прямоугольного треугольника равна {triangle_area}")
            else:
                print(f"\nПлощадь треугольника равна {triangle_area}")
            
        else:
            print("\nТреугольника с такими сторонами не существует")
    else:
        print("\nПожалуйста, введите только числа для всех сторон треугольника")
