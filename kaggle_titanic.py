import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# data load
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

# data check - finding missing values(결측치)
print(train_df.isnull().sum())

# visualize missing values (heatmap)
sns.heatmap(train_df.isnull(), cbar=False, cmap='viridis')
plt.show() 

# Data search
train_df.head()

# data preprocessing - filling missing values as mean
# 결측치(없는데이터)를 평균값으로 채움
train_df['Age'].fillna(train_df['Age'].mean(), inplace=True)
test_df['Age'].fillna(test_df['Age'].mean(), inplace=True)

# data preprocessing - filling missing values as mode
# 결측치(없는데이터)를 최빈값으로 채움
train_df['Embarked'].fillna(train_df['Embarked'].mode()[0], inplace=True)
test_df['Embarked'].fillna(test_df['Embarked'].mode()[0], inplace=True)

# data preprocessing - dropping columns
# 컬럼(열)을 삭제함
train_df.drop(columns=['Cabin'], inplace=True)
test_df.drop(columns=['Cabin'], inplace=True)

# data preprocessing - Fare
train_df['Fare'].fillna(train_df['Fare'].mean(), inplace=True)
test_df['Fare'].fillna(test_df['Fare'].mean(), inplace=True)