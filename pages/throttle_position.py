import dash
from dash import dcc, html, callback
from dash.dependencies import Output, Input
import plotly.graph_objs as go
import random
from comp.obdScan import LiveData

throttleFigs = []

dash.register_page(__name__, path="/throttle_position")

#layout
layout = html.Div(
    [
        dcc.Graph(id="throttle-live-graph", animate=True),
        dcc.Interval(id="throttle-graph-update", interval=1800, n_intervals=0),
    ]
)

# callback to update the graph
@callback(Output("throttle-live-graph", "figure"), [Input("throttle-graph-update", "n_intervals")])
def update_graph(n):
    #generating the data
    # x_data = list(range(len(throttleFigs)))
    # throttleFigs.append(LiveData.throttle_pos_live())
    # y_data = throttleFigs

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
        title="Throttle Position Live Graph",
        xaxis=dict(range=[min(x_data), max(x_data)]),
        yaxis=dict(range=[min(y_data), max(y_data)]),
    )

    #return the graph figure
    return {"data": [trace], "layout" : layout}