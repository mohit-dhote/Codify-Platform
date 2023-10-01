import random
import math


def zerodiv(fun):
    count = 0
    for j in range(30):
        x, y, z, u, v = [random.randint(-100001, 100001)] * 5
        try:
            eval(fun)
        except ZeroDivisionError:
            count += 1
        except ValueError:
            continue
    if count == 20:
        return True
    return False


def valuer(fun):
    count = 0
    for j in range(30):
        x, y, z, u, v = [random.randint(-100001, 100001)] * 5
        try:
            eval(fun)
        except ValueError:
            count += 1
        except ZeroDivisionError:
            continue
    if count == 20:
        return True
    return False


def diff_input():
    """
    Ввод для дифференциального уравнение I порядка вида: y'=f(x,y) или систем таких уравнений
    Либо для ДУ II порядка вида: y'=f(x,y,y')
    Начальное условие вида: y(m) = ... | x ∈ [m, ...]
    Точность задаётся целым числом
    :return: [f(x,y,...),...] | [y(0), z[0],...] | x∈[a, b] | точность(n)
    """

    flag = False
    while not flag:
        system = None
        print('Введите кол-во уравнений в системе (от 1 до 4): ')
        while system is None:
            try:
                count = int(input('Количество уравнений: '))
            except ValueError:
                print('Введите значение в правильном формате!')
                continue
            system = count

        mode = None
        if system == 1:
            print('Для систем из 1 уравнения предусмотрена возможность ввести ДУ 1-ого/2-ого порядка на выбор')
            while mode is None:
                try:
                    digit = int(input('Порядок уравнения: '))
                except ValueError:
                    print('Введите значение в правильном формате!')
                    continue
                mode = digit

        if mode == 2:
            fun = input('Введите функцию: ')
            fun = fun.lower()
            fun = fun.replace("y\'", "z")

        func1, func2, func3, func4 = [None] * 4
        y0, z0, u0, v0 = [None] * 4
        if mode == 2:
            for_func = ['z', fun]
        else:
            for_func = [func1, func2, func3, func4]

        for_yzuv = [y0, z0, u0, v0]
        a, b, n = [None] * 3

        # 1-ый блок, вводим функцию
        func_string = ['y', 'z', 'u', 'v']
        string = ', '.join(func_string[0:system])
        answer_func = []
        if mode == 2:
            system = mode

        for i in range(0, system):
            func = for_func[i]
            c = 0
            while func is None or (mode == 2 and c == 0):
                if mode != 2:
                    fun = input(f'Введите функцию d{func_string[i]}/dx = f(x, {string}): ')
                else:
                    fun = func

                if '^' in fun:
                    fun = fun.replace('^', '**')
                fun = fun.lower()

                plan = ['e', 'pi', 'sin', 'cos', 'tan', 'log']
                dict_replace = {i: 'math.' + i for i in plan}
                dict_replace['tg'] = 'math.tan'
                dict_replace['ln'] = 'math.log'
                dict_replace['ctan'] = '1/math.tan'
                dict_replace['ctg'] = '1/math.tan'

                for item in dict_replace:
                    if item in fun:
                        fun = fun.replace(item, dict_replace[item])

                # проверяем есть ли лишние буквы
                alphabet0 = ['z', 'u', 'v', 'j', 'k', 'q', 'r', 'b', 'd', 'w', 'f', 'f']
                for j in range(0, system-1):
                    alphabet0[j] = 'j'
                alphabet1 = ['t', 'a', 'p', 'i', 's', 'n', 'c', 'o', 'l', 'g', 'h', 'm']
                alphabet2 = {
                    't': ['math', 'tan'], 'a': ['math', 'tan'], 'p': ['pi'], 'i': ['sin', 'pi'],
                    's': ['sin', 'cos'], 'n': ['tan', 'sin'], 'c': ['cos'], 'o': ['cos', 'log'],
                    'l': ['log'], 'g': ['log'], 'h': ['math'], 'm': ['math']
                }

                for letter in range(len(alphabet0)):
                    if alphabet0[letter] in fun:
                        print('У вас есть лишние переменные/символы букв')
                        break
                    let = alphabet1[letter]
                    if fun.count(let) > sum(list(map(lambda x: fun.count(x), alphabet2[let]))):
                        print('У вас есть лишние переменные/символы букв')
                        break
                else:   # сюда заходим, если for закончился без break
                    x, y, z, u, v = [1] * 5     # проверяем ошибки при вызове eval()
                    flag_2 = False
                    try:
                        eval(fun)
                    except (SyntaxError, NameError, AttributeError):
                        print('Синтаксическая ошибка!')
                        flag_2 = True
                    except ValueError:
                        if valuer(fun):
                            print('Скорее всего в вашей формуле статическая ошибка в логарифме, исправьте её')
                            flag_2 = True
                    except ZeroDivisionError:
                        if zerodiv(fun):
                            print('Скорее всего в вашей формуле статическое деление на ноль')
                            flag_2 = True
                    except TypeError:
                        print('Неправильное использование мат. функций (проверьте ваши логарифмы и триг. ф-ции)')
                        flag_2 = True

                    if flag_2:
                        func = None
                    if not flag_2:
                        answer_func.append(fun)
                        func = fun
                        c = 1

        if mode == 2:
            print('Ваше уравнение было превращено в систему: ')
            print("{" + f'y\' = {answer_func[0]}')
            print("{" + f'z\' = {answer_func[1]}')

        # 2-ой блок, здесь будет ввод начальных условий
        while a is None or b is None:
            try:
                aa, bb = map(float, input('\nВведите 2 числа через пробел - начало и конец отрезка.'
                                          '\nКонцы включены. Разделитель целой и дробной части - точка').split())
            except ValueError:
                print('Введите значения в правильном формате!')
                continue

            a, b = aa, bb

        answer_yzuv = []
        for i in range(0, system):
            yzuv = for_yzuv[i]
            while yzuv is None:
                try:
                    some_func = float(input(f'\nВведите {func_string[i]}({a}): '))
                except ValueError:
                    print('Введите значение в правильном формате!')
                    continue
                yzuv = some_func
                answer_yzuv.append(yzuv)

        # 3-ий блок, здесь будет ввод точности
        while n is None:
            try:
                s = int(input('\nВведите число n в ряде x0, x1, ..., xn: '))
            except ValueError:
                print('Введите значение в правильном формате!')
                continue
            if s <= 0:
                print('Количество не может быть <= 0')
                continue
            else:
                n = s

        print('\nЕсли вы согласны с введёнными значениями и хотите завершить ввод, впишите любой символ/слово')
        print('В противном случае, напишите "NO" и вы начнёте с первого шага')
        check_input = input()
        if check_input != 'NO':
            return answer_func, answer_yzuv, [a, b], n
        elif check_input.lower() == 'no':
            continue


if __name__ == '__main__':
    print(diff_input())
