import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('C:/Users/ccs/creditcard.csv',na_values='NULL')
print(data.head())
count_classes = pd.value_counts(data['Class'],sort = True).sort_index()
count_classes.plot(kind = 'bar')
plt.title('Fraud class histogram')
# plt.show()
from sklearn.preprocessing  import StandardScaler
# print(data['Amount'].reshape(-1,1))
data['normAmount']=StandardScaler().fit_transform(data['Amount'].values.reshape(-1,1))
print(data.head())
X = data.ix[:,data.columns != 'Class']
y = data.ix[:,data.columns == 'Class']

number_records_fraud = len(data[data.Class == 1])
fraud_indices = np.array(data[data.Class == 1].index)

normal_indices = data[data.Class == 0].index

random_normal_indices = np.random.choice(normal_indices,number_records_fraud,replace =False)
random_normal_indices = np.array(random_normal_indices)

under_samples_indices = np.concatenate([fraud_indices,random_normal_indices])