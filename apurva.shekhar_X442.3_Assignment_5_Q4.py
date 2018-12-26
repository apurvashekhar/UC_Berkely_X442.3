#Modify the program written in question 3 so that it doesn't count characters
#on any line that begins with a pound sign (#).

fhandle = open('test.txt','r')
count = 0
for line in fhandle:
    if line.startswith('#'):
        continue
    for letter in line:
        count = count + 1
        if count >= 1000:
            break
    if count >= 1000:
        break
print(count)
