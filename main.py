# 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
print("\ntask 1: ")
lst = []
n = int(input("Введите количество чисел в списке: "))
sum = 0
for i in range(n):
    num = int(input("Введите число: "))
    lst.append(num)
    if i % 2 == 1:
        sum += num
print(f"Список: {lst}")
print(f"Сумма: {sum}")

# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
print("\ntask 2: ")
some_list = [int(input("Введите число: ")) for _ in range(int(input("Введите количество чисел в списке: ")))]
print(some_list)
length = len(some_list) 
if length % 2 == 1:
    sum_list = [some_list[i] * some_list[len(some_list) - 1 - i] for i in range(len(some_list)//2 + 1)]
else:
    sum_list = [some_list[i] * some_list[len(some_list) - 1 - i] for i in range(len(some_list)//2)]
print(sum_list)

# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
print("\ntask 3: ")
some_list = [float(input("Введите вещественное число: ")) for _ in range(int(input("Введите количество элементов: ")))]
if len(some_list) != 0:
    min = some_list[0]%1
    max = some_list[0]%1
    for elem in some_list:
        temp = elem % 1
        if temp < min:
            min = temp
        if temp > max:
            max = temp
    print(max - min)


# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
print("\ntask 4: ")
print(bin(int(input("Введите число: "))))

# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
print("\ntask 5: ")

def fib(n):
    if n >= 0:
        pos_lst = [0, 1]
        idx = range(n + 1)
        for k in idx[2:]:
           pos_lst.append(pos_lst[k-1] + pos_lst[k-2])
        return pos_lst[n]
    else:
        n= -(n-1)
        neg_lst = [1,0]
        idx = range(n + 1)
        for k in idx[2:]:
           neg_lst.append(neg_lst[k-2] - neg_lst[k-1])
        neg_lst.reverse()
        return neg_lst[0]

k = int(input("Введите число: "))
lst = []
for i in range(-k, k + 1):
    lst.append(fib(i))
print(lst)