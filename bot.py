import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from gateway_simulator import fake_gateway
from utils import parse_card

TOKEN = "TU_TOKEN_AQUI"

logging.basicConfig(level=logging.INFO)

/start

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"🤖 Checker SIMULADO\n"
"Usa:\n"
"/check 4111111111111111|12|25|123"
)

/check

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
user = update.effective_user
text = update.message.text

card = parse_card(text)  

if not card:  
    await update.message.reply_text("❌ Formato inválido")  
    return  

await update.message.reply_text("⏳ Procesando (simulado)...")  

result = fake_gateway(card)  

response = (  
    f"💳 {card}\n"  
    f"Status: {result['status']}\n"  
    f"Response: {result['message']}\n"  
    f"Retries: {result['retries']}\n"  
    f"Took: {result['time']}s\n"  
    f"User: {user.id}"  
)  

await update.message.reply_text(response)

Main

def main():
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))  
app.add_handler(CommandHandler("check", check))  

app.run_polling()

if name == "main":
main()
