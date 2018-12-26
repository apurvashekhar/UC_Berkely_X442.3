fname = input('Enter file name here: ')
fhandle = open(fname, 'r')

def count_fn():
    line_count = 0
    word_count = 0
    character_count = 0
    for line in fhandle:
        line_count = line_count + 1
        words = line.split()
        for word in words:
            word_count = word_count + 1
        for character in line:
            character_count = character_count + 1

    return line_count, word_count, character_count

print(count_fn())
