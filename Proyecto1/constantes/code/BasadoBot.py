import telebot
API = "1907330659:AAHX38zXIaVMBJu_h3sAqgOqEHqDQmnBrDc"

"""print("1) El grupo B) \n2) Cocacola otra vez me mori \n3) Terraria Plus")
grupo = input("eligue: ")
if grupo == "1":
	ChatID = -1001429027887
if grupo == '2':
	ChatID = -952941676
if grupo == "3":
	ChatID = -1001229819580"""
ChatID = -1001229819580
print(ChatID)
bot = telebot.TeleBot(API)

# Empezar
"""@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.reply_to(message, "hola")"""
# Responder Mensajes
"""@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    if message.text == "que":
        bot.send_message(message.chat.id, "so")"""
"""@bot.message_handler(func=lambda x: True)"""

# responder manuela
while False:
	mensaje = input("escribe: ")
	bot.send_message(ChatID, mensaje)


# Leer todos los mensajes
@bot.message_handler(content_types=["text"])
def echo_all(m):
	# Mandar stiker -- bot.send_sticker(ChatID, "https://img-09.stickers.cloud/packs/8a5e124e-3e43-44a5-bb7d-68642505a153/webp/5e5d12f6-4ceb-45f2-911d-67fbb40d0eaa.webp")
	print(m.from_user.first_name, ":", m.text)
	print("Desde:", m.chat.title)
	print("MensajeID:", m.message_id)


	if m.text.endswith("que") | m.text.endswith("Que"):
		bot.reply_to(m, "so")

	if m.text.endswith("rra") | m.text.endswith("Rra"):
		bot.reply_to(m, "eres")

	if m.chat.type == "private":
		if m.text.startswith("https://"):
			bot.send_photo(ChatID, m.text)
		else:
			bot.send_message(ChatID, m.text)

# Inicio y final del bot
if __name__ == "__main__":
	print("iniciando el bot")
	bot.infinity_polling()
	print("fin")