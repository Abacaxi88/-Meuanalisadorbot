import requests
from bs4 import BeautifulSoup

def get_matches_info():
    matches = []

    # Sofascore (API pública)
    try:
        response = requests.get('https://api.sofascore.com/api/v1/sport/football/events/live')
        data = response.json()
        for event in data['events']:
            if 'eSoccer Battle' in event['tournament']['name'] and '8 min' in event['tournament']['name']:
                home = event['homeTeam']['name']
                away = event['awayTeam']['name']
                matches.append({
                    'home': home,
                    'away': away,
                    'source': 'Sofascore'
                })
    except:
        pass

    # Betano (scraping simples)
    try:
        url = "https://br.betano.com/sport/futebol/"
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('div', class_='some-class-for-matches'):  # Trocar depois pela classe real
            # Exemplo de extração
            home = item.find('span', class_='team-home-name').text
            away = item.find('span', class_='team-away-name').text
            matches.append({
                'home': home,
                'away': away,
                'source': 'Betano'
            })
    except:
        pass

    # Flashscore e Esoccer Bet: (estrutura semelhante)
    # (vou adicionar depois caso queira já completo)

    return matches
