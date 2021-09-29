# Sean Blanchard
# 9/29/2021
import cmath

# Declare your age as integer variable
import math

age = 28
height = 6.3
complex_number = complex(age, height)

print(complex_number)

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this
# triangle (area = 0.5 x b x h).
input_base = int(input('Enter base:'))
input_height = int(input('Enter height:'))
area = int(0.5 * input_base * input_height)
print('The area of the triangle is', area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter
# of the triangle (perimeter = a + b + c).
input_a = int(input('Enter side a:'))
input_b = int(input('Enter side b:'))
input_c = int(input('Enter side c:'))
perimeter = int(input_a + input_b + input_c)
print('The perimeter of the triangle is', perimeter)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (
# perimeter = 2 x (length + width))
input_length = int(input('Enter the length of the rectangle:'))
input_width = int(input('Enter the width of the rectangle:'))
rectangle_perimeter = 2 * (input_length + input_width)
print('The perimeter of the rectangle is', rectangle_perimeter)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r)
# where pi = 3.14.
input_radius = int(input('Enter the radius of the circle:'))
rectangle_area = 3.14 * input_radius ** 2
rectangle_circumference = 2 * 3.14 * input_radius
print('The area of the cirlce is', rectangle_area)
print('The circumference of the circle is ', rectangle_circumference) \
 \
    # Calculate the slope, x-intercept and y-intercept of y = 2x -2
equation = 'y = 2*x - 2'
slope = equation[4]
print(slope)

x_intercept = x = 2 / 2
print(x_intercept)

y_intercept = y = 2 * 0 - 2
print(y_intercept)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
point_1 = (2, 2)
point_2 = (6, 10)
slope2 = (point_1[1] - point_2[0]) / (point_1[1] - point_2[0])
print('The slope is: ', slope2)
euclidean_distance = cmath.sqrt(((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2))
print('The euclidean distance is: ', euclidean_distance)

# Compare the slopes in tasks 8 and 9.
print('slope is slope1', slope is slope2)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is
# going to be 0.
new_x = -3
first_set = math.pow(new_x, 2)
print('first set is:', first_set)
second_set = 6 * new_x
print('second set is:', second_set)
third_set = 9
print(third_set)
newish_y = first_set + second_set + third_set
print('New set this should be 0', newish_y)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement
length_of_python = len('python')
length_of_dragon = len('dragon')
print(length_of_dragon is not length_of_dragon)

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python')
print('on' in 'dragon')

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon.')

# There is no 'on' in both dragon and python
print('on' not in 'dragon')
print('on' not in 'python')

# Find the length of the text python and convert the value to float and convert it to string
float_length = float(length_of_python)
print(float_length)
string_length = str(float_length)
print(string_length)

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = int(input('Enter a number: '))
if (num % 2) == 0:
    print(num, 'is even')
else:
    print(num, 'is odd')

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor = 7 // 3
value = 2.7
print(floor is value)
print(floor)

# Check if type of '10' is equal to type of 10
print(type(10) == type('10'))

# Check if int('9.8') is equal to 10
print('9.8' == 10)

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour: '))
rate_of_pay = hours * rate_per_hour
print('Your weekly earning is', rate_of_pay)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live.
# Assume a person can live hundred years

years_lived = int(input('Enter number of years you have lived: '))
seconds_in_a_year = 31556952
years_to_seconds = years_lived * seconds_in_a_year
print(years_to_seconds)

