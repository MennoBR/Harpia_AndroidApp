
# API básica de monitoramento do clima na região da cidade indicada.

 
import requests
import datetime as dt

#Criando função para definir Kelvin como padrão:

def Padrao_Kelvin(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) * 32
    return celsius, fahrenheit


# Obtendo informações:
 def get_atual():
    BASE_URL =  "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "6c72ca7e4174d6429033197dabb040ca"
    CITY = "São Paulo"
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY


    resposta = requests.get(url).json()
    temp_kelvin = resposta['main']['temp']
    temp_celsius, temp_fahrenheit = Padrao_Kelvin(temp_kelvin)
    sensacao_kelvin = resposta['main']['feels_like']
    sensacao_celsius, sensacao_fahrenheit = Padrao_Kelvin(sensacao_kelvin)
    umidade = resposta['main']['humidity']
    descricao = resposta['weather'][0]['description']
    vento_velo = resposta['wind']['speed']
    nascer_sol = dt.datetime.utcfromtimestamp(resposta['sys']['sunrise'] + resposta['timezone'])
    por_do_sol = dt.datetime.utcfromtimestamp(resposta['sys']['sunset'] + resposta['timezone'])

atual = {
        'city': CITY,
        'temperature': temp_celsius,
        'humidity': umidade,
        'description': descricao
    }
    return atual

# Mostrando as informações ao Usuário:

print(f'Temperatura em {CITY}: {temp_celsius:.2f}C ou {temp_fahrenheit:.2f}F.')
print(f'Sensação térmica em {CITY} é de: {sensacao_celsius:.2f}C ou {sensacao_fahrenheit:.2f}F.')
print(f'Umidade relativa do ar: {umidade}%.')
print(f'Velocidade do vento em {CITY}: {vento_velo}km/h.')
print(f'Formação de Nuvens: {descricao}.')
print(f'O sol nasce em {CITY}: {nascer_sol} hora local.')
print(f'O sol se põe em {CITY}: {por_do_sol} hora local.')