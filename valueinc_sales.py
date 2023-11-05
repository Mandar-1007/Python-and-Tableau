# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 09:34:52 2022

@author: Mandar
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') ----> format to read_csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv',sep=';')

# Summary of the data

data.info()

#working with calculations
#Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Mathematical operations on Tableau

ProfitsPerItem = 21.11 - 11.73
ProfitsPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = ProfitsPerItem * NumberOfItemsPurchased

CostPerTransaction = CostPerItem * NumberOfItemsPurchased

SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased

#CostPerTransaction Column calculation
#CostPerTransaction = CostPerItem * NumberOfItemsPurchased
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']

NumberOfItemsPurchased = data['NumberOfItemsPurchased']

CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#Adding New column to data frame

data['CostPerTransaction'] = CostPerTransaction 

# data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit claculation

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

data['Markup'] = data['ProfitPerTransaction']/(data['CostPerTransaction'])

#Rounding Markup

#roundMarkup = round(data['Markup'],2)

data['Markup'] = round(data['Markup'],2)

#Combining Data fields

my_name = 'Mandar'+' Nadkarni'

my_date = 'Day'+'-'+'Month'+'-'+'Year'

#data['Date'] = data['Day']+'-'

#checking column data type
print(data['Day'].dtype)

#Change columns type

day = data['Day'].astype(str)

year = data['Year'].astype(str)

print(day.dtype)

my_date = day+'-'+data['Month']+'-'+year

data['date'] = my_date

#using iloc to view specific columns/rows

data.iloc[0]    #views the row with index as 0

data.iloc[0:3]  #views first 3 rows

data.iloc[-5:]  #last 5 rows

data.head(5)    #first 5 rows

data.iloc[:,2]  #all rows and 2nd column

data.iloc[4,2]  #4th row and 2nd column

#Using split to split the client keywords field
#new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',',expand = True)

#Creating new columns for the split column in client keywords

data['ClientAge'] = split_col[0]

data['ClientType'] = split_col[1]

data['LengthofContract'] = split_col[2]

#Using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[','')

data['LengthofContract'] = data['LengthofContract'].str.replace(']','')

#Change to lower case

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files

#bringing in a new data set

seasons = pd.read_csv('value_inc_seasons.csv',sep=';')

#Merge files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#Dropping columns

#df = df.drop['columnname', axis = 1]

data = data.drop('ClientKeywords', axis = 1)

data = data.drop('Day', axis = 1)

data = data.drop(['Month','Year'], axis = 1)

#export into csv

data.to_csv('ValueInc_Cleaned.csv',index = False)

