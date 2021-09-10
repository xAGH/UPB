import dash
import dash_core_components
import dash_html_components as html
import pandas

df = pandas.read_excel('database.xls')

app = dash.Dash()

app.layout = html.Div([
    html.H1("Este es mi proyecto 1 con python para un servidor"),
    html.Div("Este es el texto de mi pagina"),
    html.Div(df['barrio']),
    html.Div(df['enfermos']),
    html.Div(df['recuperados']),
    html.Div(df['muertos']),
    html.Div(df['lat']),
    html.Div(df['lon'])
])

if __name__ == '__main__':
    app.run_server(port=80,host='0.0.0.0')