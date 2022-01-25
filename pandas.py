#    CREATING A DATAFRAME WITH PANDAS AND REDEFINING ROW LABELS

import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

##-----------------------     DATA FRAMES    --------------------------##

#the dataframe we are managing is 'cars' and it goes like this:


#                                                              cars_per_cap        country       drives_right
#                                                              US            809  United States          True
#                                                              AUS           731      Australia         False
#                                                              JPN           588          Japan         False
#                                                              IN             18          India         False
#                                                              RU            200         Russia          True
#                                                              MOR            70        Morocco          True
#                                                              EG             45          Egypt          True


# Print out country column as Pandas Series
cars['country']

# Print out country column as Pandas DataFrame
cars[['country']]

# Print out DataFrame with country and drives_right columns
print(cars[['country','drives_right']])

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:,'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:,['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['cars_per_cap','drives_right']])


#######                             LET'S FIND OUT WICH OF THE COUTRIES HAVE MORE THAN 500 CARS PER CAPITA

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]


# Print car_maniac
print(car_maniac)



