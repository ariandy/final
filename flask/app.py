from flask import Flask, render_template

from cleaning_data import employee_rank_by
from plotting import target

app = Flask(__name__)

# Home
@app.route('/')
def home():
    return render_template('home.html')

# Table
@app.route("/rank/", defaults={"column": "TotalWorkingYears"})
@app.route('/rank/<column>')
def data(column='Age'):
    data = employee_rank_by(column)
    return render_template('rank.html', data=data)

# Plots
@app.route('/plots')
def plots():
    data = target()
    return render_template('plots.html', data=data)

# ML

# About

if __name__ == '__main__':
    app.run(port=8888, debug=True)