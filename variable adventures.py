# Variable Adventures: The Global Edition


#----------Global Variable------------#

#Global constant used to adjust the final length
integer_additive = 7

#----------Define the functions for the script----------#

#Ask the user for their name and return it
def name_input():
    #Prompts user for their name
    name = input('Enter your name: ')
    #Returns user name to the caller
    return name

#Build and print 'The name entered is: <name> and then return it.
def print_output(name):
    #Building the output sentence using the provided name
    name_entered = ('The name entered is ') + name
    #Printing the sentence
    print(name_entered)
    #Returns the sentence to the caller
    return name_entered

#Split the sentence into a list of words and return it
def create_a_list(output_string):
    #Splits the sentence into a words list
    words = output_string.split()
    #Prints the word list
    print(words)
    #Returns the word list to the caller
    return words

#Creating a function that counts total words plus the global variable integer.
def get_length_of_list(word_list):
    #Compute len(word_list) and adding the global integer_additive
    num_words = len(word_list) + integer_additive
    #Printing the formatted string 'Total Length: ' plus the value from num_words
    print(f'Total Length: {num_words}')
    #Returns num_words to caller
    return num_words

#------------End of script functions---------------------#

#------------Main program--------------------------------#
def main():
    #Creating a local variable that contains the value from name_input
    name_value = name_input()
    #A sentence that contains the value from print_output and passes the argument from name_value
    sentence = print_output(name_value)
    #A list that contains the value from creat_a_list and passing the argument from sentence
    words = create_a_list(sentence)
    #A final number that contains the value of get_length_of_list and passes the argument from words
    final_number = get_length_of_list(words)

main()
#-------------End of Program-----------------------------#


##AI Citation
###Chat GPT helped me work through this assignment and helped me format my comments.

#What made you decide to explain every line instead of just the function block? PD
#How did chat gpt assist you in writing this? -LS



