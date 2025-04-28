import random

def analyze_best_match(matches):
    if not matches:
        return None

    best_match = random.choice(matches)  # Por enquanto, sorteia um aleatório

    # Simular probabilidades de gols individuais
    home_goals = random.randint(60, 90)  # Exemplo: 60% a 90%
    away_goals = random.randint(40, 70)  # Exemplo: 40% a 70%

    # Confiança com base na % dos times
    confidence = 'Alta' if home_goals > 75 and away_goals > 50 else 'Média' if home_goals > 60 else 'Baixa'

    # Formatar a mensagem para o bot enviar:
    message = f"""
🏟️ {best_match['home']} vs {best_match['away']}
Fonte: {best_match['source']}

⚽ Gols Individuais:
- {best_match['home']}: {home_goals}% chance
- {best_match['away']}: {away_goals}% chance

Confiança da Análise: {confidence}
    """

    return message
