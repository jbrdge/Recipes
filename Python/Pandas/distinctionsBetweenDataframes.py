#Compare Two Dataframes with Pandas

import pandas as pd


#Create two sample dataframes
df1 = pd.DataFrame({'City': ['New York', 'Chicago', 'Tokyo', 'Paris','New Delhi'],
                     'Temp': [59, 29, 73, 56,48]})

df2 = pd.DataFrame({'City': ['London', 'New York', 'Tokyo', 'New Delhi','Paris'],
                     'Temp': [55, 55, 73, 85,56]})

#Find Common rows between the two using merge
def commonUsingMerge(df1,df2):
    df = df1.merge(df2, how = 'inner' ,indicator=False)
    return df

#Find common rows between the two using concat
def commonUsingConcat(df1,df2):
    df = pd.concat([df1, df2])
    df = df.reset_index(drop=True)
    df_gpby = df.groupby(list(df.columns))
    idx = [x[0] for x in df_gpby.groups.values() if len(x) != 1]
    df.reindex(idx)
    return df

#Find Rows in DF2 Which Are Not Available in DF1
def findRowsinDF2notinDF1(df1,df2):
    right_merge = lambda x : x['_merge']=='right_only'
    df = df1.merge(df2, how = 'outer' ,indicator=True).loc[right_merge]
    return df

#Check if two Dataframes are exactly the same
def areDataframesSame(df1,df2):
    return df2.equals(df1)

#Check if two Columns are exactly the same
def aredataColumnsSame(df1,df2,column):
    return(df2[column].equals(df1[column]))

#Find all rows between two dataframes which are not common
def findDistinctRows(df1,df2):
    return pd.concat([df1,df2]).drop_duplicates(keep=False)

#Find all values in a column which are different between two dataframes
def differenceinColumns(df1,df2,column):
    return set(df1.column).symmetric_difference(df2.column)