#Write a function that will take a variable number of lists. Each list can
#contain any number of words. This function should return a dictionary where the
#words are the keys and the values are the total count of each word in all of the
#lists.


wl1 = ["double", "triple", "int", "quadruple"]
wl2 = ["double", "home run"]
wl3 = ["int", "double", "float"]

count_dictionary = {}
count = 1
def count_function(*argument):
    for wordlist in argument:
        for word in wordlist:
            if word not in count_dictionary:
                count_dictionary[word] = count
            else:
                count_dictionary[word] = count + 1
    return(count_dictionary)

answer = count_function(wl1,wl2,wl3)
print(answer)
