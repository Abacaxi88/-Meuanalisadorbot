import os
import telebot
import time
import random

#7535321372:AAEJE01dWeIpo-uxf9vNW9BDb5OUpY4rW2E
TOKEN = os.getenv('TOKEN')

# ID do usuário para envio
USER_ID = 5284117781

bot = telebot.TeleBot(TOKEN)

# Simulação de jogos de eSoccer Battle 8min
jogos_esoccer_battle = [
    {
        "time_A": "Barcelona",
        "jogador_A": "Xavi10",
        "gols_A": 78,
        "confiança_A": "Alta",
        "time_B": "Real Madrid",
        "jogador_B": "Sergio9",
        "gols_B": 65,
        "confiança_B": "Média"
    },
    {
        "time_A": "PSG",
        "jogador_A": "NeymarJR",
        "gols_A": 82,
        "confiança_A": "Alta",
        "time_B": "Bayern",
        "jogador_B": "Muller25",
        "gols_B": 74,
        "confiança_B": "Alta"
    },
    {
        "time_A": "Chelsea",
        "jogador_A": "Mount19",
        "gols_A": 70,
        "confiança_A": "Média",
        "time_B": "Arsenal",
        "jogador_B": "Saka7",
        "gols_B": 69,
        "confiança_B": "Média"
    },
    {
        "time_A": "Liverpool",
        "jogador_A": "Salah11",
        "gols_A": 76,
        "confiança_A": "Alta",
        "time_B": "Manchester City",
        "jogador_B": "DeBruyne17",
        "gols_B": 80,
        "confiança_B": "Alta"
    },
]

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "✅ Bot iniciado! Análises serão enviadas a cada 5 minutos!")

def escolher_melhor_jogo():
    # Escolhe o melhor jogo baseado na soma das chances de gols
    melhor_jogo = sorted(jogos_esoccer_battle, key=lambda x: x['gols_A'] + x['gols_B'], reverse=True)[0]
    return melhor_jogo

def montar_mensagem(jogo):
    mensagem = (
        f"⚡ *Análise Detalhada - eSoccer Battle 8 Minutos*\n\n"
        f"🏟️ *Partida:*\n"
        f"*{jogo['time_A']}* ({jogo['jogador_A']}) vs *{jogo['time_B']}* ({jogo['jogador_B']})\n\n"
        f"📊 *Gols Individuais e Confiança:*\n"
        f"- *{jogo['time_A']}*:\n"
        f"  - Probabilidade de Gol: {jogo['gols_A']}%\n"
        f"  - Confiança: {jogo['confiança_A']}\n\n"
        f"- *{jogo['time_B']}*:\n"
        f"  - Probabilidade de Gol: {jogo['gols_B']}%\n"
        f"  - Confiança: {jogo['confiança_B']}\n\n"
        f"✅ *Sugestão*: Apostar em Mais de 1.5 gols!\n\n"
        f"⏳ *Nova análise a cada 5 minutos.*"
    )
    return mensagem

def enviar_melhor_jogo():
    while True:
        jogo = escolher_melhor_jogo()
        mensagem = montar_mensagem(jogo)
        try:
            bot.send_message(USER_ID, mensagem, parse_mode='Markdown')
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")
        time.sleep(300)  # 5 minutos

if __name__ == "__main__":
    from threading import Thread
    Thread(target=bot.polling, kwargs={'none_stop': True}).start()
    Thread(target=enviar_melhor_jogo).start()
