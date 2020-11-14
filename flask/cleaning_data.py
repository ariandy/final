import pandas as pd
import seaborn as sns


def employee_rank_by(column):
    employee_id = pd.read_csv('../csv/employee_attrition_train.csv')['EmployeeNumber'].astype(str)
    df = pd.read_csv('../csv/imputed.csv')
    x = pd.concat([employee_id, df], axis=1)
    x = x.sort_values(ascending=False, by=column)[['EmployeeNumber', column]]
    return x.head(10)

