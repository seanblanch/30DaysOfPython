# Sean Blanchard
# 9/30/2021
# Python30DayChallenge!
# Exercises - Day 4

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
concatenated_list = ['Thirty', 'Days', 'Of', 'Python']
result = ' '.join(concatenated_list)
print(result)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
var1 = 'Coding'
var2 = 'For'
var3 = 'All'
join = ' '.join([var1, var2, var3])
print(join)
# % operator
operater = '% s % s % s' % (var1, var2, var3)
print(operater)
# {} format
strformat = '{} {} {}'.format(var1, var2, var3)
print(strformat)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
company = company.upper()
print(company)

# Change all the characters to lowercase letters using lower() method.
company = company.lower()
print(company)

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
company = company.title()
print(company)

# Cut(slice) out the first word of Coding For All string.
# company = company[:6] Either or
# company = company[0:6]
#print(company)

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.count('Coding'))

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

# Change Python for Everyone to Python for All using the replace method or other methods.
change = 'Python for Everyone'
print(change.replace('Everyone', 'All'))

# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
big_tech = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(big_tech.split(' ,'))

# What is the character at index 0 in the string Coding For All.
print(company[0])

# What is the last index of the string Coding For All.
print(company[-1])

# What character is at index 10 in "Coding For All" string.
print(company[10]) #space

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
if any(c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in company):
    print(company[0])


