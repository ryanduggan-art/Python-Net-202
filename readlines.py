# Readlines

#Create a sample file for demonstration
with open("NET202.txt","w") as f:
    f.write("Python.\n")
    f.write("IS.\n")
    f.write("Awesome.")

#Open the file in read mode
with open("NET202.txt", "r") as file:
    lines = file.readlines()

#Print the list of lines
print(lines)
