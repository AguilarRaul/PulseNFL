import altair as alt
from dash import dash, dcc, html, Input, Output
from vega_datasets import data
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
from PIL import Image

# Read in global data
nfl_data = pd.read_csv("data/nfl_data.csv")
pil_image = Image.open("assets/nfl.png")

# Setup app and layout/frontend
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MORPH])
app.layout = dbc.Container(
    [
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    html.Img(
                        src=pil_image,
                        style={
                            "margin": "0 auto",
                            "display": "block",
                            "height": "180px",
                        },
                    )
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.H1(
                        "NFL Pulse",
                        style={
                            "color": "black",
                            "fontSize": 50,
                            "textAlign": "center",
                            "fontFace": "bold",
                        },
                    )
                )
            ]
        ),
        html.Hr(),
        dbc.Row(
            [
                html.Label(
                    ["Welcome to NFL Pulse, sports enthusiast!"],
                    style={
                        "font-weight": "bold",
                        "text-align": "center",
                        "fontSize": 18,
                    },
                ),
                html.Hr(),
                html.Label(
                    [
                        "Here you will find your favorite team statistics in regular season including the winning percentage, the defensive rating (a measure of how good a team's defense was, the higher the better), the offensive rating (the higher the better), and the schedule difficulty rating (indicates how difficult the team's opponents were, a high number indicates that the opponents were difficult)."
                    ],
                    style={
                        "font-weight": "bold",
                        "text-align": "center",
                        "fontSize": 15,
                    },
                ),
            ]
        ),
        html.Hr(),
        dbc.Row(
            [
                html.Label(
                    ["Select your favorite team"],
                    style={
                        "font-weight": "bold",
                        "text-align": "left",
                        "fontSize": 15,
                    },
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id="team-widget",
                        value="Patriots",
                        options=np.sort(nfl_data["team_name"].unique()),
                        placeholder="Select your favorite team",
                    ),
                ),
            ],
        ),
        html.Hr(),
        dbc.Row(
            [
                html.Label(
                    ["Select the year range of your preference"],
                    style={
                        "font-weight": "bold",
                        "text-align": "left",
                        "fontSize": 15,
                    },
                ),
                dbc.Col(
                    dcc.RangeSlider(
                        id="year",
                        min=nfl_data["year"].min(),
                        max=nfl_data["year"].max(),
                        marks={i: str(i) for i in range(2000, 2020)},
                        value=[
                            nfl_data["year"].min(),
                            nfl_data["year"].max(),
                        ],
                    ),
                ),
            ],
        ),
        html.Hr(),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    html.Iframe(
                        id="line",
                        style={
                            "border-width": "10px",
                            "width": "100%",
                            "height": "400px",
                        },
                    )
                ),
                dbc.Col(
                    html.Iframe(
                        id="line_2",
                        style={
                            "border-width": "10px",
                            "width": "100%",
                            "height": "400px",
                        },
                    )
                ),
            ]
        ),
    ]
)

# Set up callbacks/backend for winning perc plot
@app.callback(
    Output("line", "srcDoc"),
    Input("team-widget", "value"),
    Input("year", "value"),
)
def plot_altair(team, year_filter):

    # Data wrangling
    nfl = nfl_data.copy()
    nfl["winning percentage"] = nfl["wins"] / 16
    nfl["winning perc"] = (nfl["winning percentage"] * 100).astype(str)
    nfl["winning perc"] = nfl["winning perc"] + "%"
    data_temp = nfl.copy().query("team_name==@team")
    data_temp = data_temp.query(
        "year>=@year_filter[0] & year<=@year_filter[1]"
    )
    data_temp["year"] = pd.to_datetime(data_temp["year"], format="%Y")
    click = alt.selection_multi(fields=["playoffs"], bind="legend")

    # Altair chart
    chart = (
        alt.Chart(data_temp)
        .mark_line(strokeDash=[4, 3], color="#d3d3d3")
        .encode(x="year", y="winning percentage:Q")
    )
    chart = chart + alt.Chart(data_temp).mark_point(size=100).encode(
        x=alt.X("year", axis=alt.Axis(title="NFL Season (Year)")),
        y=alt.Y(
            "winning percentage:Q",
            axis=alt.Axis(
                format="%", title="Winning Percentage", grid=False
            ),
        ),
        color=alt.Color(
            "playoffs",
            scale=alt.Scale(range=["#DF2E38", "#2F58CD"]),
            legend=alt.Legend(
                orient="right", title="Qualified for Playoffs"
            ),
        ),
        tooltip=["winning perc", "wins", "loss"],
        opacity=alt.condition(click, alt.value(0.9), alt.value(0.2)),
    ).properties(
        height=300,
        width=400,
        title="Team Winning Percentage During Regular Season",
    ).add_selection(
        click
    )
    return chart.to_html()


# Set up callbacks/backend for winning perc plot
@app.callback(
    Output("line_2", "srcDoc"),
    Input("team-widget", "value"),
    Input("year", "value"),
)
def plot_altair(team, year_filter):

    # Data wrangling
    nfl = nfl_data.copy()

    data_temp = nfl.copy().query("team_name==@team")
    data_temp = data_temp.query(
        "year>=@year_filter[0] & year<=@year_filter[1]"
    )
    data_temp["year"] = pd.to_datetime(data_temp["year"], format="%Y")

    data_temp = data_temp.rename(
        columns={
            "strength_of_schedule": "Schedule Difficulty Rating",
            "offensive_ranking": "Offensive Rating",
            "defensive_ranking": "Defensive Rating",
        }
    )

    nfl_stats = pd.melt(
        data_temp,
        id_vars=["team_name", "year"],
        value_vars=[
            "Schedule Difficulty Rating",
            "Offensive Rating",
            "Defensive Rating",
        ],
    )

    # Altair chart
    chart = (
        alt.Chart(nfl_stats)
        .mark_point(size=100)
        .encode(
            x=alt.X("year", axis=alt.Axis(title="NFL Season (Year)")),
            y=alt.Y(
                "value",
                axis=alt.Axis(title="Rating", grid=False),
            ),
            color=alt.Color(
                "variable",
                scale=alt.Scale(range=["#3C79F5", "#F55050", "#FFC93C"]),
                legend=alt.Legend(orient="right", title="Metric"),
            ),
            tooltip=["value"],
        )
        .properties(
            height=300,
            width=400,
            title="Team Performance Metrics During Regular Season",
        )
    )

    chart = chart + alt.Chart(nfl_stats).mark_line(
        strokeDash=[4, 3], color="#d3d3d3"
    ).encode(
        x="year",
        y="value",
        color=alt.Color(
            "variable",
        ),
    )

    return chart.to_html()


if __name__ == "__main__":
    app.run_server(debug=True)
