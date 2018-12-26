import re

strg_0 = 'AM'
strg_1 = 'am'
strg_2 = 'Parrot'

answer = print(re.match(r'^[a-z][a-z]+$|[A-Z][A-Z]+$', strg_2))

print(re.findall(r'a.*b', 'abra ka dabra aboy\nbatman is powerful'))

#Write a substitution command that will change names like file1, file2, etc. to
#file01, file02, etc. but will not add a zero to names like file10 or file20.

fname = 'file123'
print(re.sub(r'file(\d{1}$)', r'file0\1',fname))

#Many news and mail readers automatically highlight URLs that appear in text,
#for example http://yahoo.com or www.msnbc.com. Construct a regular expression
#that will extract the names of URLs embedded in a string.

fstring = 'This is a url http://yahoo.com http://www.yahoo.com www.google.com www.yahoo.nz embedded string.'

print(re.findall(r'(?:http://)?(?:www\.)?\w+\.\w+', fstring))

#Write a function that takes times of the form 03:12:19 (in other words, three
#hours, twelve minutes, and nineteen seconds) and converts them to the
#corresponding number of seconds.

def calculate_seconds(time_input):
    split_time = time_input.split(':')
    total_seconds = int(split_time[0]) * 3600 + int(split_time[1]) * 60 + int(split_time[2])
    return total_seconds

time_input = input('Enter time here: ')
print(calculate_seconds(time_input), 'seconds.')
