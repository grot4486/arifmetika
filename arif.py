from math import *


alpha = int(input("Необходимо ввести угол в радианах: "))
a1 = cos(alpha) + sin(alpha) + cos(3 * alpha) + sin(3 * alpha)
a2 = 2 * (2 ** 0.5) * cos(alpha) * sin((pi / 4) + 2 * alpha)
print(a1, a2)
