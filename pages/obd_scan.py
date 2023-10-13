from dash import html, callback, Output, Input, clientside_callback, State, dcc
import dash
import json
from comp.obdScan import LiveData
import random

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

detectionButtons = [html.Button(f"{detection[0]}", id="code-but_{}".format(detection[0]), className='vomv', value=str(detection[1]), style={"width": "100%", "height" : "50px", "font-size":"40px", "text-align":"left", "margin-bottom":"5px" }) for detection in detections]

layout = html.Div([
    html.Div([
        html.Div([
            html.Button("clear", id="clear", style={"height" : "30px", "align-self": "center", "text-size" : "25px", "width" : "60px", "border-radius" : "10px"}),
            html.H2(["State: ", html.Strong("Not Ready", id='clkState', style={"color" : "red"})]),
            html.H2(detectionMessage, id='id_mess'),
            # dcc.Interval(
            #     id='list-update',
            #     interval=1*3600
            # )
        ], style={"display" : "flex", "flex-wrap" : "true", "flex-direction" : "row-reverse" , "justify-content" : "space-evenly"}),
        html.Div(children=[
            *detectionButtons,
        ], id="mess_out", style={
            "width" : "100%",
            "height" : "600px",
            "overflow-y" : "scroll"
        }),
    ], style= {
        "width": "600px",
        "height" : "600px"
    }
    ),
    html.Div([
        html.H1(currentCode, id="codeTit"),
        html.H3(currentInfo, id="codeMessg", style={"width" : "100%"})
    ], style = {
        "padding" : "10px",
        "width" : "600px"
    }),
], id="obCode", style= {
    "display" : "flex",
    # "flex-wrap" : "wrap",
    "justify-content" : "center",
    "width" : "1200px",
    "height" : "600px"
    
})


# @callback(Output('mess_out', 'children'), Input('clear', 'n_clicks'), prevent_initial_call=True)
# def update_detection(n_clicks):
#     detUpd = [html.Button(f"{detection[0]}", id="code-but_{}".format(detection[0]), className='vomv', value=str(detection[1]), style={"width": "100%", "height" : "50px", "font-size":"40px", "text-align":"left", "margin-bottom":"5px" }) for detection in detections]
#     upd =  html.Div(
#         [
#             *detUpd
#         ], style={
#             "width" : "100%",
#             "height" : "100%"
#         }
#     )
#     return upd



@callback(
    Output("obCode", "children"),
    Input("clear", "n_clicks"),
    prevent_initial_call=True
)
def generate_code(n_clicks):
    # res = LiveData.clear_the_codes()
    # return res
    sta = False
    ch = random.randint(1,2)
    chk = False
    if ch == 1:
        detections.clear()

    divText = ""

    if len(detections) == 0:
        divText =  "Codes Cleared Succesfully"
        sta = True
    else:
        divText = "Code Clear Either Failed or They perstained"


    return html.H1(
        [
            divText
        ], style= {
            "color" : "Green" if sta else "red",
            "justify-self" : "center",
            "align-self" : "center"
        }
    )
