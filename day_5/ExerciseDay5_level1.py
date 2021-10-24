'''
Sean Blanchard
10/2/2021
Python30DayChallenge - Day 5 - Level 1
'''

# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
bike_list = ['Specialized', 'Kona', 'Yeti', 'Santa Cruz', 'Intense', 'Pivot', 'GT']

# Find the length of your list
print(len(bike_list))

# Get the first item, the middle item and the last item of the list
# first
print(bike_list[0])


# middle
def findMiddle(bike_list):
    middle = float(len(bike_list)) / 2
    if middle % 2 != 0:
        return bike_list[int(middle - .5)]
    else:
        return (bike_list[int(middle)], bike_list[int(middle - 1)])


print(findMiddle(bike_list))
# last
print(bike_list[-1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['name', 'age', 'height', 'marital status', 'address']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0])
print(findMiddle(it_companies))
print(it_companies[-1])

# Print the list after modifying one of the companies
it_companies[0] = 'Westinghouse'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('The Trade Desk')
print(it_companies)
it_companies.insert(2, 'JSL Technologies')
print(it_companies)

# Insert an IT company in the middle of the companies list
middle = int(len(it_companies) / 2)
it_companies.insert(middle, 'This is the middle')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
# converted_list = it_companies[0].upper()
converted_list = [x.upper() for x in it_companies]
print('This is the converted list', converted_list)

#Join the it_companies with a string '#;  '
it_companies.extend(converted_list)
print(it_companies)

# Check if a certain company exists in the it_companies list.
does_exist = 'Google' in it_companies
print(does_exist)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
del it_companies[0:3]
print(it_companies)

# Slice out the last 3 companies from the list
del it_companies[len(it_companies)-3:len(it_companies)]
print(it_companies)

# Slice out the middle IT company or companies from the list
del it_companies[int(len(it_companies)/2)]
print(it_companies)

# destroy the IT companies list
it_companies.clear()
print(it_companies)

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
new_end = front_end + back_end
print(new_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert
# Python and SQL after Redux.
full_stack = new_end
insert_stack = ['Python', 'SQL']
full_stack.insert(5, 'Python\', \'SQL')
print(full_stack)