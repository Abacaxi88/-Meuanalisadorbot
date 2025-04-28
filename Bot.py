import logging
import os
import time
import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configuração de logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 8180464376:AAHistnIPOrFPmPOrqpcwxTAFbusqllv05g
TOKEN = os.getenv("TOKEN")

# Funções do Bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bem-vindo ao Meu Analisador Bot! Use /analise para começar.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Comandos disponíveis:\n/start - Iniciar\n/help - Ajuda\n/analise - Ver análise de Esoccer")

async def analise(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Exemplo básico de scraping
    url = "https://betano.com/sport/soccer/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # Aqui você ajustaria para pegar os dados de odds ou jogos
        await update.message.reply_text("Análise pré-jogo enviada! (ajustar scraping conforme necessidade)")
    else:
        await update.message.reply_text("Erro ao acessar a Betano.")

# Rodar o Bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("analise", analise))

    logging.info("Bot iniciado...")
    app.run_polling()
