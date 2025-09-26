# Weekend Plans

Friday = ['Sleep', 'Work', 'Run']
Saturday = ['Game', 'Food', 'Chores']
print('Friday List:' , Friday)
print('Saturday List:' , Saturday)

# Add items to the list
Friday.append('Homework')
print('Appended:' , Friday)
print('Last Item Removed:' , Friday.pop())
print('Friday List:' , Friday)

Friday.extend(Saturday)
print('Extended:' , Friday)
del Friday [0]
print('Items Removed:' , Friday)
del Friday [1:3]
print('Slice Removed:', Friday)
