import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 로드
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

# 데이터 미리보기
print(train_df.head())
print(train_df.info())
print(train_df.describe())