import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import grasia_dash_components as gdc
import dash_html_components as html
from dash.dependencies import Input, Output, ClientsideFunction
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

external_scripts = [
    {'src' : 'https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'}
]
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, external_scripts=external_scripts)

server = app.server

df_results = pd.read_csv('../epl/datasets/results_since_92.csv')


def create_table(df_results):
    fig = go.Figure(data=[go.Table(
        header=dict(values=['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'Season'],
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[df_results.Date, df_results.HomeTeam, df_results.AwayTeam, df_results.FTHG, df_results.FTAG, df_results.FTR, df_results.Season],
                   fill_color='lavender',
                   align='left'))
    ])

    return fig


df_scorers = pd.read_csv('../epl/datasets/top_goal_scorers.csv')

figure = {
    'data': [
        dict(
            x=df_scorers[df_scorers['Player'] == i]['Goals'],
            y=df_scorers[df_scorers['Player'] == i]['Played'],
            text=df_scorers[df_scorers['Player'] == i]['Player'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=df_scorers[df_scorers['Player'] == i]['Country']
        ) for i in df_scorers['Player'].unique()
    ],
    'layout': dict(
        xaxis={'type': 'log', 'title': 'Goals'},
        yaxis={'title': 'Played'},
        margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
        hovermode='compare'
    )
}

df_stats = pd.read_csv(
    '../epl/datasets/stats_2006-2018/EPL_2018.csv').fillna(0)


def graph_stats(df, stat):
    fig = px.bar(df.sort_values(stat), x='Team', y=stat,
                 hover_data=['Team', stat], color=stat,
                 height=400)
    return fig


def graph_pie(df):
    fig = go.Figure(data=[go.Pie(labels=['Home', 'Away', 'Draw'], values=[len(df[df['FTR'] == 'H']['FTR']), len(df[df['FTR'] == 'A']['FTR']), len(df[df['FTR'] == 'D']['FTR'])], textinfo='label+percent',
                                 insidetextorientation='radial'
                                 )])
    return fig


df_standings = pd.read_csv(
    '../epl/datasets/EPLStandings.csv', index_col=0).T


def graph_line(team):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.linspace(2000, 2016, 17), y=list(df_standings[team]),
                             mode='lines+markers',
                             name='Standings'))

    fig.add_annotation(
        x=df_standings[df_standings[team] ==
                       df_standings[team].min()].index[0],
        y=df_standings[team].min(),
        xref="x",
        yref="y",
        text="Best Position",
        showarrow=True,
        font=dict(
            size=16,
            color="#ffffff"
        ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        ax=20,
        ay=-30,
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="#088da5",
        opacity=0.7
    )

    fig.add_annotation(
        x=df_standings[df_standings[team] ==
                       df_standings[team].max()].index[0],
        y=df_standings[team].max(),
        xref="x",
        yref="y",
        text="Worst Position",
        showarrow=True,
        font=dict(
            size=16,
            color="#ffffff"
        ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        ax=20,
        ay=-30,
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="#800000",
        opacity=0.7
    )
    fig['layout']['xaxis'].update(dtick=1)
    fig['layout']['yaxis'].update(dtick=1, autorange="reversed")
    return fig



# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "25rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "27rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.Div(children=[
        html.H2("Everything EPL", className="display-3"),
        html.Img(src="./assets/icon.png",height=200,width=200,alt="Awesome fucking logo")]),
        html.Hr(),
        html.H1(
            "Links:"
        ),
        dbc.Nav(
            [
                html.A(children="Section 1", href="#section1"),
                html.A(children="Section 2", href="#section2"),
                html.A(children="Section 3", href="#section3"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(
        id="page-content", style=CONTENT_STYLE,
        children=[
        html.H2(style={'textAlign': 'center'},
                children='All Premier League Match Results'),
        html.Label('Choose a season:'),
        dcc.Dropdown(
            id='dropdown_table',
            options=[
                dict(label=i, value=i) for i in df_results['Season'].unique()
            ],
            value='2017-18',
            multi=False
        ),
        dcc.Graph(id='all_results', figure=create_table(df_results)),
        html.Br(),

        html.Div(id="section1", children=[
        html.H2(style={'textAlign': 'center'}, children='Top Goal Scorers'),
        dcc.Graph(figure=figure),
        html.Br()]),

        html.Div(id="section2", children=[
        html.H2(style={'textAlign': 'center'},
                children='Stats'),
        html.Label('Choose a year:'),
        dcc.Dropdown(
            id='dropdown_stats_years',
            options=[
                dict(label=i, value=i) for i in range(2006, 2019)
            ],
            value='2018',
            multi=False
        ),
        html.Label('Choose a statistic:'),
        dcc.Dropdown(
            id='dropdown_stats',
            options=[
                dict(label=i, value=i) for i in (df_stats.columns)
            ],
            value='punches',
            multi=False
        ),
        dcc.Graph(id='all_stats', figure=graph_stats(
            df_stats.fillna(0), 'punches')),
        html.Br()]),

        html.H2(style={'textAlign': 'center'}, children='Home/Away Wins'),
        html.Label('Choose a season:'),
        dcc.Dropdown(
            id='dropdown_win_location',
            options=[
                dict(label=i, value=i) for i in range(2001, 2020)
            ],
            value='2019',
            multi=False
        ),
        dcc.Graph(id='win_location', figure=graph_pie(pd.read_csv(
            '../epl/datasets/full_team_matches_data/all_matches2019.csv').fillna(0))),
        html.Br(),
        html.H2(style={'textAlign': 'center'}, children='EPL Standings'),
        html.Label('Choose a team:'),
        dcc.Dropdown(
            id='dropdown_standings',
            options=[
                dict(label=i, value=i) for i in list(df_standings.columns)
            ],
            value='Arsenal',
            multi=False
        ),
        dcc.Graph(id='standings', figure=graph_line('Arsenal')),
        html.Br()
    ])


app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(
    Output("all_results", "figure"),
    [
        Input("dropdown_table", "value")
    ],
)
def table(season):
    df_filter = df_results[df_results["Season"] == season]
    return create_table(df_filter)


@app.callback(
    Output("all_stats", "figure"),
    [
        Input("dropdown_stats", "value"),
        Input("dropdown_stats_years", "value")
    ],
)
def stats(stat, year):
    df = pd.read_csv(
        '../epl/datasets/stats_2006-2018/EPL_{}.csv'.format(year)).fillna(0)
    return graph_stats(df, stat)


@app.callback(
    Output("win_location", "figure"),
    [
        Input("dropdown_win_location", "value")
    ],
)
def pie(year):
    df = pd.read_csv(
        '../epl/datasets/full_team_matches_data/all_matches{}.csv'.format(year)).fillna(0)
    return graph_pie(df)


@app.callback(
    Output("standings", "figure"),
    [
        Input("dropdown_standings", "value")
    ],
)
def standings(team):
    return graph_line(team)


if __name__ == '__main__':
    app.run_server(port=8050, debug=True)
