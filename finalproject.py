#Write a text analyzer. It should be in a form of a function that takes a file
#name as an argument. It should read and analyze a text file and then print:

#- the top 5 most frequently used words in the file
#- the number of times the top 5 words are used
#- should be sorted by most frequently used count
#- the longest word in the document
#- the average size of each word
import re

print('This is a text analyzer!')

#Create a histogram to find frequently used words.
def most_frequent_words(content):
    count_dict = {}
    temp_list = []
    for word in content:
        count_dict[word] = count_dict.get(word, 0) + 1
    for word, count in count_dict.items():
        temp_list.append((count, word))
    temp_list = sorted(temp_list, reverse=True)
    print('Top five most frequently used words and count: ')
    for count, word in temp_list[:6]:
        print(word, count)

#The longest word.
def longest_word(content):
    long_word = None
    max_length = 0
    for word in content:
        if long_word is None or len(word) > max_length:
            max_length = len(word)
            long_word = word
    print('Longest word: ',long_word)
    print('Length of the longest word: ', max_length)

#Average size of each word.
def average_size(content):
    total_size = 0
    for word in content:
        total_size += len(word)
    print('Average size of each word: %.2f' % (total_size / len(content)))

fname = input('Enter file name: ')
no_punctuation = ""
try:
    fcontent = open(fname,'r').read()
    complied_content = re.compile(r'\w+', re.IGNORECASE)
    no_punctuation = complied_content.findall(fcontent)
except IOError:
    print('No file named %s found.' % fname)
    quit()

most_frequent_words(no_punctuation)
longest_word(no_punctuation)
average_size(no_punctuation)
