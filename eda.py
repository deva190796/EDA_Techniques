#eda 
import pandas as pd
import numpy as np
emp = pd.read_excel(r"C:\Users\Lenovo\Desktop\FSDS\EDA\Rawdata.xlsx")
print(emp)
print(id(emp))
print(emp.columns)
print(emp.shape)
print(emp.head())
print(emp.tail())
print(emp.info())
print(emp.isnull())
print(emp.isna())
print(emp.isnull().sum())
print(emp.isnull().any().any())

#cleaning
emp['Name'] = emp['Name'].str.replace(r'\W','',regex = True)
print(emp['Name'])
emp['Domain'] = emp['Domain'].str.replace(r"\W","",regex = True)
print(emp['Domain'])
emp['Age'] = emp['Age'].str.replace(r'\W','',regex = True)
print(emp['Age'])
emp['Age'] = emp['Age'].str.extract('(\\d+)')
print(emp)
emp['Salary'] = emp['Salary'].str.replace(r'\W','',regex = True)
print(emp)
emp['Exp'] = emp['Exp'].str.extract('(\\d+)')
print(emp)

clean_data = emp.copy()
print(clean_data)
print(clean_data.isnull().sum())

clean_data["Age"] = clean_data['Age'].fillna(np.mean(pd.to_numeric(clean_data['Age'])))
clean_data['Exp'] = clean_data['Age'].fillna(np.mean(pd.to_numeric(clean_data['Exp'])))
clean_data['Location'] = clean_data['Location'].fillna(clean_data['Location'].mode()[0])
print(clean_data.isnull().sum())
print(clean_data.info())

clean_data['Salary'] = clean_data['Salary'].astype(int)
clean_data['Exp'] = clean_data['Exp'].astype(int)
clean_data['Age'] = clean_data['Age'].astype(int)
print(clean_data.info())


#changing type
clean_data['Name'] = clean_data['Name'].astype('category')
clean_data['Domain'] = clean_data['Domain'].astype('category')
clean_data['Location'] = clean_data['Location'].astype('category')
print(clean_data.info())

#conversion of dataset to csv file

#visualisation
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
print(clean_data['Salary'])

#univariate analysis
vis1 = sns.distplot(clean_data['Salary'])
plt.show()
vis2 = sns.histplot(clean_data['Salary'])
plt.show()

#bivariate analysis
vis3 = sns.lmplot(data = clean_data,x = 'Exp', y = 'Salary')
plt.show()

#variable identification
x_iv = clean_data[['Name','Domain','Age','Location','Exp']]
print(x_iv)
x_dv = clean_data['Salary']

#imputations
imputation = pd.get_dummies(clean_data, dtype = int)
print(imputation)