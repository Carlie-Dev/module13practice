import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

#Create numpy array
array = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(array)

#Access numpy array element

print('\nElement at row 1, collum 2:', array[1,2])

#Slice to get the first two rows and collums
print(array[:2,:2])

#Operations
#add to each element
print(array + 2)
print(array)
#Not perminate. Do this to make it perminate. array = array + 2
#Transpose Array #Turns the rows into collums
print('\n')
print(array.T)

#row-wise and collum wise

print('Some of Each Row')
#x axis
print(np.sum(array, axis=1))
#y axis
print(np.sum(array, axis=0))

#Get the mean of all the values

print('Mean of all the values')
print(np.mean(array))

#Reshape array
print(array.reshape(-1))

#############################################################################################

#pandas

#Start with data
data = {
    'Name' : ['Bud','Anna','Payton','Darian'],
    'Age' : [25,25,12,98],
    'Salary' : [60000,57000,85000,120000]
}

#create dataframe

df = pd.DataFrame(data)
print(df)

#accessing data

print(df['Name'])

#multiply collums
print(df[['Name','Salary']])

#Accessing rows using loc and iloc

print('\nSecond row using iloc')
print(df.iloc[1])

print('\nRows where age is greater than 30')
print(df.loc[df['Age'] > 30])

#adding a collum
df['Years In Company'] = [2,4,5,8]
print(f'\n{df}')

#Operations
#calculate mean of collumn

mean_salary = df['Salary'].mean()
print(f'Mean: ${mean_salary}')

#Group and aggragate data
grouped_df = df.groupby('Age').sum()
print(grouped_df)

#########################################################################
#matplotlib

#Generate some data

x = np.linspace(0, 10, 100)
y = np.sin(x)
# print(x)
# print(y)

#Line plot
#plot size is 8 by 4
plt.figure(figsize=(8,4))
plt.plot(x,y, label = 'sin(x)')
plt.title('Line Plot')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show()

#Bar chart
plt.figure(figsize=(8,4))
plt.bar(x,y, label = 'sin(x)')
plt.title('Bar Plot')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show()

#Bar chart
name = ['Alice','Bob','Cody','Dean','Eddy']
values = [30,45,67,100,101]
plt.bar(name,values, color='red')
plt.show()