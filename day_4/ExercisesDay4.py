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
p_f_e = 'Python For Everyone'
res = [char for char in p_f_e if char.isupper()]
print(''.join(res))

# Create an acronym or an abbreviation for the name 'Coding For All'.
res2 = [char for char in company if char.isupper()]
print(''.join(res2))

# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
new_sentence = 'You cannot end a sentence with because because because is a conjunction'
print(new_sentence.index('because'))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot
# end a sentence with because because because is a conjunction'
print(new_sentence.rindex('because'))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because
# because because is a conjunction'
print(new_sentence[31:54])

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a
# sentence with because because because is a conjunction'
second_sentence = 'You cannot end a sentence with because because because is a conjunction'
print(second_sentence.index('because'))

# Does ''Coding For All' start with a substring Coding?
if company.find('Coding') == 0:
    print('it starts with Coding')
else:
    print('it does not start with Coding')

# Does 'Coding For All' end with a substring coding?
if company.endswith('coding'):
    print('The string ends with coding')
else:
    print('The string does not end with Coding')

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
c_f_a_string = '\tCoding For All\t\t'
print(c_f_a_string.expandtabs(-1))

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
challenge = '30DaysOfPython'
print(challenge.isidentifier())
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid',
# 'Falcon']. Join the list with a hash with space string.
lists = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(lists))

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
sentence_one = 'I am enjoying this challenge.'
sentence_two = 'I just wonder what is next.'
sentence_combined = sentence_one + '\n' + sentence_two
print(sentence_combined)

# Use a tab escape sequence to write the following lines.
tab_sentence = 'Name\tAge \tCountry \tCity \nAsabeneh \t250 \tFinland \tHelsinki'
print(tab_sentence)

# Use the string formatting method to display the following:
string_formatting = 'radius = 10 \narea = 3.14 * radius ** 2 \nThe area of a circle with raidus 10 is 314 meters square.'
print(string_formatting)

# Make the following using string formatting methods:
string_formatting = '8 + 6 = 14 \n8 - 6 = 2 \n8 * 6 = 48 \n8 / 6 = 1.33 \n8 % 6 = 2 \n8 // 6 = 1 \n8 ** 6 = 262144'
print(string_formatting)