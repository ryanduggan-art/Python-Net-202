#
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
        #this is where the program jumps back to start of while True and reevaluates until name = Joe
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
