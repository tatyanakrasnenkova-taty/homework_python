#Задайте список из n чисел последовательности (1 + 1/n)^n. Вывестив консоль сам список и сумму его элементов.

num = int(input())
ist = []
pr = 0
n = 1


for i in range(num):
    pr = (1 + 1/n)**n
    ist.append(pr)
    n += 1 
    
print(sum(ist))
print(type(ist))