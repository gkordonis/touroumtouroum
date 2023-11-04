# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 01:22:09 2022

@author: George Kordonis
"""

def print_pyramid(number):
    """this is a function which receives an input and, if it is an integer
    with value greater than 1, returns a pyramid shape of the multiplications
    up until itself"""
    if (type(number) is not int):
        print("WRONG PARAMETER. PLEASE RUN THE METHOD USING AN INTEGER GREATER THAN 1")
    elif (number<2):
        print(number)
    else:
        pyramid_list=[number]
        for a in range(number):
            if a == 0:
                print(*pyramid_list)
            else:
                pyramid_list.append(number + number*a)
                print(*pyramid_list)
        for b in range(len(pyramid_list),1,-1):   
            if b != 0:
                pyramid_list.remove(number*b)
                print(*pyramid_list[::-1])        

        
print_pyramid(10)