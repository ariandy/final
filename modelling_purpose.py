import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, recall_score, log_loss

def Xy(df):
    X = df.drop('Attrition',axis=1)
    ordinal = ['Education', 'EnvironmentSatisfaction', 'JobInvolvement', 'JobLevel',
               'JobSatisfaction', 'PerformanceRating', 'RelationshipSatisfaction',
               'StockOptionLevel', 'WorkLifeBalance']
    X[ordinal] = X[ordinal].astype(str)
    X = pd.get_dummies(X, drop_first=True)
    y = df['Attrition'].map({'Yes':1,'No':0})
    
    return X, y

def basic_trainer(X, y, algorithm, test_size):
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y,
                                                        test_size= test_size, random_state=11111992)
    model = algorithm()
    model.fit(X_train, y_train)
    pred_test = model.predict(X_test)
    pred_train = model.predict(X_train)
    
    return X_train, X_test, y_train, y_test, pred_train, pred_test

def recall_report(y_train, pred_train, y_test, pred_test):
    recall_test = recall_score(y_test,pred_test)
    recall_train = recall_score(y_train,pred_train)
    return recall_train, recall_test

def log_loss_report(y_train, pred_train, y_test, pred_test):
    log_loss_test = log_loss(y_test,pred_test)
    log_loss_train = log_loss(y_train,pred_train)
    return log_loss_train, log_loss_test

def algorithm_report_accumulation(algorithm_list, X, y, test_size, notes):
    recall_train_arr = []
    recall_test_arr = []
#     log_loss_train_arr = []
#     log_loss_test_arr = []
    notes_arr = []

    for i in algorithm_list:
        X_train, X_test, y_train, y_test, pred_train, pred_test = basic_trainer(X, y, i, test_size)
        recall_train, recall_test = recall_report(y_train, pred_train, y_test, pred_test)
#         log_loss_train, log_loss_test = log_loss_report(y_train, pred_train, y_test, pred_test)
        recall_train_arr.append(recall_train)
        recall_test_arr.append(recall_test)
#         log_loss_train_arr.append(log_loss_train)
#         log_loss_test_arr.append(log_loss_test)
        notes_arr.append(notes)

    recall_df = pd.DataFrame({
        'Algorithm': algorithm_list,
        'Train Recall': recall_train_arr,
        'Test Recall': recall_test_arr,
#         'Train Log-loss': log_loss_train_arr,
#         'Test Log-loss': log_loss_test_arr,
        'Notes': notes_arr
    })
    return recall_df