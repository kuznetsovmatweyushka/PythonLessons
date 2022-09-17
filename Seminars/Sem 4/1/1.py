# 1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 3 5

def read_file(path : str) -> list:
    f = open(path, 'r')
    data = f.read()
    f.close()
    data = list(map(int,data.split(' ')))
    return data

def find_nums(nums : list) -> int:
    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] > 1:
            return nums[i] + 1

data_list = read_file("C:\\Users\\ukeuk\\Desktop\\Учеба\\Знакомство с Python\\Seminars\\Sem 4\\1\\numb.txt")
print(f"Нехватает числа {find_nums(data_list)}")

