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
X = data.loc[:,data.columns != 'Class']
y = data.loc[:,data.columns == 'Class']

number_records_fraud = len(data[data.Class == 1])
fraud_indices = np.array(data[data.Class == 1].index)

normal_indices = data[data.Class == 0].index

random_normal_indices = np.random.choice(normal_indices,number_records_fraud,replace =False)
random_normal_indices = np.array(random_normal_indices)

under_samples_indices = np.concatenate([fraud_indices,random_normal_indices])

under_sample_data = data.iloc[under_samples_indices,:]

X_undersample = under_sample_data.loc[:,under_sample_data.columns != 'Class']
y_undersample = under_sample_data.loc[:,under_sample_data.columns == 'Class']

##
print("Percentage of normal transactions: ",len(under_sample_data[under_sample_data.Class == 0])/len(under_sample_data))
print("Percentage of fraud transactions: ",len(under_sample_data[under_sample_data.Class == 1])/len(under_sample_data))
print("Total number of transactions in resample data : ",len(under_sample_data))

from  sklearn.model_selection  import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)
print("Number transactions train dataset : ",X_train.shape[0])
print("Number transactions test dataset",X_test.shape[0])
print("Total number of transactions: ",len(X_train)+len(X_test))

X_train_undersample,X_test_undersample,y_train_undersample,y_test_undersample = \
train_test_split(X_undersample,y_undersample,test_size=0.3,random_state=0)
print("")
print("Number transactions train dataset: ",len(X_train_undersample))
print("Number transacitions test dataset: ",len(X_test_undersample))
print("Total number of transactions: ",len(X_train_undersample)+len(X_test_undersample))


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection  import KFold,cross_val_score
from sklearn.metrics import confusion_matrix,precision_recall_curve,roc_auc_score\
    ,roc_curve,classification_report,auc,recall_score

def print_Kfold_scores(X_train_data,y_train_data):
    fold = KFold(n_splits=10,shuffle = True)

    #
    c_param_range = [0.01,0.1,1,10,100]
    result_table = pd.DataFrame(index=range(len(c_param_range),2),columns=['C_parameter','Mean recall score'])
    result_table['C_parameter'] = c_param_range
    j = 0
    for c_param in c_param_range:
        print('++++++++++++++++++++++++++')
        print('C parameter: ',c_param)
        print('++++++++++++++++++')
        print('')

        recall_accs = []
        for train_index, test_index  in fold.split(X_train_data):
            lr = LogisticRegression(C= c_param,penalty='l1')
            lr.fit(X_train_data.iloc[train_index,:],y_train_data.iloc[train_index,:].values.ravel())
            y_pred_undersample = lr.predict(X_train_data.iloc[test_index,:].values)

            recall_acc = recall_score(y_train_data.iloc[test_index,:].values,y_pred_undersample)
            recall_accs.append(recall_acc)
            print(' recall score: ',recall_acc)

        result_table.loc[j,'Mean recall score'] = np.mean(recall_accs)
        j += 1
        print('')
        print('Mean recall score',np.mean(recall_accs))
        print('')

    result_table['Mean recall score'] = result_table['Mean recall score'].astype('float64')
    best_c = result_table.loc[result_table['Mean recall score'].idxmax()]['C_parameter']
    print('*************************************************')
    print('Best model to choose from cross validation is with C parameter = ', best_c)
    print('*********************************************************************************')

    return best_c

best_c = print_Kfold_scores(X_train_undersample, y_train_undersample)
import itertools

def plot_confusion_matrix(cm,classes,normalize=False,title='confusion matrix',cmap=plt.cm.Blues):
    plt.imshow(cm,interpolation='nearest',cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks,classes,rotation=0)
    plt.yticks(tick_marks,classes)
    if normalize:
        cm = cm.astype('float')/cm.sum(axis=1)[:,np.newaxis]
    else:
        1
    thresh = cm.max()/2
    for i,j in itertools.product(range(cm.shape[0]),range(cm.shape[1])):
        plt.text(j,i,cm[i,j],horizontalalignment='center',color='white' if cm[i,j]>thresh else 'black')
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')



lr = LogisticRegression(C = best_c,penalty='l1')
lr.fit(X_train_undersample,y_train_undersample.values.ravel())
y_pred_undersample = lr.predict(X_test_undersample.values)

cnf_matrix = confusion_matrix(y_test_undersample,y_pred_undersample)
np.set_printoptions(precision=2)
print("Recall metric in the testing dataset: ",cnf_matrix[1,1]/(cnf_matrix[1,0]+cnf_matrix[1,1]))
class_names =[0,1]
plt.figure()
plot_confusion_matrix(cnf_matrix,classes=class_names,title='Confusion matrix')
plt.show()


lr = LogisticRegression(C=best_c,penalty='l1')
y_pred_undersample_score = lr.fit(X_train_undersample,y_train_undersample.values.ravel())\
    .decision_function(X_test_undersample.values)

fpr,tpr,thresholds = roc_curve(y_test_undersample.values.ravel(),
                               y_pred_undersample_score)

roc_auc = auc(fpr,tpr)
plt.title('Receiver Operating Characteristic')
plt.plot(fpr,tpr,label='AUC = %.2f'% roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0,1],[0,1],'r--')
plt.xlim([-0.1,1.0])
plt.ylim([-0.1,1.01])
plt.ylabel('True Positive Rate')
plt.xlabel('Fasle Positive Rate')
plt.show()

precision,recall,threshold = precision_recall_curve(y_test_undersample.values.ravel(),
                                                   y_pred_undersample_score)
plt.title('Precision-Recall Curve')
plt.plot(recall,precision)
plt.xlim([0.0,1.10])
plt.ylim([0.0,1.10])
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.show()