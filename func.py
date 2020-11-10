import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import anderson
from sklearn.preprocessing import LabelEncoder

def custom_desc(df):
    data_features = df.columns
    count = []
    unique = []
    top = []
    freq = []

    for item in data_features :
        count.append(df[item].count())
        unique.append(df[item].nunique())
        top.append(df[item].value_counts().idxmax())
        freq.append(df[item].value_counts().max())

    desc = pd.DataFrame({
        'count' : count,
        'unique' : unique,
        'top' : top,
        'freq' : freq
    }, index = df.columns)
    return desc.T

def custom_info(df, mode='all'):
    data_features = df.columns
    data_type = []
    null = []
    null_pct = []
    unique = []
    uniqueSample = []

    for item in data_features :
        data_type.append(str(df[item].dtype))
        null.append(sum(df[item].isnull()))
        null_pct.append(round(df[item].isna().sum()/len(df)*100,2))
        unique.append(df[item].nunique())
        uniqueSample.append(df[item].sample(3).values)

    desc = pd.DataFrame({
        'dataFeatures' : data_features,
        'dataType' : data_type,
        'null' : null,
        'nullPct' : null_pct,
        'unique' : unique,
        'uniqueSample' : uniqueSample
    })

    if mode == 'missing_values_only':
        desc = desc[desc.null>0].reset_index(drop=True).drop(['unique', 'uniqueSample'], axis=1)
    return desc

def zero_std(df):
    x = df.describe().T
    x = x[x['std']==0]
    return x['std'].index.to_list()

def categorical_converter(df):
    temp=df.copy()
    categorical_features = temp.select_dtypes(include = "object").columns
    le = LabelEncoder()
    for feature in categorical_features:
        temp[feature] = le.fit_transform(temp[feature].astype(str))
    return temp

def anderson_normality_test(data):
    result = {'Anderson' : {i : j for i,j in zip(anderson(data)[2],anderson(data)[1])}}
    result['Anderson']['statistic'] = anderson(data)[0]
    return result

def anderson_result_extractor(raw_anderson_result, significance_level):
    anderson_stat = raw_anderson_result['Anderson']['statistic']
    critical_value = raw_anderson_result['Anderson'][significance_level]
    accepted_hypothesis = ''
    if anderson_stat < critical_value:
        accepted_hypothesis = 'H0'
    else:
        accepted_hypothesis = 'HA'
    return anderson_stat, critical_value, accepted_hypothesis

def boxplot_for_outlier(data):
    data=data.melt()
    plt.figure(figsize=(15,10))
    plt.title("Boxplots for Numerical variables")
    bp=sns.boxplot(x='value',y='variable',data=data)
    bp.set_xticklabels(bp.get_xticklabels())
    plt.show()

def outlier_counter(df, column):
    Q1 = df[column].describe()['25%']
    Q3 = df[column].describe()['75%']
    Iqr = Q3 - Q1
    upper = Q3 + 1.5 * Iqr
    lower = Q1 - 1.5 * Iqr
    detector = df[~((df[column] >= lower) & (df[column] <= upper))][column]
    counter = len(detector)
    percentage = round(counter / len(df)*100, 2)
    return counter, percentage, detector.index

def univariate_outlier_report(df, outlier_columns):
    counter_arr = []
    percentage_arr = []

    for i in outlier_columns:
        counter, percentage, get_index = outlier_counter(df, i)
        counter_arr.append(counter)
        percentage_arr.append(percentage)

    outlier_df = pd.DataFrame({
        'Outlier Columns': outlier_columns,
        'Outlier Count': counter_arr,
        'Percentage': percentage_arr
    })
    return outlier_df

def get_all_univariate_outlier_index(df, outlier_columns):
    index_accumulator = []
    for i in outlier_columns:
        counter, percentage, get_index = outlier_counter(df, i)
        index_accumulator += get_index.to_list()
    return list(set(index_accumulator))