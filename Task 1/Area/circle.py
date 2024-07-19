import math

# В этой функции мы вычисляем площадь треугольника
def area(r):
    return r*r*math.pi

# В этой функции мы проверяем, ввёл ли польщз именно цифры
def check_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
    # Основная функция
def circle():

    a = input("\nВведите радиус круга: ")

    if check_number(a):
        a = float(a)
        return print ("\nПлощадь круга равна ",area(a))
    else:
        return print("\nПожалуйста, введите только числа для радиуса")
