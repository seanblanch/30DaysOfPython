'''
Sean Blanchard
10/2/2021
Python30DayChallenge - Day 6 - Level 1
'''

empty_tuple = ()
print(empty_tuple)

sister_tuple = ('Jessica', 'Brie')
print(sister_tuple)

brother_tuple = ('Vizzo', 'Lukas')
print(brother_tuple)

sibiling_tuple = sister_tuple + brother_tuple
print(sibiling_tuple)

print(len(sibiling_tuple))

parents_tuple = ('Steve', 'Anne')
family_members = sibiling_tuple + parents_tuple
print(family_members)

