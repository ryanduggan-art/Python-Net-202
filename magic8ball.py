# Return values

import random

def getanswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedely so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Ask again Later'
    elif answerNumber == 5:
        return 'Concentrate and ask again'
    elif answerNumber == 6:
        return 'My reply is no'
    elif answerNumber == 7:
        return 'Reply hazy'
    elif answerNumber == 8:
        return 'Outlook not good'
    elif answerNumber == 9:
        return 'Doubtful'

question = input('Ask a yes or no question:')
r = random.randint(1,9)
fortune = getanswer(r)
print(fortune)

