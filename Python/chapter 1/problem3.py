import os
#specify path
path = '/Users/Nitin Baranwal/OneDrive/Desktop'
#list all files
contents = os.listdir(path)
#print name of all files
for item in contents:
    print(item)