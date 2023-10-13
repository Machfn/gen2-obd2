import dash
from dash import dcc, html, callback
from dash.dependencies import Output, Input
import plotly.graph_objs as go
import random
from comp.obdScan import LiveData

airflowFigs = []

dash.register_page(__name__, path="/airflow_graph")

#layout
layout = html.Div(
    [
        dcc.Graph(id="airflow-live-graph", animate=True),
        dcc.Interval(id="airflow-graph-update", interval=1800, n_intervals=0),
    ]
)

# callback to update the graph
@callback(Output("airflow-live-graph", "figure"), [Input("airflow-graph-update", "n_intervals")])
def update_graph(n):
    #generating the data
    # x_data = list(range(len(airflowFigs)))
    # airflowFigs.append(LiveData.airflow_rate_live())
    # y_data = airflowFigs

    x_data = list(range(10))
    y_data = [random.randint(0, 100) for _ in range (10)]

    #create the graph trace
    trace = go.Scatter(
        x=x_data,
        y=y_data,
        mode="lines+markers",
        name="Data",
        line={"color": "rgb(115, 28, 196)"},
        marker={"color": "rgb(0, 255, 0)", "size": 8},
    )

    # Create the graph
    layout = go.Layout(
        title="airflow rate Live Graph",
        xaxis=dict(range=[min(x_data), max(x_data)]),
        yaxis=dict(range=[min(y_data), max(y_data)]),
    )

    #return the graph figure
    return {"data": [trace], "layout" : layout}