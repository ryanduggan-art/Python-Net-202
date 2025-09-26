#File Access
file = open('Access.txt','w')
print('FileName:',file.name)
print('File Open Mode:',file.mode)
print('Readable:',file.readable())
print('Writable:',file.writeable())
def get_status(f):
    if(f.closed):
        return 'Closed'
    else:
        return 'Open'
print('File Status: ',get_status(file))
file.close()
print('\nFile Status:',get_status(file))
