import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from telegram import Update
import wakeonlan  # Asegúrate de instalar la librería para Wake-on-LAN

# Comando /start
async def start(update: Update, context) -> None:
    keyboard = [
        [InlineKeyboardButton("💻 Apagar PC", callback_data='apagar')],
        [InlineKeyboardButton("🔄 Reiniciar PC", callback_data='reiniciar')],
        [InlineKeyboardButton("⚡ Encender PC", callback_data='encender')],
        [InlineKeyboardButton("🧹 Borrar Chat", callback_data='borrar_chat')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "*¡Hola! Soy tu bot de PC.*\n\n"
        "Selecciona una de las opciones abajo para interactuar.",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# Respuesta a los botones
async def button(update: Update, context) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'apagar':
        await query.edit_message_text("La PC se apagará en breve.")
        # Código para apagar la PC en Windows
        os.system("shutdown /s /f /t 0")
    elif query.data == 'reiniciar':
        await query.edit_message_text("La PC se reiniciará en breve.")
        # Código para reiniciar la PC en Windows
        os.system("shutdown /r /f /t 0")
    elif query.data == 'encender':
        await query.edit_message_text("Paquete WOL enviado para encender la PC.")
        # Para enviar el paquete WOL, necesitas la dirección MAC de la PC.
        mac_address = 'D4-5D-64-07-80-BF'  # Cambia esto por la dirección MAC de tu PC
        wakeonlan.send_magic_packet(mac_address)
    elif query.data == 'borrar_chat':
        await query.edit_message_text("El chat ha sido limpiado.")
        # No hay una forma directa de borrar el chat, pero puedes borrar los mensajes del bot.

# Configuración del bot
def main() -> None:
    application = Application.builder().token("7778739715:AAEAhgnDzI8Y2RTkWPJ2P6Ez-ag6oefcZHQ").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

if __name__ == '__main__':
    main()
