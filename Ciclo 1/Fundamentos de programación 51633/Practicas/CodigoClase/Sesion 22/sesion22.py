#LLAMADO A LIBRERIAS
import pandas as pd
import ssl
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go

#DEFINICION DE FUNCIONES
def capturaweb_a_archivo(filename): 
    '''
    esta funcion captura los datos del covid19 a nivel mundial y lo guarda en el servidor local con el nombre 
    de filename de los argumentos, el programa no recibe parámetros, y la fuente de información es la URL:
     https://covid.ourworldindata.org/data/owid-covid-data.csv requiere de pandas y de ssl para su funcionamiento'''
    ssl._create_default_https_context = ssl._create_unverified_context
    df = pd.read_csv(
       'https://covid.ourworldindata.org/data/owid-covid-data.csv', 
       usecols=['date', 'location', 'total_cases','new_cases','total_deaths','new_deaths'], 
       parse_dates=['date'])
    nombrearchivo = str(filename) + ".csv"
    df.to_csv(nombrearchivo)

def captura_desdearchivo(filename):
    '''
    Funcion que lee el archivo filename.csv y carga la data en la variable de retorno
    '''
    datos = pd.read_csv(filename)
    return datos
def captura_pais_desdearchivo(pais,archivo):
    '''
    Función que lee la información de un solo pais y la carga en la variable de retorno
    '''
    datos_totales = pd.read_csv(archivo)
    datos = datos_totales[datos_totales['location'].isin([pais])]
    return datos
#DEFINICION DEL PROGRAMA PRINCIPAL
#capturaweb_a_archivo("data")
data = captura_pais_desdearchivo('Colombia','data.csv')
#print(data.head())
fechas = data['date'].tolist()
muertes = data['new_deaths'].tolist()

app = dash.Dash()
fig = go.Figure(data=[go.Scatter(x=fechas, y=muertes)])

app.layout = html.Div(children=[
    html.H1(children='Estadisticas de Covid19 para Colombia'),
    html.Div(children='El texto que me impone mi jefe, bla. bla, bla'),
    dcc.Graph(id='Numero de Muertes por Covid 19 diarias en Colombia',figure=fig)
])
#funcion lanzadora del main
if __name__ == '__main__':
    app.run_server(port=80,host='0.0.0.0',debug=True)