import Area.circle as circle
import Area.triangle as triangle

def main():
    str=input("\nВыберите площадь чего вы хотите вычислить:\n\n (Введите цифру) \n\n 1.Треугольник \n 2.Круг\n\n")

    if str == "1":
        triangle.triangle()
    elif str == "2":
        circle.circle()
    else:
        str=input("Вы ввели неверное значение!\n\n Выберите площадь чего вы хотите вычислить:\n\n (Введите цифру) \n\n 1.Треугольник \n 2.Круг\n\n")

while 1:
    main()