from differential_input import diff_input
import math


def euler_method(function=None, y0=None, a_b=None, n=None):
    if function is None or y0 is None or a_b is None or n is None:
        function, yzuv, a_b, n = diff_input()

    a, b = a_b
    h = (b-a)/n
    x0 = a

    answer_list = [(0, x0, *yzuv)]
    g = len(yzuv)
    while len(yzuv) < 4:
        yzuv.append(None)

    yi, zi, ui, vi = [None] * 4
    f1, f2, f3, f4 = [None] * 4
    k = [yi, zi, ui, vi]
    f = [f1, f2, f3, f4]

    for i in range(1, n+1):
        x, y, z, u, v = x0, *yzuv

        for j in range(0, g):
            f_xy = eval(function[j])
            f[j] = h * f_xy
            k[j] = yzuv[j] + f[j]
            yzuv[j] = k[j]

        x0 += h

        answer_list.append((i, x0, *k[0:g]))

    return function, answer_list


if __name__ == "__main__":
    print(euler_method())
