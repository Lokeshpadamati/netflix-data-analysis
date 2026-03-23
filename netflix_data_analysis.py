# Netflix Data Analysis Project

# ================================
# 1. Import Libraries
# ================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# style
sns.set(style="whitegrid")

# ================================
# 2. Load Dataset
# ================================
df = pd.read_csv("netflix_titles.csv")

# preview
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# ================================
# 3. Data Cleaning
# ================================

# check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# fill missing values
df['country'].fillna('Unknown', inplace=True)
df['cast'].fillna('No Cast', inplace=True)
df['director'].fillna('No Director', inplace=True)

# drop rows where date_added is null
df = df.dropna(subset=['date_added'])

# convert date_added to datetime
df['date_added'] = pd.to_datetime(df['date_added'])

# extract year added
df['year_added'] = df['date_added'].dt.year

# ================================
# 4. Basic Analysis
# ================================

# Movies vs TV Shows
print("\nContent Type Count:")
print(df['type'].value_counts())

plt.figure()
sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows on Netflix")
plt.show()

# ================================
# 5. Top Countries
# ================================

top_countries = df['country'].value_counts().head(10)

plt.figure()
top_countries.plot(kind='bar')
plt.title("Top 10 Content Producing Countries")
plt.xlabel("Country")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# ================================
# 6. Content Growth Over Years
# ================================

content_growth = df['year_added'].value_counts().sort_index()

plt.figure()
content_growth.plot(kind='line', marker='o')
plt.title("Netflix Content Growth Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Shows")
plt.show()

# ================================
# 7. Most Popular Genres
# ================================

# split genres
df['listed_in'] = df['listed_in'].str.split(',')

# explode genres
genres = df.explode('listed_in')

# clean spaces
genres['listed_in'] = genres['listed_in'].str.strip()

top_genres = genres['listed_in'].value_counts().head(10)

plt.figure()
top_genres.plot(kind='bar')
plt.title("Top 10 Genres on Netflix")
plt.xticks(rotation=45)
plt.show()

# ================================
# 8. Ratings Analysis
# ================================

plt.figure()
sns.countplot(y='rating', data=df, order=df['rating'].value_counts().index)
plt.title("Content Ratings Distribution")
plt.show()

# ================================
# 9. Movies Duration Analysis
# ================================

# filter movies
movies = df[df['type'] == 'Movie']

# extract duration number
movies['duration'] = movies['duration'].str.replace(' min', '')
movies['duration'] = pd.to_numeric(movies['duration'], errors='coerce')

plt.figure()
sns.histplot(movies['duration'].dropna(), bins=30)
plt.title("Movie Duration Distribution")
plt.xlabel("Minutes")
plt.show()

# ================================
# 10. Key Insights (Print)
# ================================

print("\n🔍 Key Insights:")
print("1. Most content on Netflix are Movies.")
print("2. USA produces the highest number of shows.")
print("3. Content increased significantly after 2015.")
print("4. Drama and International genres are very popular.")
print("5. Most movies are around 90-120 minutes long.")
