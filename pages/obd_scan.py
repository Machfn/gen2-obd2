from dash import html, callback, Output, Input, clientside_callback
import dash
import json

dash.register_page(__name__, path="/obd_scan")


dete = 5


detections = [
    ("P0104", "Mass or Volume Air Flow Circuit Intermittent"),
    ("B0003", ""), # unknown error code, it's probably vehicle-specific
    ("C0123", ""),
    ("P0B07", "Electric/Auxiliary Transmission Fluid Pump Motor Phase W Current Low"),
    ("P0B0B", "Electric/Auxiliary Transmission Fluid Pump A Motor Supply Voltage Circuit High")
]

currentCode = "None Selected"
currentInfo = "This will be what we know about it"


detectionMessage = "No Detections" if not dete else f'{dete} detections in ECU'

detectionButtons = [html.Button(f"{detection[0]}", id="code-but_{}".format(detection[0]), style={"width": "100%", "height" : "50px", "font-size":"40px", "text-align":"left", "margin-bottom":"5px" }) for detection in detections]

layout = html.Div([
    html.Div([
        html.H2(detectionMessage),
        *detectionButtons,
    ], style= {
        "width": "600px",
        "height" : "600px",
        "overflow-y" : "scroll"
    }
    ),
    html.Div([
        html.H1(currentCode, id="obCode"),
        html.H3(currentInfo)
    ], style = {
        "padding" : "10px"
    })
], style= {
    "display" : "flex",
    "flex-wrap" : "wrap",
    "width" : "1200px",
    
})

@callback(
    Output("obCode", "children"),
    [Input("code-but_{}".format(detection[0]), "n_clicks") for detection in detections]
)
def generate_code(n_clicks):
    return n_clicks