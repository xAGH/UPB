import dash
import dash_core_components
import dash_html_components
import pandas

df = pandas.read_excel('F:/UPB/Ciclo 1/Fundamentos de programación 51633/Practicas/Server/database.xls')

app = dash.Dash()

app.layout = dash_html_components.Div([
    dash_html_components.H1("Este es mi proyecto 1 con python para un servidor."),
    dash_html_components.Div("Este es el texto de mi página."),
    
])

if __name__ == '__main__':
    app.run_server(port=80, host='0.0.0.0')