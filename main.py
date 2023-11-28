import telebot

bot = telebot.TeleBot('6390433636:AAGY8cMeFNcKTksdRBgGZR2Tljaa7R35Olg')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     'Привет! Рад, что ты заглянул! \nЕсли хочешь получить комплимент - напиши команду /compliment, настроиться на позитив - /positive, замотивироваться - /motivation')


@bot.message_handler(commands=['motivation'])
def main(message):
    bot.send_message(message.chat.id,
                     'У тебя всё получится, главное - не сдаваться! Помни: дорогу освоит идущий! Я верю в тебя!',
                     parse_mode='Markdown')


@bot.message_handler(commands=['compliment'])
def main(message):
    bot.send_message(message.chat.id, 'Ты большой молодец и делаешь достаточно!', parse_mode='Markdown')


@bot.message_handler(commands=['positive'])
def main(message):
    bot.send_message(message.chat.id, 'Ты сегодня хорошо поработал!', parse_mode='Markdown')


bot.infinity_polling()