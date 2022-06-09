import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 
import wrangle 
import sklearn
from sklearn.model_selection import train_test_split

#import data 
df = wrangle.wrangle_zillow()
#split data 
train, validate, test = wrangle.split_zillow_data(df)
train_Ventura = train[train.location == 'Ventura']
train_LA = train[train.location == 'LA']
train_Orange = train[train.location == 'Orange']
validate_Ventura = validate[validate.location == 'Ventura']
validate_LA = validate[validate.location == 'LA']
validate_Orange = validate[validate.location == 'Orange']
test_Ventura = test[test.location == 'Ventura']
test_LA = test[test.location == 'LA']
test_Orange = test[test.location == 'Orange']

def Ventura_Pie():
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

    #define data
    data1 = [9, 4, 50, 20, 14, 3]
    labels1 = ['1', '1.5', '2', '2.5', '3', '3.5/4/4.5']
    colors = sns.color_palette('coolwarm')[0:5]

    ax1.pie(data1, labels = labels1, colors = colors, autopct='%.0f%%')
    ax1.set_title('Number of bathrooms Ventura', fontdict = {'fontsize' : 14})

    data2 = [9, 45, 40, 6]
    labels2 = [2, 3, 4, 5]

    ax2.pie(data2, labels = labels2, colors = colors, autopct='%.0f%%')
    ax2.set_title("Number of bedrooms Ventura", fontdict = {'fontsize' : 14})
    plt.tight_layout()
    sns.set(rc = {'figure.figsize':(10,6)})

def Ventura_bedroom(): 
    a = sns.lmplot(x="yearbuilt", y="taxvaluedollarcnt", hue="bedroomcnt", col="bedroomcnt",
               data=train_Ventura, line_kws={'color': 'grey'}, palette='coolwarm', height=6, aspect=.4, x_jitter=.1)
    plt.tight_layout()

mode_bathrooms_Ventura = train_Ventura.bathroomcnt.isin([1, 1.5, 2, 2.5, 3])
mo_bath_V = train_Ventura[mode_bathrooms_Ventura]

def Ventura_bathroom():
    a = sns.lmplot(x="yearbuilt", y="taxvaluedollarcnt", hue="bathroomcnt", col="bathroomcnt",
               data=mo_bath_V, line_kws={'color': 'grey'}, palette='coolwarm', height=6, aspect=.4, x_jitter=.1)
    plt.tight_layout()

def Ventura_SquareFeet():
    a = sns.lmplot(x="calculatedfinishedsquarefeet", y="taxvaluedollarcnt",
               data=train_Ventura, line_kws={'color': 'red'}, palette = 'coolwarm')
    plt.title('How does square feet affect property tax value in Ventura?', fontdict = {'fontsize' : 18})

def Orange_Pie():
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

    #define data
    data1 = [8, 7, 44, 23, 15, 3]
    labels1 = ['1', '1.5', '2', '2.5', '3', '3.5/4/4.5/5']
    colors = sns.color_palette('coolwarm')[0:5]

    ax1.pie(data1, labels = labels1, colors = colors, autopct='%.0f%%')
    ax1.set_title('Number of bathrooms Orange County', fontdict = {'fontsize' : 14})

    data2 = [14, 49, 32, 5]
    labels2 = [2, 3, 4, 5]

    ax2.pie(data2, labels = labels2, colors = colors, autopct='%.0f%%')
    ax2.set_title("Number of bedrooms Orange County", fontdict = {'fontsize' : 14})
    plt.tight_layout()
    sns.set(rc = {'figure.figsize':(10,6)})

def Orange_bedroom():
    m = sns.lmplot(x="yearbuilt", y="taxvaluedollarcnt", hue="bedroomcnt", col="bedroomcnt",
               data=train_Orange, line_kws={'color': 'grey'}, palette='coolwarm', height=6, aspect=.4, x_jitter=.1)


mode_bathrooms_Orange = train_Orange.bathroomcnt.isin([1, 1.5, 2, 2.5, 3])
mo_bath_O = train_Orange[mode_bathrooms_Orange]
def Orange_bathroom():
    p = sns.lmplot(x="yearbuilt", y="taxvaluedollarcnt", hue="bathroomcnt", col="bathroomcnt",
               data=mo_bath_O, line_kws={'color': 'grey'}, palette='coolwarm', height=6, aspect=.4, x_jitter=.1)

def Orange_SquareFeet():
    a = sns.lmplot(x="calculatedfinishedsquarefeet", y="taxvaluedollarcnt",
               data=train_Orange, line_kws={'color': 'red'}, palette = 'coolwarm')
    plt.title('How does square feet affect property tax value in Orange County?', fontdict = {'fontsize' : 18})

def LA_Pie():
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

    #define data
    data1 = [28, 50, 19, 3]
    labels1 = ['1', '2', '3', '4/5']
    colors = sns.color_palette('coolwarm')[0:5]

    ax1.pie(data1, labels = labels1, colors = colors, autopct='%.0f%%')
    ax1.set_title('Number of bathrooms LA', fontdict = {'fontsize' : 14})

    data2 = [22, 51, 23, 4]
    labels2 = [2, 3, 4, 5]

    ax2.pie(data2, labels = labels2, colors = colors, autopct='%.0f%%')
    ax2.set_title("Number of bedrooms LA",  fontdict = {'fontsize' : 14})
    plt.tight_layout()
    sns.set(rc = {'figure.figsize':(10,6)})

def LA_bedroom():
    r = sns.lmplot(x="yearbuilt", y="taxvaluedollarcnt", hue="bedroomcnt", col="bedroomcnt",
               data=train_LA, line_kws={'color': 'grey'}, palette='coolwarm', height=6, aspect=.4, x_jitter=.1)

mode_bathrooms_LA = train_LA.bathroomcnt.isin([1, 2, 3, 4])
mo_bath_LA = train_LA[mode_bathrooms_LA]
def LA_bathroom():
    z = sns.lmplot(x="yearbuilt", y="taxvaluedollarcnt", hue="bathroomcnt", col="bathroomcnt",
               data=train_LA, line_kws={'color': 'grey'},palette='coolwarm', height=6, aspect=.4, x_jitter=.1)

def LA_SquareFeet():
    a = sns.lmplot(x="calculatedfinishedsquarefeet", y="taxvaluedollarcnt",
               data=train_LA, line_kws={'color': 'red'}, palette = 'coolwarm')
    plt.title('How does square feet affect property tax value in LA County?', fontdict = {'fontsize' : 18})