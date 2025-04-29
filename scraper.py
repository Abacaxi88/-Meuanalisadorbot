import requests
from bs4 import BeautifulSoup

def buscar_partidas_betano():
    # Exemplo básico (é necessário adaptar depois para HTML atualizado da Betano)
    url = "https://www.betano.com/sports/football/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    partidas = []

    # Exemplo de como buscar (o seletor precisa ser adaptado conforme o HTML real)
    for jogo in soup.select(".event-row"):  # <-- exemplo fictício
        time_casa = jogo.select_one(".home-team").text.strip()
        time_fora = jogo.select_one(".away-team").text.strip()
        horario = jogo.select_one(".event-time").text.strip()

        partidas.append({
            "time_casa": time_casa,
            "time_fora": time_fora,
            "horario": horario,
            "confiança": "Alta"  # Aqui você poderá melhorar usando odds ou estatísticas
        })

    return partidas
