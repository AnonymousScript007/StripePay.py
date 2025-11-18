from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Reemplaza con tu token real
TOKEN = "TU_TOKEN_AQUI" "8445700529:AAEuEJBVQVJmLextpEud2yhYR328z9DAI0c"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu bot de Telegram 🤖")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Comandos disponibles:\n/start - Inicia el bot\n/help - Muestra esta ayuda")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))

print("🤖 Bot en marcha... Ctrl + C para detenerlo")
app.run_polling()
