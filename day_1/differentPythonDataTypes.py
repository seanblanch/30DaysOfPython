#number
print(1)
print(1.1)
print(1+1j)

#String
print('This is a string of characters')

#Boolean
print(True)
print(False)

#List of numbers
NumberList = [1, 2, 3 , 4]
print(NumberList)

#List of Strings
StringList = ['Sean', 'Brie', 'Corona']
print(StringList)
print(StringList[2])

#Tuple
#A tuple is an ordered collection of different data types
#but tuples cannot be modified once create
NameTuple = ('Sean', 'Brie', 'Anne', 'Steve', 1) #Names
print(NameTuple)

#Set
"""
A set is a collection of data types similar to
list and tuple. Unlike list and tuple, set is not a
ordered collection of items.
Like in Mathematics, set in Python stores only
Unique items.
"""
integerSet = {2, 4, 3, 5}
print(integerSet)
floatSet = {3.14, 9.81, 2.7}
print(floatSet)

#Dictionary
"""
A Python dictionary object is an unordered
collection of data in a key value pair format
"""

seanDictionary = {
    'firstName': 'Sean',
    'lastName': 'Blanchard',
    'country': 'United States of America',
    'age': '28',
    'is_married': False,
    'skills': ['Java', 'Pyton', 'SQL']
}
print(seanDictionary)
print(seanDictionary["firstName"])
for key,value in seanDictionary.items():
    print(key, ' : ', value)