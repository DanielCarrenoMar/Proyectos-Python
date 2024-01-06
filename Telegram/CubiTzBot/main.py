from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from keys import CubiTz, Grupos
import asyncio

token = CubiTz.get("token")

animacion = [
    """
    [░░░░]
    """,
    """
    [▓░░░]
    """,
    """
    [█▓░░]
    """,
    """
    [██▓░]
    """,
    """
    [███▓]
    """,
    """
    [████]
    """,
    """
    ⢿⣿⣿⣿⣭⠹⠛⠛⠛⢿⣿⣿⣿⣿⡿⣿⠷⠶⠿⢻⣿⣛⣦⣙⠻⣿
    ⣿⣿⢿⣿⠏⠀⠀⡀⠀⠈⣿⢛⣽⣜⠯⣽⠀⠀⠀⠀⠙⢿⣷⣻⡀⢿
    ⠐⠛⢿⣾⣖⣤⡀⠀⢀⡰⠿⢷⣶⣿⡇⠻⣖⣒⣒⣶⣿⣿⡟⢙⣶⣮
    ⣤⠀⠀⠛⠻⠗⠿⠿⣯⡆⣿⣛⣿⡿⠿⠮⡶⠼⠟⠙⠊⠁⠀⠸⢣⣿
    ⣿⣷⡀⠀⠀⠀⠀⠠⠭⣍⡉⢩⣥⡤⠥⣤⡶⣒⠀⠀⠀⠀⠀⢰⣿⣿
    ⣿⣿⡽⡄⠀⠀⠀⢿⣿⣆⣿⣧⢡⣾⣿⡇⣾⣿⡇⠀⠀⠀⠀⣿⡇⠃
    ⣿⣿⣷⣻⣆⢄⠀⠈⠉⠉⠛⠛⠘⠛⠛⠛⠙⠛⠁⠀⠀⠀⠀⣿⡇⢸
    ⢞⣿⣿⣷⣝⣷⣝⠦⡀⠀⠀⠀⠀⠀⠀⠀⡀⢀⠀⠀⠀⠀⠀⠛⣿⠈
    ⣦⡑⠛⣟⢿⡿⣿⣷⣝⢧⡀⠀⠀⣶⣸⡇⣿⢸⣧⠀⠀⠀⠀⢸⡿⡆
    ⣿⣿⣷⣮⣭⣍⡛⠻⢿⣷⠿⣶⣶⣬⣬⣁⣉⣀⣀⣁⡤⢴⣺⣾⣽⡇
    """
]

async def start(update: Update, context: ContextTypes):
    await update.message.reply_text(f'Hola {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes):
    await update.message.reply_text("Ayuda")

async def custom(update: Update, context: ContextTypes):
    await update.message.reply_text(f'- {update.message.text}')

async def pantalla(update: Update, context: ContextTypes):
    message = await context.bot.send_message(update.message.chat.id, animacion[0])

    for i in range(len(animacion)-1):
        await asyncio.sleep(1)
        await context.bot.edit_message_text(chat_id=update.message.chat.id,
                                                message_id=message.message_id,
                                                text=animacion[i+1])
        
async def basadoMaker(update: Update, context: ContextTypes):
    pass

async def error(update: Update, context: ContextTypes):
    print(f"Update {update.message.chat.first_name} caused error {context.error}")
    update.message.chat.set_

#MAIN
    
if __name__ == "__main__":
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("custom", custom))
    app.add_handler(CommandHandler("pantalla", pantalla))

    app.add_handler(MessageHandler(filters.TEXT, basadoMaker))

    #app.add_error_handler(error)

    print("Iniciado")
    app.run_polling(poll_interval=1, timeout=10)