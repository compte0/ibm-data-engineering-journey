'''code 1'''
#appel de la bibliothèque
import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)


'''code 2'''
import pandas as pd
# dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

print(df.iloc[2])  
print('-'*8)
print(df.loc[1])   

print('-'*8)

print(df[['Name', 'Age']])  
print('-'*8)

print(df[1:3])             

print('-'*8)

unique_dates = df['Age'].unique()
print(f"{unique_dates} valeur d'age unique" )

print(f'-'*8)

high_above_102 = df[df['Age'] > 25]
print(high_above_102)

print('-'*8)



'''code numpy'''
import numpy as np

# Creating a 1D array
arr_1d = np.array([1, 2, 3, 4, 5]) # **np.array()** is used to create NumPy arrays.