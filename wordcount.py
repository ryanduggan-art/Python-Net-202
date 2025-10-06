def word_count(filename):# defines word_count with the parameters of a filename
    """Counts word frequency in a text file."""
    counts = {} # empty dictonary container
    try: # begin a try statement
        with open(filename, 'r') as file: # opens filename in read mode and assigns it the local variable 'file'
            for line in file:# loops through each line in the file
                words = line.strip().lower().split() # defines words variable as every word on the line with spaces stripped out and forced to lower-case. Splits at line end. 
                for word in words: #nested for loop that loops through words to look for iterations of word
                    counts[word] = counts.get(word, 0) + 1 # sets a word counter where each time the loop iterates over the word, it adds one to the count. 
    except FileNotFoundError: # exception that runs if filename isn't found
        print("File not found.") # message that prints if file isn't found
        return None

    return counts # after script has looped through words and recorded all iterations, the count is returned to counts dictionary. 

def main():# begins main program
    filename = input("Enter filename: ").strip() # sets variable filename as a string input. 
    result = word_count(filename) # sets variable result to be the result of the function word_count run on filename
    if result: # if there is a result number or if the word occurs in filename
        print("Word frequencies:") # prints the total number of times word occurs in filename 
        for word, count in sorted(result.items(), key=lambda x: x[1], reverse=True): # iterates over the word-count pairs and sorts by the second item in descending language
            print(f"{word}: {count}")# prints the word-count tuples
main()
