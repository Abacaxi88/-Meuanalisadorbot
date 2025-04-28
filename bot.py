import os
import telebot
import time
import random

# 7535321372:AAEJE01dWeIpo-uxf9vNW9BDb5OUpY4rW2E
TOKEN = os.getenv('TOKEN')

# ID do usuário para quem o bot vai mandar as mensagens automaticamente
USER_ID = 5284117781  # Substitua aqui se quiser enviar para outro ID

bot = telebot.TeleBot(TOKEN)

# Simulação de possíveis jogos analisados
jogos_disponiveis = [
    {"partida": "Team A vs Team B", "gols": "Alta", "confiança": "92%"},
    {"partida": "Team C vs Team D", "gols": "Média", "confiança": "78%"},
    {"partida": "Team E vs Team F", "gols": "Alta", "confiança": "88%"},
    {"partida": "Team G vs Team H", "gols": "Baixa", "confiança": "64%"},
]

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Olá! Estou pronto para enviar análises de eSoccer para você!")

def escolher_melhor_jogo():
    # Simula escolher o jogo com maior confiança
    melhor_jogo = sorted(jogos_disponiveis, key=lambda x: int(x['confiança'].replace('%', '')), reverse=True)[0]
    return melhor_jogo

def enviar_melhor_jogo():
    while True:
        melhor_jogo = escolher_melhor_jogo()
        mensagem = (
            f"🔥 *Análise Especial de eSoccer*\n\n"
            f"🏟️ *Partida*: {melhor_jogo['partida']}\n"
            f"⚽ *Probabilidade de Gols*: {melhor_jogo['gols']}\n"
            f"✅ *Confiança*: {melhor_jogo['confiança']}\n\n"
            f"*Sugestão*: Apostar em Mais de 1.5 gols.\n"
            f"⏳ Atualizando em 5 minutos..."
        )
        try:
            bot.send_message(USER_ID, mensagem, parse_mode='Markdown')
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")
        time.sleep(300)  # 5 minutos = 300 segundos

# Inicia o bot
if __name__ == "__main__":
    from threading import Thread
    # Thread para continuar recebendo comandos
    Thread(target=bot.polling, kwargs={'none_stop': True}).start()
    # Thread para mandar jogos a cada 5 minutos
    Thread(target=enviar_melhor_jogo).start()
