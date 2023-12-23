from math import * # Импорт библиотеки math


alpha = int(input("Необходимо ввести угол в радианах: ")) # Ввод угла
a1 = cos(alpha) + sin(alpha) + cos(3 * alpha) + sin(3 * alpha) # Вычисление значений функций
a2 = 2 * (2 ** 0.5) * cos(alpha) * sin((pi / 4) + 2 * alpha) # Вычисление значений функций
print(a1, a2) # Вывод результатов
