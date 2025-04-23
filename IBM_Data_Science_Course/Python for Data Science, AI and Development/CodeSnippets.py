import pandas as pd
import numpy as np
import requests
import json
import matplotlib as plt
%matpltlib inline



# APIs
# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
data = requests.get(url)
results = json.loads(data.text)
df2 = pd.json_normalize(results)
banana = df2.loc[df2["name"] == 'Banana']
banana.iloc[0,7]
df1 = pd.DataFrame(get_users())  


#Conditions
a = 5
a == 6
i = 6
i > 5
i = 2
i != 6

album_year = 1990
if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")
    
#Exception handling

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")
    
#Functions  

# Function Definition

def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)

# Make a Function for the calculation above

def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0 
    else:
        c = 5
    return(c) 
print()
sum()
len()


# Use append to add elements to list

L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
L
# Clone (clone by value) the list A

B = A[:]
B

# Get the column as a series

x = df['Length']
x

# Get the column as a dataframe

x = df[['Artist']]
type(x)


# Access the value on the first row and the first column

df.iloc[0, 0]

# Slicing the dataframe

df.iloc[0:2, 0:3]

# Access the column using the name

df.loc[1, 'Artist']


# Slicing the dataframe using name

df.loc[0:2, 'Artist':'Released']


# For loop example

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])     


# Exmaple of for loop, loop through list

for year in dates:  
    print(year)   
    
# Loop through the list and iterate on both index and element value

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)


# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")

# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
a.size
a.ndim
a.shape
a.mean()
a.min()
a.max()
np.subtract(a,b)
np.dot()
np.linespace(-2,2,num = 5)


a = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
# Multiply X with Y

Z = X * Y
Z = np.dot(A,B)

# Find the intersections

album_set1.union(album_set2)
album_set2.difference(album_set1)  
album_set1.intersection(album_set2) 


























