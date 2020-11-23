from flask import Flask, render_template, request, send_from_directory, current_app

from cleaning_data import employee_rank_by, dataset
from plotting import attrition_pie_chart, age_distplot, age_totalworkingyears_distplot, gender_educationfield_composition
from prediction import get_unique, predictor

# -------------------------- Experimental purpose
# import io
# import seaborn as sns
# import numpy as np
# import base64
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# import matplotlib.pyplot as plt
# import seaborn as sns
# from flask import Flask, render_template, send_file
# -------------------------- Experimental purpose

app = Flask(__name__, static_url_path='', 
            static_folder='templates/static'
)

# Home
@app.route('/')
def home():
    return current_app.send_static_file('index.html')

# Sample
@app.route('/samples')
def samples():
    data = dataset().head(10)
    return render_template('samples.html', data=data)

# Rank
@app.route("/rank/", defaults={"column": "TotalWorkingYears"})
@app.route('/rank/<column>')
def rank(column='Age'):
    data = employee_rank_by(column)
    return render_template('rank.html', data=data)

# Plots
@app.route('/plots')
def plots():
    data = attrition_pie_chart()
    data2 = age_distplot()
    data3 = age_totalworkingyears_distplot()
    data4 = gender_educationfield_composition()
    return render_template('plots.html',
                            data=data, data2=data2, data3=data3, data4=data4)

# ML
@app.route('/prediction', methods=['GET','POST'])
def prediction():
    if request.method == 'POST':
        data = request.form
        data = data.to_dict()
        data['Age'] = int(data['Age'])
        data['DailyRate'] = int(data['DailyRate'])
        data['DistanceFromHome'] = int(data['DistanceFromHome'])
        data['Education'] = int(data['Education'])
        data['EnvironmentSatisfaction'] = int(data['EnvironmentSatisfaction'])
        data['HourlyRate'] = int(data['HourlyRate'])
        data['JobInvolvement'] = int(data['JobInvolvement'])
        data['JobLevel'] = int(data['JobLevel'])
        data['JobSatisfaction'] = int(data['JobSatisfaction'])
        data['MonthlyIncome'] = int(data['MonthlyIncome'])
        data['MonthlyRate'] = int(data['MonthlyRate'])
        data['NumCompaniesWorked'] = int(data['NumCompaniesWorked'])
        data['PercentSalaryHike'] = int(data['PercentSalaryHike'])
        data['PerformanceRating'] = int(data['PerformanceRating'])
        data['RelationshipSatisfaction'] = int(data['RelationshipSatisfaction'])
        data['StockOptionLevel'] = int(data['StockOptionLevel'])
        data['TotalWorkingYears'] = int(data['TotalWorkingYears'])
        data['TrainingTimesLastYear'] = int(data['TrainingTimesLastYear'])
        data['WorkLifeBalance'] = int(data['WorkLifeBalance'])
        data['YearsAtCompany'] = int(data['YearsAtCompany'])
        data['YearsInCurrentRole'] = int(data['YearsInCurrentRole'])
        data['YearsSinceLastPromotion'] = int(data['YearsSinceLastPromotion'])
        data['YearsWithCurrManager'] = int(data['YearsWithCurrManager'])
        result = predictor(data)[0][1]
        conclusion1 = "Kemungkinan pegawai tersebut untuk keluar adalah " + str(round(result,2)*100) + "%."
        conclusion2 = "Maka dengan nilai probabilitas tersebut, pegawai diprediksi "
        result_by_word = ''
        if result > 0.5:
            result_by_word = ' akan keluar.'
        else:
            result_by_word = ' tidak keluar.'
        conclusion2 += result_by_word 
        return render_template('result.html', conclusion1=conclusion1, conclusion2=conclusion2)
    data_BusinessTravel = get_unique(dataset(), 'BusinessTravel')
    data_Department = get_unique(dataset(), 'Department')
    data_EducationField = get_unique(dataset(), 'EducationField')
    data_Gender = get_unique(dataset(), 'Gender')
    data_JobRole = get_unique(dataset(), 'JobRole')
    data_MaritalStatus = get_unique(dataset(), 'MaritalStatus')
    data_OverTime = get_unique(dataset(), 'OverTime')
    return render_template('prediction.html',
                            data_EducationField = data_EducationField,
                            data_Department = data_Department,
                            data_BusinessTravel = data_BusinessTravel,
                            data_Gender = data_Gender,
                            data_JobRole = data_JobRole,
                            data_MaritalStatus = data_MaritalStatus,
                            data_OverTime = data_OverTime)

# -------------------------- Experimental purpose
# @app.route('/plt')
# def test():
#     x=[i for i in range(100)]
#     y=[i for i in range(100)]
#     fig,ax=plt.subplots(figsize=(6,6))
#     ax=sns.set(style="darkgrid")
#     sns.lineplot(x,y)
#     canvas=FigureCanvas(fig)
#     img = io.BytesIO()
#     fig.savefig(img)
#     img.seek(0)
#     return send_file(img,mimetype='img/png')
# -------------------------- Experimental purpose

# About

if __name__ == '__main__':
    app.run(port=9292, debug=True)