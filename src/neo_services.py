#importando a biblioteca requests, utilizada para requisições HTTP em python

import requests

def get_neos():
    response = requests.get("https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=DEMO_KEY")
    
    if response.status_code == 200:
        #converte aresposta JSON em um dicionário python
        result = response.json()
        #retorna a lista de objetos próximos da terra
        return result["near_earth_objects"]
    else:
        #caso a resposta não seja 200, lança uma exceção com o código do status
        response.raise_for_status()