# Apartment_code
 Python code for Apartment problem

Problem:
Assume there are area's (localities) one next to another..
Each area/locality has one apartment for sale, and you are looking to buy an apartment that is closest to a gym, store, and a school.
Example Input:

Sample 1:
Area_name: 'A',
Gym: False,
Store: False,
School: True 
Area_name: 'B',
Gym: False, 
Store: True,
School: False,
Area_name: "C",
Gym: True,
Store: True,
School: False

Output 1:
B

Sample 2:
Area_name: 'A',
Gym: False,
Store: True,
School: False,
Area_name: 'B',
Gym: True,
Store: False,
School: False,
Area_name: 'C'
Gym: True,
Store: True,
School: False,
Area_name: 'D'
Gym: False,
Store: True,
School: False,
Area_name: 'E'
Gym: False,
Store: True,
School: True

Output 2:
D

------------------------- processed input ------------------------------------

blocks_names = ['A', 'B', 'C']

amenities = ['Gym', 'Store', 'School'] #list of amenities required

apart = [
    {'Gym': False, 'Store': False, 'School': True},
    {'Gym': False, 'Store': True, 'School': False},
    {'Gym': True ,'Store': True, 'School': False}] #each blocks with amenities

-----------------------------------------------------------------------------
Approch:
first we create a map amenities and blocks, i.e. make a dict with list of block haviong each amenites -> amenitiesAvail

amenitiesAvail:
{'Gym': [2], 'Store': [1, 2], 'School': [0]}

then for every block, go through every missing amenites and find the closest block that satisfies that missing amenites -> minDist

minDist:
{0: [2, 1, 0], 1: [1, 0, 1], 2: [0, 0, 2]}

now me take max of each block, since that will be the max distance we will need to travel to meet the missing amenity

maxDist:
[2, 1, 2]

min(maxDist) will give us the block which has least distance to travel to utilize all amenites.

----------------------------------------------------------------------------------------------------------------------

GFG link:
https://ide.geeksforgeeks.org/09170936-2caa-432c-9b21-d10dae93c949