def max_number(my_list):
    max_num = my_list[0][0]
    coord_max = '(0,0)'
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            if max_num < my_list[i][j]:
                max_num = my_list[i][j]
                coord_max = f'({i + 1}, {j + 1})'
    return max_num, coord_max


def min_number(my_list):
    min_num = my_list[0][0]
    coord_min = '(0,0)'
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            if min_num > my_list[i][j]:
                min_num = my_list[i][j]
                coord_min = f'({i + 1}, {j + 1})'
    return min_num, coord_min


def middle_num(my_list):
    middle = 0
    counter = 0
    for i in my_list:
        middle += sum(i)
        counter += len(i)
    return middle / counter


def fill(row, col):
    numbers_list = []
    for line in range(row):
        numbers = input(f'Введите цифры в строке {line} через пробел: ').split()
        numbers = list(map(int, numbers))
        if len(numbers) > col:
            print('Слишком много цифр, лишние уберем!')
            numbers = numbers[:col]
        elif len(numbers) < col:
            print('Не хватает цифр, недостаток будет заполнен 0')
            miss = col - len(numbers)
            for i in range(miss):
                numbers.append(0)
        numbers_list.append(numbers)
    return numbers_list


row = int(input('Введите количество строк: '))
col = int(input('Введите количество столбцов: '))
matrix = fill(row, col)
for i in matrix:
    for j in i:
        print(j, end=' ')
    print()

max_num = max_number(matrix)
print('Наибольшее число:', max_num[0])
print('Координаты:', max_num[1])
print()
min_num = min_number(matrix)
print('Наименьшее число:', min_num[0])
print('Координаты:', min_num[1])
print()
print('Среднее арифметическое:', round(middle_num(matrix), 3))