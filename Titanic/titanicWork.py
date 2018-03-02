from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('train.csv')
la = ['Pclass', 'Sex','Age','SibSp','Parch']
X = []
for i in la:
	X.append(data[i])
X.dropna(axis=1,how='all',inplace='True')

