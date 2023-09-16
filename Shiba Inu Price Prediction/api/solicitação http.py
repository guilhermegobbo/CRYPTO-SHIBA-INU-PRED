import requests

url = 'http://localhost:5000/previsao'

start_date = '2023-09-15'
end_date = '2023-09-20'

response = requests.get(f'{url}/{start_date}/{end_date}')

if response.status_code == 200:
    previsoes = response.json()['previsoes']
    for previsao in previsoes:
        print(f'Data: {previsao["data"]}, Previsão: {previsao["previsao"]}')
else:
    print(f'Erro: {response.json()}')
