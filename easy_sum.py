#/usr/bin/ env python3
#-*- coding: utf-8 -*-

def two_sum(array, target):
    newarray = list(enumerate(array))
    newarray.sort(key = lambda x: x[0])        
    i = 0
    j = len(newarray) - 1
    while i < j:
        result = newarray[i][1] + newarray[j][1]
        if result > target:                                                
            j = j - 1
        elif result < target:
            i = i + 1
        elif result == target:
            index1, index2 = newarray[i][0] + 1, newarray[j][0] + 1
            print('index1 = %d, index2 = %d' % (index1, index2))
            return index1, index2

array = [3, 5, 7, 9, 8]
print(array)
two_sum(array, 13)
