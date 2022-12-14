'''
5 Реализуйте алгоритм перемешивания списка.
Из библиотеки random использовать можно только randint


from random import sample
 
if __name__ == '__main__':
 
    nums = range(5)
 
    l = sample(nums, len(nums))
    print(l)
'''   
   
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]



import random
def mix_list(list_original):
    list = list_original[:]
    list_length = len(list)
    for i in range(list_length):
        index_aleatory = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    return list

mixed_list = mix_list(list)
print(list)
print(mixed_list)
