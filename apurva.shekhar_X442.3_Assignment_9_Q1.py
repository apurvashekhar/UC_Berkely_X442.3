#Using os.walk, write a script that will print the filenames of zero length
#files. It should also print the count of zero length files.

import os

count = 0
empty_files = []

for root, directory, files in os.walk('empty_directory'):
    for filename in files:
        file_size = os.path.getsize(os.path.join(root,filename))
        if file_size == 0:
            empty_files.append(filename)
            count += 1

finalnames_of_empty_files = ' , '.join(empty_files)
print("Names of zero length files :", finalnames_of_empty_files)
print("Total count of zero length files :", count)
