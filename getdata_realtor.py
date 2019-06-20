# set up working directory
import sys, os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
#os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import zipcodes
from csvreader import csvread
filename = 'zipcodes.csv'
zipcodes_all = csvread(filename)

# select subset of zip codes
zipcodes = zipcodes_all[441:]
#zipcode = zipcodes[0]

# scrape MLS listings
from scrapeweb_realtor import webscrape
data_raw = webscrape(zipcodes)
## find zip codes with no listings found

#import numpy as np
#missing_zips = np.setdiff1d(zipcodes,data_all.loc[:,'Zip'])

# write .csv file with data
data_raw.to_csv('data_from_441.csv')
    

# Calls the above functions
def main():
    if len(sys.argv) != 2:
        print('usage: python realestate.py zipcodes')
        sys.exit(1)
    zips = csvread(sys.argv[1])
    print(zips)

# Calls the main function
if __name__ == '__main__':
  main()