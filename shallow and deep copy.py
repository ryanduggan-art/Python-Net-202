#Shallow and Deep Copy

#Import copy module
import copy

#Initialize List 1
li1 = [1, 2, [3, 5], 4]

#Using copy for a shallow copy
lil2 = copy.copy(li1)

#Using copy for a deep copy
li3 = copy.deepcopy(li1)
print('li3 ID:', id(li3), 'Value:', li3)
#print('li1 ID', id(li1), 'Value:', li1)

