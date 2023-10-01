from differential_input import diff_input
import math
from copy import deepcopy


def runge_kutta(function=None, yzuv=None, a_b=None, n=None):
    if function is None or yzuv is None or a_b is None or n is None:
        function, yzuv, a_b, n = diff_input()

    a, b = a_b
    h = (b-a)/n
    x0 = a

    answer_list = [(0, x0, *yzuv)]
    g = len(yzuv)
    while len(yzuv) < 4:
        yzuv.append(None)

    yi, zi, ui, vi = [None] * 4
    func_i = [yi, zi, ui, vi]
    k_i = [[None] * 4 for i in range(g)]
    for i in range(1, n+1):
        for j in range(0, g):
            x, y, z, u, v = x0, *yzuv
            f_xy = eval(function[j])
            k_i[j][0] = h * f_xy

        new_yzuv = deepcopy(yzuv)
        new_yzuv[0:g] = [(yzuv[j] + k_i[j][0]/2) for j in range(g)]
        for j in range(0, g):
            x, y, z, u, v = x0 + h/2, *new_yzuv
            f_xy = eval(function[j])
            k_i[j][1] = h * f_xy

        new_yzuv = deepcopy(yzuv)
        new_yzuv[0:g] = [(yzuv[j] + k_i[j][1] / 2) for j in range(g)]
        for j in range(0, g):
            x, y, z, u, v = x0 + h/2, *new_yzuv
            f_xy = eval(function[j])
            k_i[j][2] = h * f_xy

        new_yzuv = deepcopy(yzuv)
        new_yzuv[0:g] = [(yzuv[j] + k_i[j][2]) for j in range(g)]
        for j in range(0, g):
            x, y, z, u, v = x0 + h, *new_yzuv
            f_xy = eval(function[j])
            k_i[j][3] = h * f_xy

        for j in range(g):
            func_i[j] = yzuv[j] + (1/6)*(k_i[j][0] + 2*k_i[j][1] + 2*k_i[j][2] + k_i[j][3])
            yzuv[j] = func_i[j]

        x0 += h
        answer_list.append((i, x0, *func_i[0:g]))

    return answer_list


if __name__ == "__main__":
    print(runge_kutta(["math.sin(x+y)"], [0], [0, 1], 10))
