'''
Sean Blanchard
10/2/2021
Python30DayChallenge - Day 7 - Level 1
'''

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Westinghouse', 'The Trade Desk', 'ProCore'])
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('Westinghouse')
print(it_companies)

# What is the difference between remove and discard
'''
The remove() method raises an error when the specified
 element doesn't exist in the given set,
  however the discard() method doesn't raise any error
   if the specified element is not present in the set 
   and the set remains unchanged.
'''

