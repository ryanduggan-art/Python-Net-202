# Find file size
#Import os module
import os
#path
path = '/Users/ryanduggan/Desktop/'
#Get the size of specified path
size = os.path.getsize(path)
#print size of specified path
print("size (In Byets) os '%s':" %path, size)
