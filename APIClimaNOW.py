
# API básica de monitoramento do clima na região da cidade indicada.


import requests
import datetime as dt

def Padrao_Kelvin(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

def get_atual(city):
    BASE_URL =  "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "6c72ca7e4174d6429033197dabb040ca"
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city

    resposta = requests.get(url).json()
    temp_kelvin = resposta['main']['temp']
    temp_celsius, temp_fahrenheit = Padrao_Kelvin(temp_kelvin)
    sensacao_kelvin = resposta['main']['feels_like']
    sensacao_celsius, sensacao_fahrenheit = Padrao_Kelvin(sensacao_kelvin)
    umidade = resposta['main']['humidity']
    descricao = resposta['weather'][0]['description']
    vento_velo = resposta['wind']['speed']
    nascer_sol = dt.datetime.fromtimestamp(resposta['sys']['sunrise'] + resposta['timezone']).strftime('%H:%M:%S')
    por_do_sol = dt.datetime.fromtimestamp(resposta['sys']['sunset'] + resposta['timezone']).strftime('%H:%M:%S')

    dados_clima = {
        'city': city,
        'temperature': temp_celsius,
        'feels_like': sensacao_celsius,
        'humidity': umidade,
        'description': descricao,
        'wind_speed': vento_velo,
        'sunrise': nascer_sol,
        'sunset': por_do_sol
    }

    return dados_clima

city = "São Paulo"
weather = get_atual(city)

print(f'Temperatura em {city}: {weather["temperature"]:.2f}C.')
print(f'Sensação térmica em {city} é de: {weather["feels_like"]:.2f}C.')
print(f'Umidade relativa do ar: {weather["humidity"]}%.')
print(f'Velocidade do vento em {city}: {weather["wind_speed"]}km/h.')
print(f'Formação de Nuvens: {weather["description"]}.')
print(f'O sol nasce em {city}: {weather["sunrise"]} hora local.')
print(f'O sol se põe em {city}: {weather["sunset"]} hora local.')

