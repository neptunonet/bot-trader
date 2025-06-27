from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from config import TELEGRAM_BOT_TOKEN
from main import analizar_ticker

def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="¡Hola! Enviá /analizar TICKER para obtener una señal.")

def analizar(update: Update, context: CallbackContext):
    try:
        ticker = context.args[0].upper()
        resultado = analizar_ticker(ticker)
        text = f"{ticker} → Entrada: {resultado['entrada']} | Salida: {resultado['salida']}"
        chat_id = update.effective_chat.id
        context.bot.send_message(chat_id=chat_id, text=text)
    except IndexError:
        context.bot.send_message(chat_id=update.effective_chat.id, text="⚠️ Tenés que pasar un ticker. Ej: /analizar AAPL")
    except Exception as e:
        chat_id = update.effective_chat.id if update.effective_chat else None
        if chat_id:
            context.bot.send_message(chat_id=chat_id, text=f"⚠️ Error: {e}")
        print(f"Error en analizar: {e}")

def main():
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("analizar", analizar))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()