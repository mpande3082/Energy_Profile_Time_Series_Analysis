import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels
from prophet import Prophet
#'pd' for example is a library naming convention

df = pd.read_csv("owid-energy-data.csv")
#pd.read_csv ALWAYS returns a dataframe
#if you want to check type: print(type(df))
#pd.read_csv tells pandas to open and read the file 
#it's a method/function that is within pandas
#object.method(inputs)


#print(df.head())
#dataframe itself is an object with builtin functions
#df.head() are the first 5 ROWS of dataframe
#the header row is not included in the 5

#arrow -> means the TYPE the fn returns
#default for df.head is 5 rows

#STEP 2: filter the data
countries = ["United States", "China"]

#dataframe is indexable by row position AND column string
#first: index by column name
countries_column = df["country"] #TYPE: SERIES
boolean_series = countries_column.isin(countries) #TYPE: SERIES
#isin method loops over every entry in the column and checks against countries list

#print(type(countries_column))
#print(type(row_indices))

#second: index by rows
filtered_df = df[boolean_series]
#filtered dataframe includes all the rows whose country column is US or China
#all columns are kept, only rows are filtered

#SUMMARY: 
    #filtering rows: index df using a boolean series df[df["column"].isin(columnlist)]
    #filtering columns: pass in list of column names df[['x', 'y']]
    
print(filtered_df)
