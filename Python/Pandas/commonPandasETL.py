import pandas as pd
#Common Pandas ETL Methods


#------------------------Loading Data-----------------------------#
filepath=''

#read a csv/txt file
df = pd.read_csv(filepath,header=0)

#read a xlsx file
df = pd.read_excel(filepath, header=None)

#read a .npy or .npz  file
numpy_data = np.load(filename, allow_pickle=True)
columns = ['col1', 'col2', 'col3', 'col4']
df = pd.DataFrame(data=numpy_data['df_name_as_saved_in_npy_file'], 
                  columns=columns)

#------------------------Renaming Data-----------------------------#

#set the names of the columns in a dataframe
columns_1 = ['col1', 'col2', 'col3']
df.columns = columns_1

#reset index
df = df.reset_index(drop=True)

#------------------------Using Functions---------------------------#

#using a lambda function to split strings in a column
get_word = lambda input_data: input_data.split(" ")[0]
df['new_col'] = df['old_col'].apply(get_word)
#or in same column
df['old_col'] = df['old_col'].apply(get_word)



#------------------------Dropping Data-----------------------------#
#drop columns
drop_cols = ['col1','col2']
df.drop(drop_cols,axis=1, inplace=True)
#extract portion of a dataframe based on a condition
df = df.loc[df['col1'] == 'value']
#extract portion of a dataframe which does not contain NaN
df = df.loc[df['col1'].notna()]
#or
df.dropna(axis='columns', inplace=True)
#Drop the rows where at least one element is missing.
df.dropna(inplace=True)
#Keep only the rows with at least 2 non-NA values.
df.dropna(thresh=2, inplace=True)

#---------------------Sorting and Combining Data-------------------#

#sort values by column
df = df.sort_values(by=['col1'])

#sum of values in a column, grouped by another column without using 
#the column as an index
df = df.groupby(['col1'], as_index=False).sum(['col2'])

#combine dataframes vertically
df = pd.concat((df1,df2))

#combine dataframes horizontally
df = pd.concat((df1,df2), axis=1)


#------------------Manipulating and Converting Data----------------#

#remove all commas from df
df = df.replace(to_replace=r',', value='', regex=True)

#convert strings in a column to floats
df['col2'] = pd.to_numeric(df['col2'], downcast="float")

#multiply all values in a col
df['col2'] = 1000*df['col2']
