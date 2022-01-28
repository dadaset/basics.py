#    TYPICAL CONTROL

# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10 :
    print("medium size, nice!")
else :
    print("pretty small.")
    
#_____________________________ WHILE LOOP ____________________________________#

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset<0 : 
      offset = offset +1
    else : 
      offset = offset -1   
    print(offset) 
#___________________________ FOR LOOP _______________________________________#


# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, area in enumerate(areas) :
    print("room " + str(index) + ": " + str(area))

   
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch

for x in house:
    print("the "+ x[0] + " is " + str(x[1]) + " sqm")
    
#___________________________ LOOP OVER A DICTIONARY___________________________________#
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
#In Python 3, you need the items() method to loop over a dictionary: 

for c,k in europe.items() :
    print("the capital of "+ str(c) + " is " + str(k)) 
    
    #<script.py> output:
    
    #the capital of spain is madrid
    #the capital of france is paris
    #the capital of germany is berlin
    #the capital of norway is oslo
    #the capital of italy is rome
    #the capital of poland is warsaw
    #the capital of austria is vienna

    #___________________________ LOOP OVER A NUMPY ARRAY___________________________________#
    
# these two arrays are already loaded
#   np_height = [74 74 72 ... 75 75 73] 
#   np_baseball = [[ 74 180]
# [ 74 215]
# [ 72 210]
# ...
# [ 75 205]
# [ 75 190]
# [ 73 195]]

# Import numpy as np
import numpy as np

# For loop over np_height
for x in np_height :
    print(str(x) + " inches")

# For loop over np_baseball
for x in np.nditer(np_baseball) :
    print(x)
    
#___________________________ LOOP OVER A DATAFRAME___________________________________#

#cars:   
#      cars_per_cap        country  drives_right
#US            809  United States          True
#AUS           731      Australia         False
#JPN           588          Japan         False
#IN             18          India         False
#RU            200         Russia          True
#MOR            70        Morocco          True
#EG             45          Egypt          True

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(str(lab))
    print(row)

#concatenate labels and a specific column 
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

for lab, row in cars.iterrows() :
    print(str(lab) +": " + str(row['cars_per_cap']))
    
#___________________________USING A FOR LOOP TO ADD A COLUMN TO A DATAFRAME_______________________________#
    
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()
    
# Print cars
print(cars)








