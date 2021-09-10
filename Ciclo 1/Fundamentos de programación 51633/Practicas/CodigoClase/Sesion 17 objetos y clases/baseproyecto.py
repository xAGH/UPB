import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
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