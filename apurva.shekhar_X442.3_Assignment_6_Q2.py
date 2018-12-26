#Write a function that accepts an arbitrary number of lists and returns a single
#list with exactly one occurrence of each element that appears in any of
#the input lists.

empty_list = list()
def merged_lists(*all_lists):
    for list in all_lists:
        for number in list:
            if number not in empty_list:
                empty_list.append(number)
    return empty_list

list1 = [1,2,3,4]
list2 = [2,3,4,5,6]
list3 = ['a','b','c']
final_list = merged_lists(list1, list2,list3)
print(final_list)
