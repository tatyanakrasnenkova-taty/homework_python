#Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой мето

'''
5 Реализуйте алгоритм перемешивания списка.
Из библиотеки random использовать можно только randint
'''

from random import sample
 
if __name__ == '__main__':
 
    nums = range(5)
 
    l = sample(nums, len(nums))
    print(l)