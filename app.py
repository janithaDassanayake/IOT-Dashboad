import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd


import warnings

warnings.filterwarnings("ignore")

googleSheetId = '1rOvejFB9yC9rSQdQbIzpC_VFKj9GcCDA6mOSFnZl_aQ'
worksheetName = 'peoplecounts'
URL = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
    googleSheetId,
    worksheetName
)

data = pd.read_csv(URL)
data["Date"] = pd.to_datetime(data["Date"], infer_datetime_format=True)
data.sort_values("Date", inplace=True)

# Dropping all columns except for the Closing Price
data = data.drop(columns=['Price'])


# ----------------------------------------

googleSheetId = '1MBWHr0e5uE6wVRzmgx1kf4AFRhemANHqj_nmnHiKLOM'
worksheetName = 'Sanitizer'
URL = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
    googleSheetId,
    worksheetName
)

data1 = pd.read_csv(URL)
data1["Date"] = pd.to_datetime(data1["Date"], infer_datetime_format=True)
data1.sort_values("Date", inplace=True)
data1 = data1.loc['2020-01-01':]
# Dropping all columns except for the Closing Price








external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

# --------------------------------------------------------------------------------------

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = "Sanitizer Analytics"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="🧴🤲 = 🦠❌", className="header-emoji"),
                html.H1(
                    children=" Sanitizer Analytics", className="header-title"
                ),
                html.P(
                    children=""
                             "Analyze the behavior of Sanitizer Volume"
                             " and the Number of Customers",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data1["Date"],
                                    "y": data1["volume"],
                                    "type": "lines",
                                    "hovertemplate": "%{y:.2f} ml"
                                                     "<extra></extra>",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Sanitizer Usage Trend",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "ticksuffix": " ml",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17B897"],
                            },
                        },
                    ),
                    className="card",

                ),

                html.Div(
                    children=dcc.Graph(
                        id="volume-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["count"],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Customer Trend",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#E12D39"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="volume1-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["count"],
                                    "type": "lines",
                                    "hovertemplate": "Rs :%{y:.2f*100}"
                                                     "<extra></extra>",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Sanitizer Price Trend",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "Rs :",
                                    "fixedrange": True,
                                },
                                "colorway": ["#0000FF"],
                            },
                        },
                    ),

                    className="card",
                ),


            ],
            className="wrapper",
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
