from Euler import euler_method
import math


def euler_caushy(function=None, y0=None, a_b=None, n=None):
    if function is None or y0 is None or a_b is None or n is None:
        euler = euler_method()
        function = euler[0]
        table_euler = euler[1]
    else:
        table_euler = euler_method(function, y0, a_b, n)[1]

    a = table_euler[0][1]
    b = table_euler[-1][1]
    n = len(table_euler) - 1
    h = (b - a) / n

    yzuv = table_euler[0][2:]
    yzuv = list(yzuv)
    x0 = a

    answer_list = [(0, x0, *yzuv)]
    g = len(yzuv)
    while len(yzuv) < 4:
        yzuv.append(None)

    f1, f2, f3, f4 = [None] * 4
    f = [f1, f2, f3, f4]
    new_f1, new_f2, new_f3, new_f4 = [None] * 4
    new_f = [new_f1, new_f2, new_f3, new_f4]
    yi, zi, ui, vi = [None] * 4
    k = [yi, zi, ui, vi]

    for i in range(1, n+1):
        x, y, z, u, v = x0, *yzuv

        for j in range(g):
            f[j] = eval(function[j])

        new_yzuv = yzuv
        new_yzuv[0:g] = table_euler[i][2:]
        x, y, z, u, v = x0+h, *new_yzuv
        for j in range(g):
            new_f[j] = eval(function[j])

        for j in range(g):
            k[j] = yzuv[j] + (h/2) * (f[j] + new_f[j])
            yzuv[j] = k[j]

        x0 += h
        answer_list.append((i, x0, *k[0:g]))

    return answer_list


if __name__ == "__main__":
    print(euler_caushy())

