# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 11:30:04 2022

@author: George Kordonis
"""

def get_most_frequent(words_list,ignore_case=False):
    """this is a function that counts the number of instances a word appears in a 
    given list and return the word with the highest count, not counting 
    capitalization for ignore_case:TRUE and counting capitalization
    for the default value of ignore_case:FALSE"""
    counter_list=[]
    lower_list=[]
    if ignore_case == True:
        for i in range(len(words_list)):
            lower_list.append(str(words_list[i]).lower())
        for j in range(len(lower_list)):
            counter_list.append(lower_list.count(lower_list[j]))
            max_value = max(counter_list)
            max_index = counter_list.index(max_value)
        word_m  = lower_list[max_index]
        count_m  = counter_list[max_index]
        tuple_max = (word_m ,count_m )
    else:
        for i in range(len(words_list)):
            counter_list.append(words_list.count(words_list[i]))
            max_value = max(counter_list)
            max_index = counter_list.index(max_value)
        word_m = words_list[max_index]
        count_m = counter_list[max_index]
        tuple_max = (word_m ,count_m )
    print(tuple_max)

    
get_most_frequent(["a","b","x","A","eisai bro","a","eisai Bro","c","c","c","A"],True)    