import pandas as pd
df = pd.read_csv('C:/Users/ccs/creditcard.csv',na_values='NULL') ##注意csv文件实际显示是隐藏了后缀，
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
import numpy as np

df = df.dropna(how='any',axis=0)
# print(df.groupby('Class').size())
# print(df[0:2])
"""
Class
0    284315
1       492
dtype: int64
"""
# print(df.describe())
# plt.plot(df['Time'],df['Class'])
# plt.plot(df['V1'],df['Class'])
# plt.scatter(df['V1'],df['Class'])

# plt.scatter(df['V2'],df['Class'])
# plt.scatter(df['V3'],df['Class'])

# plt.scatter(df['Time'],df['Class'])
# print(df.isna())

df = df.fillna(0)
# df = df.sample(random_state=1)
"""
###随机选择一部分数据；默认随机抽取1行，即n=1;
最后，你还可以使用random_state参数来为sample的随机数生成器设置一个种子，它将会接收一个整数或者一个numpy RandomState 对象。"""
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                        hidden_layer_sizes=(5,2), random_state=1)
column_list = list(range(30))

df_tmp_1 = df[(df['Class'] == 1)]
df_tmp_0 = df[(df['Class'] == 0)]


train_x_1 = df_tmp_1.iloc[0:300, column_list]
train_y_1 = df_tmp_1.iloc[0:300, 30]

train_x_0 = df_tmp_0.iloc[0:200000, column_list]
train_y_0 = df_tmp_0.iloc[0:200000, 30]


test_x_1 = df_tmp_1.iloc[300:491, column_list]
test_y_1 = df_tmp_1.iloc[300:491, 30]

test_x_0 = df_tmp_0.iloc[200000:284314, column_list]
test_y_0 = df_tmp_0.iloc[200000:284314, 30]


train_x = pd.concat([train_x_0, train_x_1],axis=1)
train_y = pd.concat([train_y_0, train_y_1],axis=1)
test_x = pd.concat([test_x_0, test_x_1],axis=1)
test_y = pd.concat([test_y_0, test_y_1],axis=1)



# test_x = df.iloc[284316:, column_list]

# test_x = df.iloc[284316:284806,[30,]]


# print(df[(df['Class'] == 1)])
# #
# print(df.dtypes)

# print(test_x[1:5])

# test_y = df.ix[284316:,30]
clf.fit(train_x, train_y)
#print("层数----------------------")
#print(clf.n_layers_)
#print("权重----------------------")
#for cf in clf.coefs_:
#    print(cf)
#print("预测值----------------------")
y_pred=clf.predict(test_x)
m = len(y_pred)
##分错4个
t = 0
f = 0
for i in range(m):
    if y_pred[i] ==test_y[i]:
        t += 1
    else :
        f += 1
print("正确:"+str(t))
print("错误:"+str(f))


