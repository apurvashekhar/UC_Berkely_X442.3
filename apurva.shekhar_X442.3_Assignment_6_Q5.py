#Write a function that combines several dictionaries by creating a new dictionary
#with all the keys of the original ones. If a key appears in more than one input
#dictionary, the value corresponding to that key in the new dictionary should be
#a list containing all the values encountered in the input dictionaries that
#correspond to that key.

dic1 = {}
dic1['apple'] = 1
dic1['banana'] = 2
dic1['carrot'] = 3
dic2 = {}
dic2['apple'] = 'a'
dic2['banana'] = 'b'
dic2['carrot'] = 'c'

def new_dic(*dictionaries):
    final_dictionary = {}
    for dic in dictionaries:
        for k,v in dic.items():
            if k not in final_dictionary:
                value_list = []
                value_list.append(v)
                final_dictionary[k] = value_list
            else:
                final_dictionary[k].append(v)
    print(final_dictionary)

answer = new_dic(dic1, dic2)
