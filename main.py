from telebot import TeleBot

bot = TeleBot('8069948743:AAG1F292prbQrNO-M-FCE0sQBnsd54654YU')


@bot.message_handler(commands=['start'])
def top(message):
    bot.send_message(message.chat.id, 'Умскул, вам на работу олимпиадник не нужен по математике и физике? Призёр Росатома по математике за 11 класс, Газпрома по физике (3 уровень в перечне был за 11 класс), инженерной олимпиады')


bot.infinity_polling()