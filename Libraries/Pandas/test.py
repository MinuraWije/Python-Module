import pandas as pd 

#Creating a dataframe
# data = {'Name': ['Minura','Omesh','Sanuka'], 'Age': [21,23,17]}
# df = pd.DataFrame(data)
# print(df,type(df))          #Dataframe index numbers are assigned automatically(starts from 0) but can be changed as needed

#Accessing cells in a DataFrame

# 1. using loc(label based)
# print(df.loc[1,'Name'])

# 2. using index(index based)
# print(df.iloc[1,0])

# print(df.loc[1])

# print(df.loc[[0,1]])        #Returns multiple specified rows 

# data = {"calories": [420,380,390], "duration":[50,40,45]}
# df = pd.DataFrame(data, index=["day1","day2","day3"])
# print(df)

# # print(df.loc["day2"])
# print(df.loc[["day2","day3"]])

# print(df['calories'])


# print(df.shape)     # Returns the dimensions of the DataFrame as a tuple (rows, columns)
# print(df.columns)
# print(list(df.columns))

# print(df.dtypes)
# print(df.size)

# df = pd.DataFrame({'A':[1,2],'B':[3,4]})
# print(df.values,type(df.values))            #Returns the data as a NumPy array.

# data = {'Age':[21,25,34,23],'Salary':[789,450,32940,420]}
# df = pd.DataFrame(data)
# print(len(df))

# data = {'Order ID':[101,102,103,104,105],
#         'Product':['Laptop','Smartphone','Desk chair','Monitor','Bookshelf'],
#         'Category':['Electronics','Electronics','Furniture','Electronics','Furniture'],
#         'Quantity':[2,5,10,4,2],
#         'Price per unit': [1000,800,150,200,300],
#         'Region':['North','South','East','West','North']}

#You are a data analyst for a retail company. The company has provided you with the above table containing sales data. Your task is to analyse the 
# sales data using python and pandas to answer some key business questions. 
# 1. Calculate the total revenue for each order. Add a new column "Total Revenue" to store the total revenue. 
# 2. Identify the best selling product. Find the product with the highest total sales revenue. 

# df = pd.DataFrame(data)
# print(df['Quantity']*df['Price per unit'])
# df['Total Revenue'] = list(df['Quantity']*df['Price per unit'])     #Adding a new column
# print(df['Total Revenue'].max())
# print(df[df['Total Revenue']>=df['Total Revenue'].max()])

# data = {'Age':[25,30,35,40],
#         'Salary':[50000,60000,70000,80000]}
# df = pd.DataFrame(data)
# print(df.mean())            #Calculates the mean of numerical columns 
# print(df.sum())
# print(df.describe())

# data = {
#     'Name':['Alice','Minura','Omesh'],
#     'Age':[32,21,23],
#     'Score':[56,90,95]
# }
# df = pd.DataFrame(data)
# filtered_df = df[df['Age']>25]            #filtering data here
# print(filtered_df,type(filtered_df))

df = pd.DataFrame({'A':[1,2],'B':[3,4]})
df.loc[len(df)] = [5,7]
# print(df)

#Dropping a column or row
#if axis=1 we drop columns, if axis=0 we drop rows
#if inplace=True, the DataFrame is modified directly, no new object is returned
#if inplace=False, a new dataframe with the columns dropped is created while the existing dataframe remains

# df_dropped = df.drop('B',axis=1)
# df_dropped = df.drop(2,axis=0)
# print(df_dropped)

#Reading csv files as a dataframe

# df = pd.read_csv('./CSV/employee.csv')
# print(df)

#Reading JSON file as a dataframe

df = pd.read_json('./JSON/students.json')
print(df)