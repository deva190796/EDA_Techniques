#movie rating analysis
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
movies = pd.read_csv(r"C:\Users\Lenovo\Desktop\FullStackDataScience\DATASETS\Movie-Rating.csv")

print(movies)
print(type(movies))
print(movies.columns)
print(movies.info())
print(movies.shape)
print(movies.head())
print(movies.tail())

#Renaming Column Names
movies.columns = ['Film','Genre','CriticRating','AudienceRating','BudgetMillions','Year']
print(movies.columns)

#changin the type
print(movies.describe())
print(movies.info())
movies.Film = movies.Film.astype('category')
movies.Genre = movies.Genre.astype('category')
movies.Year = movies.Year.astype('category')
print(movies.info())
print(movies)

#visualisation
j = sns.jointplot(data = movies, x = 'CriticRating', y = 'AudienceRating', kind = 'reg')
plt.show()

vis1 = sns.lmplot(data = movies, x = 'CriticRating', y = 'AudienceRating', fit_reg = False, hue = 'Genre')
vis2 = sns.lmplot(data = movies, x = 'CriticRating', y = 'AudienceRating', fit_reg = True, hue = 'Genre')
plt.show()

#we can finalise and tell the client to not to make movies in romantic genre as the genre is facing low rating