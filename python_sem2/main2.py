#4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

n = int(input())
a = int(input("Введите первое значение индекса - "))
b = int(input("Введите второе значение индекса - "))
ist = []

for i in range(-n, n+1): 
    ist.append(i)

print(ist)
print(ist[a] * ist[b])

print(sum(ist))








