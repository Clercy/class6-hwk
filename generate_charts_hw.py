#!/usr/bin/env python

# 1. load a dataset from a file
# 2. "organize" that file, so that we can access columns *or* rows of it easily
# 3. compute some "summary statistics" about dataset
# 4. print those summary statistics

# 1. load a dataset
# 1a. accept arbitrary filename as arhument
# 1b. load the file

def thetimestamp ():

    now = datetime.datetime.now()
    thetimestamp = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second)
    return thetimestamp


from argparse import ArgumentParser

parser = ArgumentParser(description='A CSV reader +  stats maker')
parser.add_argument('csvfile', help='Path to the input csv file.')

parsed_args = parser.parse_args()
print(parsed_args)
print(parsed_args.csvfile)

my_csv_file = parsed_args.csvfile

# Check if file exists

import os
import os.path as op

#Validate if file is tere or else abort here
assert op.isfile(my_csv_file), "Please give a real file,k thx"
print('Woot the file exists')

# 1b. load the file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

data = pd.read_csv(my_csv_file, sep='\s+|,', header=None)

#Add Header
data.columns = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B1000", "LSTAT", "MEDV"]

data['CRIM'] = data['CRIM'].astype(float).round(2)
data['NOX'] = data['NOX'].astype(float).round(2)

#Show Data
print(data)

########################################  HISTOGRAM  ###########################################
#Generate Histograms

for c in data.columns:

    plt.hist(data[c], bins=14)
    plt.ylabel(c)
    plt.savefig(c + '_'+ thetimestamp() + '.png')
    plt.close()

########################################  HISTOGRAM  ###########################################

########################################### SCATTER ###########################################
#Generate Scatterplots

for c in data.columns:

    for d in data.columns:

        if c != d:

            plt.scatter(data[c],data[d])
            plt.xlabel(c)
            plt.ylabel(d)
            plt.savefig('SCT_' + c + '_' + d + '_'+ thetimestamp() + '.png')
            plt.close()

########################################### SCATTER ###########################################

###########################################  PLOT  ############################################
#Generate Plot

for c in data.columns:

    #print(c)           # Returns name
    #print(data[c])     # Returns data

    for d in data.columns:

        #print(d)       # Returns name
        #print(data[d]) # Returns data

        if c != d:

            plt.plot(data[c],data[d])
            plt.xlabel(c)
            plt.ylabel(d)
            plt.savefig('PLT_' + c + '_' + d + '_'+ thetimestamp() + '.png')
            plt.close()

###########################################  PLOT  ############################################

#Formatted the Mean and Standard Deviation
print(np.round(np.mean(data),decimals=2))
#print(np.mean(data))
print(np.round(np.std(data),decimals=2))
#print(np.std(data))
