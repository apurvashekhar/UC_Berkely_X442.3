# Write a loop that reads each line of a file. It should count the number of
# characters in each line and keep track of the total number of characters read.
# Once you have a total of 1,000 or more characters, break from the loop. (You
# can use a break statement to do this.)

# 1. Read every line of the file.
# 2. Read every letter in every line.
# 3. When the count of letter reaches 1000, break the loop.

fhandle = open('test.txt','r')
count = 0
for line in fhandle:
    for letter in line:
        count = count + 1
        if count >= 1000:
            break
    if count >= 1000:
        break
print(count)
