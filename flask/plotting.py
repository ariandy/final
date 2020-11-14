import pandas as pd
import plotly
import plotly.graph_objects as go
import json

def target():
    df = pd.read_csv('../csv/imputed.csv')
    attrition = df['Attrition'].value_counts(normalize=True)

    fig = go.Figure([
        go.Bar(x=attrition.index, y=attrition.values)
    ])
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json