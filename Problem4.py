# Write a python program using os module and searsch and write all the content whihc is in a diractory 
import os
# write the path of which directory you want to choose 
directory_path = 'C:\\Users'
# list all the contents and file of the chosen directory 
contents = os.listdir(directory_path)
# print all the content in the selected directory 
for item in contents:
    print(item)

