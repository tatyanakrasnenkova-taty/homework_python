# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет */


print ('Введите цифру, обозначающую день недели')

number = int (input ())

if (number == 6 or number == 7):
    print('да')
elif (number > 7):
    print('введите цифру от 1 до 7, ведь в недели 7 дней')
else:
    print('нет')