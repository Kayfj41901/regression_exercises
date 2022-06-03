import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression 
from math import sqrt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')




def plot_residuals(y, yhat): 
    plt.figure(figsize = (11,5))
    plt.subplot(121)
    plt.scatter(df.x, df.baseline_residual)
    plt.axhline(y = df.y.mean(), ls = ':', c = 'red')
    plt.xlabel('x')
    plt.ylabel('Residual')
    plt.title('Baseline Residuals')

    plt.subplot(122)
    plt.scatter(df.x, df.residual)
    plt.axhline(y = df.yhat, ls = ':', c='red')
    plt.xlabel('x')
    plt.ylabel('Residual')
    plt.title('OLS model residuals')
    return plot_residuals

def regression_errors(y, yhat):
    #sum of squared errors 
    SSE = df['residual^2'].sum()

    #total sum of squares 
    TSS = df['baseline_residual^2'].sum()

    #explained sum of squares 
    ESS = TSS - SSE

    #mean squared error 
    MSE = SSE/len(df)

    #root mean squared error 
    RMSE = sqrt(MSE)
    print(SSE, ESS, TSS, MSE, RMSE)

def baseline_mean_errors(y):
    SSE = df['residual^2'].sum()
    MSE = SSE/len(df)
    RMSE = sqrt(MSE)
    print(SSE, MSE, RMSE)

def better_than_baseline(y, yhat): 
    if 'RMSE' < 'RMSE baseline': 
        print(True)
    else: 
        print(False)
