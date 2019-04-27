"""
kmeans=MiniBatchKMeans(n_clusters=2)
kmeans.fit(df.values)
"""


import pandas as pd
from scipy import stats
from sklearn.ensemble import RandomForestRegressor
data = pd.read_csv('C:/Users/ccs/Documents/kaggle_data/credits/cs-training.csv')
print(data[1:3])
# print(data.columns)
data.describe().to_csv('C:/Users/ccs/Documents/kaggle_data/credits/DataDescribe.csv')
print(data.describe())

import numpy as np
def set_missing(df):

    process_df = df.ix[:,[5,0,1,2,3,4,6,7,8,9]]
    print(process_df.columns)
    process_df = process_df.as_matrix().astype(np.float)

    # process_df = process_df.as_matrix()
    process_df[process_df == np.inf] = np.nan

    process_df= pd.DataFrame(process_df,columns=['MonthlyIncome', 'SeriousDlqin2yrs',
       'RevolvingUtilizationOfUnsecuredLines', 'age',
       'NumberOfTime30-59DaysPastDueNotWorse', 'DebtRatio',
       'NumberOfOpenCreditLinesAndLoans', 'NumberOfTimes90DaysLate',
       'NumberRealEstateLoansOrLines', 'NumberOfTime60-89DaysPastDueNotWorse'])

    known = process_df[process_df.MonthlyIncome.notnull()].as_matrix()
    unknown = process_df[process_df.MonthlyIncome.isnull()].as_matrix()
    X = known[:,1:]
    y = known[:,0]
    rfr = RandomForestRegressor(random_state=0,n_estimators=200,max_depth=3,n_jobs=-1)
    X =  pd.DataFrame(X,columns=['SeriousDlqin2yrs',
       'RevolvingUtilizationOfUnsecuredLines', 'age',
       'NumberOfTime30-59DaysPastDueNotWorse', 'MonthlyIncome',
       'NumberOfOpenCreditLinesAndLoans', 'NumberOfTimes90DaysLate',
       'NumberRealEstateLoansOrLines','NumberOfTime60-89DaysPastDueNotWorse'])
    X = X.fillna(0)
    test_X = unknown[:, 1:]

    test_X = pd.DataFrame(test_X, columns=['SeriousDlqin2yrs',
                                 'RevolvingUtilizationOfUnsecuredLines', 'age',
                                 'NumberOfTime30-59DaysPastDueNotWorse', 'MonthlyIncome',
                                 'NumberOfOpenCreditLinesAndLoans', 'NumberOfTimes90DaysLate',
                                 'NumberRealEstateLoansOrLines','NumberOfTime60-89DaysPastDueNotWorse'])
    test_X = test_X.fillna(0)


    rfr.fit(X,y)
    predicted = rfr.predict(test_X).round(0)
    print(predicted)
    df.loc[(df.MonthlyIncome.isnull()),'MonthlyIncome']=predicted

    return df

data = set_missing(data)
data = data.dropna()
data = data.drop_duplicates()
data.to_csv('C:/Users/ccs/Documents/kaggle_data/credits/MissingData.csv',index=False)

data = data[data['age']>0]
data = data[data['NumberOfTime30-59DaysPastDueNotWorse']<90]
data['SeriousDlqin2yrs']=1-data['SeriousDlqin2yrs']

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

print(data.columns)
print('******')
Y = data['SeriousDlqin2yrs']
X = data.ix[:,1:]
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=0)
train = pd.concat([Y_train,X_train],axis=1)
test = pd.concat([Y_test,X_test],axis=1)
clasTest = test.groupby('SeriousDlqin2yrs')['SeriousDlqin2yrs'].count()
train.to_csv('C:/Users/ccs/Documents/kaggle_data/credits/TrainData.csv',index=False)
test.to_csv('C:/Users/ccs/Documents/kaggle_data/credits/TestData.csv',index=False)

# d = train['age'].hist().get_figure()
# d.savefig('C:/Users/ccs/Documents/kaggle_data/credits/train_age_distribution.jpg')/
# plt.hist(X['age'], bins=15,color='blue')
# plt.hist(X['MonthlyIncome'], bins=50000,color='red')

plt.show()

# plt.plot(train['age']).
# plt.show()

def mono_bin(Y,X,n=20):
    r = 0
    good =Y.sum()
    bad =Y.count()-good
    while np.abs(r) <1:
        d1 = pd.DataFrame({'X':X,"Y":Y,"Bucket":pd.qcut(X,n)})
        d2 = d1.groupby("Bucket",as_index =True)
        r,p = stats.spearmanr(d2.mean().X,d2.mean().Y)
        n = n-1

    d3 = pd.DataFrame(d2.X.min(),columns=['min'])
    d3['min'] = d2.min().X
    d3['max'] = d2.max().X
    d3['sum'] = d2.sum().Y
    d3['total'] = d2.count().Y
    d3['rate'] = d2.mean().Y
    d3['woe'] = np.log((d3['rate']/(1-d3['rate']))/(good/bad))
    d4 =(d3.sort_index(by='min')).reset_index(drop=True)
    print('='*60)
    print(d4)
    return d4


np.unique