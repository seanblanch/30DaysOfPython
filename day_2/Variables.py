'''
Sean Blanchard
9/24/2021
'''
#Day 2: 30 Days of python Programming

first_name = 'Sean'
last_name = 'Blanchard'
full_name = 'Sean Blanchard'
country = 'United States of America'
city = 'Ventura'
age = 28
year = 2021
is_married = False
is_true = True
is_light_on = False
multi_variable_tuple = (1, 2, 3, 4, 5, 6, 7) #tuple
mult_variable_list = [1, 2, 'Sean', 6, 'college'] #list

print(first_name)
print(last_name)
print(full_name)
print(country)
print(age)
print(year)
print(is_married)
print(is_true)
print(is_light_on)
print(multi_variable_tuple)
print(mult_variable_list)

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(multi_variable_tuple))
print(type(mult_variable_list))

print('The length of my first name is: ', len(first_name))

if len(first_name) == len(last_name):
    print('The length of my first name is the same length of my last name.')
elif len(first_name) < len(last_name):
    print('Your last name is longer than your first name!')
elif len(first_name) > len(last_name):
    print('Your first name is longer than your last name!')


num_one = 5
num_two = 4
total = num_one + num_two
print(total)

diff = num_two - num_one
print(diff)

product = num_two * num_one
print(product)

division = num_one / num_two
print(division)

remainder = num_two % num_one
print(remainder)

exp = num_one ** num_two
print(exp)

floor_division = num_one // num_two
print(floor_division)


