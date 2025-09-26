# Supplying Arguments

# Defines echo function to accept a user, language, and system.
def echo(user, lang, sys):
    print('User:', user, 'Language:', lang, 'Platform:', sys)

# Call the function passing string values to the function arguments.
echo('Professor Griffiths', 'Python', 'Windows')

#Call the function passing string values to the functions by specifying the arguments
echo(lang = 'Python', sys = 'Mac OS', user = 'Todd')

#Defin another function to accept two arguments with default values.
def mirror (user = 'Chad', lang = 'Python'):
    print('\nUser:', user, 'Language:', lang)

#Add statements to call the second function both using and overriding default values.
mirror()
mirror(lang = 'Java')
mirror(user = 'HCC')
mirror('CIS303', 'MYSQL')
