# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:36:29 2019

@author: michaelboles
"""

# set up working directory
import os
import pandas as pd
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
#os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

### PRICE PLOTS ###

### Bay overview ###

# import data
data_bay = pd.read_csv('./Data/listings/data_bay.csv')
shapefile = r'./shapefiles/Bay cities/ba_cities.shp'

# calculate quintiles
from calculatequintiles import price_quintiles
pricequintiles_bay = price_quintiles(data_bay)

# plot data
from cartoplotfunctions import cartoplot_bay_price
mapsize = 30
cartoplot_bay_price(data_bay, mapsize, pricequintiles_bay, shapefile)


### San Francisco ###

# import data
data_sf = pd.read_csv('./data/data_sf.csv')

# calculate quintiles
pricequintiles_sf = price_quintiles(data_sf)

# plot data
from cartoplotfunctions import cartoplot_sf_price
shapefile_sf = r'./shapefiles/SF neighborhoods/geo_export_9b5217d9-9101-418b-8805-7dd14339f103.shp'
mapsize = 15
cartoplot_sf_price(data_sf, mapsize, pricequintiles_sf, shapefile_sf)


### East Bay ###

# import data
data_eastbay = pd.read_csv('./data/data_eastbay.csv')

# calculate quintiles
pricequintiles_eastbay = price_quintiles(data_eastbay)

# plot data
from cartoplotfunctions import cartoplot_eastbay_price
mapsize = 15
cartoplot_eastbay_price(data_eastbay, mapsize, pricequintiles_eastbay, shapefile)

### Peninsula ###

# import data
data_peninsula = pd.read_csv('./data/data_peninsula.csv')

# calculate quintiles
pricequintiles_peninsula = price_quintiles(data_peninsula)

# plot data
from cartoplotfunctions import cartoplot_peninsula_price
mapsize = 15
cartoplot_peninsula_price(data_peninsula, mapsize, pricequintiles_peninsula, shapefile)


### South Bay ###

# import data
data_southbay = pd.read_csv('./data/data_southbay.csv')

# calculate quintiles
pricequintiles_southbay = price_quintiles(data_southbay)

# plot data
from cartoplotfunctions import cartoplot_southbay_price
mapsize = 15
cartoplot_southbay_price(data_southbay, mapsize, pricequintiles_southbay, shapefile)


### COMMUTE PLOT ###

# import data
#data_bay_withtimes = pd.read_csv('./data/listings/data_bay_withtimes.csv')
#data_bay_withtimes['Min commute'] = data_bay_withtimes[['SF time', 'PA time']].min(axis=1)

# get shapefile, file containing commute, school data by zipcode
shapefile = r'./shapefiles/Bay Zips/ZIPCODE.shp'
data_zipcodes = pd.read_csv('./data/data by zipcode/data_zipcodes.csv')

# plot data
from cartoplotfunctions import cartoplot_commute
mapsize = 15
cartoplot_commute(mapsize, shapefile, data_zipcodes)


### SCHOOL PLOT ###

# plot data
from cartoplotfunctions import cartoplot_schools
cartoplot_schools(mapsize, shapefile, data_zipcodes)


### PRICE DIFFERENCE PLOT ###

# import data
shapefile = r'./shapefiles/Bay cities/ba_cities.shp'
data_all_price_predictions = pd.read_csv('./data/listings/data_all_price_predictions.csv')

# calculate quintiles
from calculatequintiles import price_diff_quintiles
price_diff_quintiles = price_diff_quintiles(data_all_price_predictions)

# plot data
from cartoplotfunctions import cartoplot_bay_price_predictions
mapsize = 30
cartoplot_bay_price_predictions(data_all_price_predictions, mapsize, price_diff_quintiles, shapefile)

