import pandas as pd
import seaborn as sns

def employee_rank_by(column):
    x = dataset()
    x = x.sort_values(ascending=False, by=column)[['EmployeeNumber', column]]
    return x.head(10)

def dataset():
    employee_id = pd.read_csv('csv/employee_attrition_train.csv')['EmployeeNumber'].astype(str)
    x = pd.concat([employee_id, imputed()], axis=1)
    return x

def imputed():
    return pd.read_csv('csv/imputed.csv')
