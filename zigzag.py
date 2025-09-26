# A fun zig-zag program

#Imports time and sys modules
import time, sys
indent = 0 #How many spaces to indent
indent_increasing = True #Whether the indentation is increasing or not

try:
    while True: #The main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.0001) #Pause for 1/1000th of a second.

        if indent_increasing:
            #Increase the number of spaces:
            indent = indent + 1
            if indent == 10:
                #Change direction:
                indent_increasing = False
        else:
            #Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                #Changes direction:
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()

