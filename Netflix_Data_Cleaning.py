'''
This code takes a dataset of Netflix data and cleans it to prepare for analysis purposes.
'''
import pandas as pd

# Read dataset into a dataframe
filePath = "/Users/brendan/Downloads/netflix_titles.csv"
df = pd.read_csv(filePath)

# Drop any duplicates found in the data
df = df.drop_duplicates()

# Replace all null values with "Not Available"
df = df.fillna("Not Available")

# Drop the cast, listed_in, and description columns as they are not needed in analysis
df = df.drop(columns = ("cast", "listed_in", "description"), errors = 'ignore')

# Save cleaned dataset as a new csv file
cleanFilePath = "/Users/brendan/Downloads/netflix_titles_cleaned.csv"
df.to_csv(cleanFilePath, index = False)


