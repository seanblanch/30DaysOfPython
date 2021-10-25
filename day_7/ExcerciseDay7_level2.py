'''
Sean Blanchard
10/2/2021
Python30DayChallenge - Day 7 - Level 2
'''

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Join A and B
C = A.union(B)
print(C)

# Find A intersection B
D = A.intersection(B)
print(D)

# Is A subset of B
print(A.issubset(B))

# Are A and B disjoint sets
print(A.isdisjoint(B))

# Join A with B and B with A
print(A.union(B))
print(B.union(A))

# What is the symmetric difference between A and B
print(A.symmetric_difference(B))

del A
del B
del C
