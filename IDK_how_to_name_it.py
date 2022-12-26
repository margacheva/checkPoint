# 1
def triangles(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a == b or b == c or a == c:
            if a == b == c:
                print('Равносторонний треугольник')
            else:
                print('Равнобедренный треугольник')
        else:
            print('Разносторонний треугольник')
    else:
        print('Не сущестует')


triangles(3, -5, 42)
