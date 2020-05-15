import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, ClientsideFunction
import plotly.graph_objects as go
import pandas as pd

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

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H2(style={'textAlign': 'center'},
            children='All Premier League Match Results'),
    html.Label('Choose a season:'),
    dcc.Dropdown(
        id='dropdown',
        options=[
            dict(label=i, value=i) for i in df_results['Season'].unique()
        ],
        value='2017-18',
        multi=False
    ),
    dcc.Graph(id='all_results', figure=create_table(df_results)),
    html.Br(),
    html.H2(style={'textAlign': 'center'}, children='Top Goal Scorers'),
    dcc.Graph(figure=figure),
    html.Br()
])

@app.callback(
    Output("all_results", "figure"),
    [
        Input("dropdown", "value")
    ],
)
def table(season):
    df_filter = df_results[df_results["Season"]==season]
    return create_table(df_filter)

if __name__ == '__main__':
    app.run_server(port=8050, debug=True)
