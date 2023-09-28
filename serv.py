# https://www.kbb.com/obd-ii/

import dash
from dash import dcc, html, Dash
from dash.dependencies import Output, Input
import plotly.graph_objs as go
import random

#initializing the Dash app
app = Dash(__name__, use_pages=True)



if __name__ == "__main__":
    app.run_server(debug=True, port=5550)