import telebot
import time
from scraper import buscar_partidas_betano

# TOKEN configurado
TOKEN = '7535321372:AAEJE01dWeIpo-uxf9vNW9BDb5OUpY4rW2E'
bot = telebot.TeleBot(TOKEN)

# Seu Chat ID
chat_id = 5284117781  # ID que você forneceu

def enviar_melhor_partida():
    partidas = buscar_partidas_betano()

    if not partidas:
        bot.send_message(chat_id, "Nenhuma partida encontrada no momento.")
        return

    melhor_partida = partidas[0]  # Pegando a primeira partida para exemplo
    mensagem = (
        f"🏆 Melhor Partida Encontrada:\n\n"
        f"**{melhor_partida['time_casa']}** vs **{melhor_partida['time_fora']}**\n"
        f"Horário: {melhor_partida['horario']}\n"
        f"Confiança: {melhor_partida['confiança']}\n\n"
        f"Analisado com dados reais!"
    )
    bot.send_message(chat_id, mensagem, parse_mode="Markdown")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bot de análise de eSoccer iniciado!")

if __name__ == "__main__":
    while True:
        enviar_melhor_partida()
        time.sleep(300)  # Aguarda 5 minutos entre envios
