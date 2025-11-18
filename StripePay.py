import logging
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# TU TOKEN AQUÍ (reemplaza con el que te dio BotFather)
TELEGRAM_TOKEN = '8382736754:AAHg747Y_jUHVNOldT8xE5m3HnFShlJtfCU'

# Algoritmo de Luhn
def luhn_algorithm(number):
    digits = [int(d) for d in number]
    checksum = 0
    for i in range(len(digits)-1, -1, -1):
        digit = digits[i]
        if (len(digits) - i) % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    return (10 - (checksum % 10)) % 10

# Validar tarjeta
def simulate_payment(card_number, exp_month, exp_year, cvv):
    now = datetime.now()
    if luhn_algorithm(card_number[:-1]) != int(card_number[-1]):
        return "❌ Número inválido"
    if exp_year < now.year or (exp_year == now.year and exp_month < now.month):
        return "❌ Tarjeta expirada"
    if len(cvv) != 3 or not cvv.isdigit():
        return "❌ CVV inválido"
    return "✅ Pago exitoso"

# Procesar tarjeta individual
def process_card(line):
    parts = line.strip().split('|')
    if len(parts) != 4:
        return f"{line} -> ❌ Formato incorrecto"
    try:
        card, mm, yy, cvv = parts
        result = simulate_payment(card, int(mm), int(yy), cvv)
        return f"{card}|{mm}|{yy}|{cvv} -> {result}"
    except:
        return f"{line} -> ❌ Error al procesar"

# Comando /stripe
async def stripe_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        message = ' '.join(context.args)
        cards = message.strip().split('\n')
        results = [process_card(card) for card in cards if card.strip()]
        reply = '\n'.join(results[:50])
        if len(results) > 50:
            reply += "\n⚠️ Solo se muestran los primeros 50 resultados."
        await update.message.reply_text(reply)
    else:
        await update.message.reply_text("⚠️ Usa el formato:\n/stripe <tarjetas separadas por línea>")

# Función principal
async def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("stripe", stripe_handler))
    print("✅ Bot en funcionamiento...")
    await app.run_polling()

# Ejecutar bot
if name == "main":
    import asyncio
    asyncio.run(main())

# Importante: reemplazas esta línea con tu token:

TELEGRAM_TOKEN = '8382736754:AAHg747Y_jUHVNOldT8xE5m3HnFShlJtfCU'
