import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import ssl

app = dash.Dash()

def dataset():
    ssl._create_default_https_context = ssl._create_unverified_context
    datafinal = {}
    df = pd.read_csv('owid-covid-data.csv', 
    usecols=['date', 'location', 'total_cases','new_cases','total_deaths','new_deaths'])

    df = pd.read_csv(
         'https://covid.ourworldindata.org/data/owid-covid-data.csv', 
         usecols=['date', 'location', 'total_cases','new_cases','total_deaths','new_deaths'], 
         parse_dates=['date'])
    pais=['Colombia']
    datos = df[df['location'].isin(pais)]
    casostotales=datos['total_cases'].tolist()
    fechas=datos['date'].tolist()
    muertestotales=datos['total_deaths'].tolist()
    nuevasmuertes = datos['new_deaths'].tolist()
    nuevoscasos = datos['new_cases'].tolist()
    datafinal['pais'] = pais
    datafinal['casostotales'] = casostotales
    datafinal['fechas'] = fechas
    datafinal['muertestotales'] = muertestotales
    datafinal['nuevasmuertes'] = nuevasmuertes
    datafinal['nuevoscasos'] = nuevoscasos
    return datafinal



data = dataset()
fig = go.Figure(data=[go.Scatter(x=data['fechas'], y=data['nuevasmuertes'])])

app.layout = html.Div([
    html.H1('Covid 19 Colombia'),
    html.Div('carreta que debo mostrar en la pagina al inicio',id='text-content'),
    dcc.Graph(
        id='ejemplo grafica',
        figure=fig
    ),
    dcc.Slider(
        id='my-slider',
        marks = {i: '{}'.format(data['fechas'][i]) for i in range(0,len(data['fechas']),30)},#{0: {'label':data['fechas'][0]}},
        min = 0,#data['fechas'][0],#str(data['fechas'][0]).split("T")[0],
        max = len(data['fechas']),#str(data['fechas'][-1]).split("T")[0],
        value = len(data['fechas'])#str(data['fechas'][-1]).split("T")[0],
    )
    # dcc.Graph(id='map', figure={
    #     'data': [{
    #         'lat': df['lat'],
    #         'lon': df['lon'],
    #         'marker': {
    #             'color': 150,
    #             'size': df['enfermos'],
    #             'opacity': 0.6
    #         },
    #         'customdata': df['riesgo'],
    #         'type': 'scattermapbox'
    #     }],
    #     'layout': {
    #         'mapbox': {
    #             'accesstoken': 'pk.eyJ1IjoibGVvbmFyZG9iZXRhbmN1ciIsImEiOiJjazlybGNiZWcwYjZ6M2dwNGY4MmY2eGpwIn0.EJjpR4klZpOHSfdm7Tsfkw',
    #             'center' : {
    #                 'lat': 6.240737,
    #                 'lon': -75.589900
    #                 },
    #             'zoom' : 10
    #         },
    #         'hovermode': 'closest',
    #         'margin': {'l': 0, 'r': 0, 'b': 0, 't': 0}
    #     }
    # })
])


if __name__ == '__main__':
    app.run_server(debug=True,port=80,host='0.0.0.0')




