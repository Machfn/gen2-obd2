# https://www.kbb.com/obd-ii/

import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.graph_objs as go
import random


#initializing the Dash app
app = dash.Dash(__name__)

#layout
app.layout = html.Div(
    [
        dcc.Graph(id="live-graph", animate=True),
        dcc.Interval(id="graph-update", interval=1000, n_intervals=0),
    ]
)

# callback to update the graph
@app.callback(Output("live-graph", "figure"), [Input("graph-update", "n_intervals")])
def update_graph(n):
    #generating the data
    x_data = list(range(10))
    y_data = [random.randint(0, 100) for _ in range(10)]

    #create the graph trace
    trace = go.Scatter(
        x=x_data,
        y=y_data,
        mode="lines+markers",
        name="Data",
        line={"color": "rgb(0, 255, 0)"},
        marker={"color": "rgb(0, 255, 0)", "size": 8},
    )

    # Create the graph
    layout = go.Layout(
        title="live Graph",
        xaxis=dict(range=[min(x_data), max(x_data)]),
        yaxis=dict(range=[min(y_data), max(y_data)]),
    )

    #return the graph figure
    return {"data": [trace], "layout" : layout}

if __name__ == "__main__":
    app.run_server(debug=True, port=5500)