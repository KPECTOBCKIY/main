import telebot;
bot = telebot.TeleBot('6648964856:AAEl3d48O2kL71dxEpFrK8CAgL2Oy9kLkoY');

#методы получения текста
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

@bot.message_handler(content_types=['text', 'document', 'audio'])

if message.text == "Привет":
    bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
elif message.text == "/help":
    bot.send_message(message.from_user.id, "Напиши привет")
else:
    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
