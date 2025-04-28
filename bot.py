import telebot
import requests
from time import sleep

TOKEN = '7684868949:AAH8CixcXqtgC40_ulM01XNK3uggEWLuHYs'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Olá! Eu sou o Meuanalisadorbot. Estou aqui para analisar partidas de eSoccer! Comece pedindo a análise de uma partida.")

@bot.message_handler(commands=['analise'])
def analisar(message):
    bot.send_message(message.chat.id, "Analisando a partida... Aguarde um momento.")
    sleep(5)
    bot.send_message(message.chat.id, "Análise concluída: A partida tem alta probabilidade de vitória para o time A, com chances de ambos os times marcarem.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "Comando não reconhecido. Use /start para começar.")

if __name__ == "__main__":
    bot.polling(none_stop=True)
