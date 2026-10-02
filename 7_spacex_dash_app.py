# SpaceX Launch Records Dashboard (Plotly Dash)
# Run:  python 7_spacex_dash_app.py   then open http://127.0.0.1:8050
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Read the launch data into a pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

launch_sites = sorted(spacex_df['Launch Site'].unique())
site_options = [{'label': 'All Sites', 'value': 'ALL'}] + [{'label': s, 'value': s} for s in launch_sites]

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),

    # TASK 1: Launch Site drop-down input component
    dcc.Dropdown(id='site-dropdown',
                 options=site_options,
                 value='ALL',
                 placeholder='Select a Launch Site here',
                 searchable=True),
    html.Br(),

    # TASK 2: Pie chart showing successful launches
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    # TASK 3: Payload range slider
    dcc.RangeSlider(id='payload-slider',
                    min=0, max=10000, step=1000,
                    marks={i: str(i) for i in range(0, 10001, 2500)},
                    value=[min_payload, max_payload]),

    # TASK 4: Scatter chart payload vs. launch outcome
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])


# TASK 2: callback for the pie chart
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        success = spacex_df[spacex_df['class'] == 1]
        fig = px.pie(success, names='Launch Site',
                     title='Total Successful Launches by Site')
    else:
        site_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        counts = site_df['class'].value_counts().rename(index={1: 'Success', 0: 'Failure'}).reset_index()
        counts.columns = ['Outcome', 'Count']
        fig = px.pie(counts, values='Count', names='Outcome',
                     title=f'Total Success vs. Failed Launches for site {entered_site}',
                     color='Outcome', color_discrete_map={'Success': '#2E8B57', 'Failure': '#C0392B'})
    return fig


# TASK 4: callback for the scatter chart
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
               Input(component_id='payload-slider', component_property='value')])
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)]
    title = 'Correlation between Payload and Success for all Sites'
    if entered_site != 'ALL':
        df = df[df['Launch Site'] == entered_site]
        title = f'Correlation between Payload and Success for {entered_site}'
    fig = px.scatter(df, x='Payload Mass (kg)', y='class',
                     color='Booster Version Category', title=title)
    return fig


if __name__ == '__main__':
    app.run(debug=False, port=8050)
