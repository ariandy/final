import pandas as pd
import plotly
import plotly.graph_objects as go
import plotly.figure_factory as ff
import json

def fig_json(fig):
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

def dataset():
    return pd.read_csv('csv/imputed.csv')

def age_distplot():
    df = dataset()
    x = df['Age'].values
    group_labels = ['Age'] # name of the dataset
    fig = ff.create_distplot([x], group_labels)
    return fig_json(fig)

def attrition_pie_chart():
    df = dataset()
    x = df['Attrition'].value_counts(normalize=True)
    fig = go.Figure(data=[go.Pie(labels=x.index, values=x.values, hole=.3)])
    return fig_json(fig)

def age_totalworkingyears_distplot():
    df = dataset()
    x = df.Age
    y = df.TotalWorkingYears

    fig = go.Figure()
    fig.add_trace(go.Histogram2dContour(
            x = x,
            y = y,
            colorscale = 'Blues',
            reversescale = True,
            xaxis = 'x',
            yaxis = 'y'
        ))
    fig.add_trace(go.Scatter(
            x = x,
            y = y,
            xaxis = 'x',
            yaxis = 'y',
            mode = 'markers',
            marker = dict(
                color = 'rgba(0,0,0,0.3)',
                size = 3
            )
        ))
    fig.add_trace(go.Histogram(
            y = y,
            xaxis = 'x2',
            marker = dict(
                color = 'rgba(0,0,0,1)'
            )
        ))
    fig.add_trace(go.Histogram(
            x = x,
            yaxis = 'y2',
            marker = dict(
                color = 'rgba(0,0,0,1)'
            )
        ))

    fig.update_layout(
        autosize = False,
        xaxis = dict(
            zeroline = False,
            domain = [0,0.85],
            showgrid = False
        ),
        yaxis = dict(
            zeroline = False,
            domain = [0,0.85],
            showgrid = False
        ),
        xaxis2 = dict(
            zeroline = False,
            domain = [0.85,1],
            showgrid = False
        ),
        yaxis2 = dict(
            zeroline = False,
            domain = [0.85,1],
            showgrid = False
        ),
        height = 600,
        width = 600,
        bargap = 0,
        hovermode = 'closest',
        showlegend = False
    )
    return fig_json(fig)

def gender_educationfield_composition():
    df = dataset()
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=df.EducationField.value_counts().index,
        x=df.EducationField.value_counts().values,
        name='Female',
        orientation='h',
        marker=dict(
            color='rgba(246, 78, 139, 0.6)',
            line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
        )
    ))
    fig.add_trace(go.Bar(
        y=df.EducationField.value_counts().index,
        x=df.EducationField.value_counts().values,
        name='Male',
        orientation='h',
        marker=dict(
            color='rgba(58, 71, 80, 0.6)',
            line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
        )
    ))

    fig.update_layout(barmode='stack')
    return fig_json(fig)