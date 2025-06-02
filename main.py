import telebot

bot = telebot.TeleBot('7881078626:AAHuP_YpbTtnRiNhPPL_xM9iNgmvrwslJ1M')

@bot.message_handler(commands=['start', 'help'])
def send_welkome(message):
    bot.reply_to(message,'kak dela?')

@bot.message_handler(commands=['exit'])
def send_welkome(message):
    bot.reply_to(message,'paka')

@bot.message_handler(commands=['fun'])
def send_welcome(message): 
    for i in range(100): bot.send_message(message.chat.id,')')
                                                                                                        
bot.infinity_polling()