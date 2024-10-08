# -*- coding: utf-8 -*-
"""handwritten character recognition

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gHXjuZ_CPW6IMfSx9-Fe8O5xtUMsyKqr
"""

import pandas as pd

# Load the train and test datasets
train_df = pd.read_csv('written_name_train_v2.csv')
test_df = pd.read_csv('written_name_test_v2.csv')

# Combine train and test datasets
combined_df = pd.concat([train_df, test_df], ignore_index=True)

# Save the combined dataset to a new CSV file
combined_df.to_csv('combined_dataset.csv', index=False)

import pandas as pd

# Load the dataset
file_path = '/content/combined_dataset.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(data.head())

import pandas as pd

# Load the dataset
file_path = '/content/combined_dataset.csv'
data = pd.read_csv(file_path)

# Check for missing values
print(data.isnull().sum())

# Fill missing values (if any) with the mean (modify this as needed)
# Exclude columns with non-numeric data types for calculating the mean
numeric_data = data.select_dtypes(include=['number'])
data[numeric_data.columns] = numeric_data.fillna(numeric_data.mean())

# Convert categorical variables to dummy/indicator variables (if any)
data = pd.get_dummies(data)

# Assuming the last column is the target variable (modify as needed)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Display the shapes of X and y
print(X.shape, y.shape)