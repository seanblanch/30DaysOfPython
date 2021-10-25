'''
Sean Blanchard
10/2/2021
Python30DayChallenge - Day 6 - Level 2
'''

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Apple', 'Orange', 'Banana', 'Grapes')
vegetables = ('Brussle Sprouts', 'Asparagus', 'Lettuce', 'Cabbage')
animal = ('Dog', 'Chicken', 'Antelope', 'Bison')

food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])

print(findMiddle(food_stuff_tp))

# Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[0:3])
print(food_stuff_lt[len(food_stuff_lt)-3:len(food_stuff_lt)])

# Delete the food_staff_tp tuple completely
del food_stuff_tp
