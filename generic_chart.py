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
#parser.add_argument('csvfile', help='Path to the input csv file.')

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

data.columns = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B1000", "LSTAT", "MEDV"]

#print(data.head())
#print(data.tail())




#data.round({"CRIM":1, "ZN":1, "INDUS":1, "CHAS":1})
#data.round({"CRIM":1})
#print(data.dtypes)
#data = data.astype('float64')
#data.round(3)
#data.astype(float).round(2)
data['CRIM'] = data['CRIM'].astype(float).round(2)
data['NOX'] = data['NOX'].astype(float).round(2)
#data.append(data.mean(numeric_only=True), ignore_index=True)


print(data)

#trying for sum
#data.loc[len(data)] = [data[col].sum() for col in data.columns]

#columns = list(data)
#for column in columns:
#    print (data[column])

#######to iterate over all columns but the first one
##for column in data.columns[1:]:

#colors = (0,0,0)
#area = np.pi*3

#HISTOGRAM
for column in data.columns:

    #plt.plot(data[column])
    plt.hist(data[column], bins=14)
    print(column)
    print(data[column])
    #plt.hist(column, bins=14)
    #plt.hist(column)

    #plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    #plt.scatter(data[column], data[column], s=area, c=colors, alpha=0.5)

    #print(data[column])# This is the column data to see
    plt.ylabel(column)
    #plt.show()
    #mp.savefig('foo.png')
    plt.savefig(column + '_'+ thetimestamp() + '.png')
    plt.close() # by using this I clear the plot cache or else it adds incrementally


#colors = (0,0,0)
#area = np.pi*3


#SCATTER
for column in data.columns:
    #print(str(column)) #Name of the present column
    #print(len(data.columns)) # Width of the Dataframe. data.columns returns 14
    ##x = len(data.columns)

    #col1 = data[column]

    for x in range(len(data.columns)) :
        #print(data.columns[x]) #Iterate through the column names
        if column != data.columns[x]:
            ##plt.scatter(column, data.columns[x], s=area, c=colors, alpha=0.5)

            #col2 = data[column]

            ##plt.scatter(column, data.columns[x] )
            plt.scatter(column, x)

            ##plt.savefig(column + '_'+ thetimestamp() + '.png')
            plt.savefig('SCT_' + column + '_' + data.columns[x] + '_'+ thetimestamp() + '.png')
            plt.close()



#PLOT
for column in data.columns:
    #print(str(column)) #Name of the present column
    #print(column)
    #print(len(data.columns)) # Width of the Dataframe. data.columns returns 14
    ##x = len(data.columns)
    for y in range(len(data.columns)) :
        #print(data.columns[y]) #Iterate through the column names
        #print(y)
        if column != data.columns[y]:
            ##plt.scatter(column, data.columns[x], s=area, c=colors, alpha=0.5)


            #time = [0, 1, 2, 3]
            #position = [0, 100, 200, 300]

            #print(column)

            #print(y)


            ##plt.scatter(column, data.columns[x] )
            #plt.plot(column, data.columns[x],'-')
            #plt.plot(column, x,'-')

            #plt.plot(time,position,'-')

            ##plt.savefig(column + '_'+ thetimestamp() + '.png')
            plt.savefig('PLT_' + column + '_' + data.columns[y] + '_'+ thetimestamp() + '.png')
            plt.close()









#now = datetime.datetime.now()
#mytimestamp = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second)

#mytimestamp = thetimestamp()
#print(thetimestamp())
#print (mytimestamp)

print('Number of columns: ' + str(len(data.columns)))
print('Number of columns: ' + str(len(data.columns)))
print('Number of rows: ' + str(len(data.index)))



#print(data["CRIM"].mean())
#print(data.shape)




print(np.round(np.mean(data),decimals=2))
print(np.mean(data))

print(np.round(np.std(data),decimals=2))
print(np.std(data))
