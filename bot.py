import telebot
TOKEN = ''
bot = telebot.TeleBot(TOKEN)
number = 0


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Insert operation")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == '/square':
        bot.send_message(message.from_user.id, 'Enter number')
        bot.register_next_step_handler(message, square_number)
    else:
        num1 = ''
        num2 = ''
        for i in message.text:
            if i in ['+']:
                for i in message.text:
                    if i == '+':
                        break
                    else:
                        num1 += i
                for i in message.text[::-1]:
                    if i == '+':
                        break
                    else:
                        num2 += i
                res = int(num1) + int(num2[::-1])
                bot.reply_to(message, str(res))
            elif i in ['-']:
                for i in message.text:
                    if i == '-':
                        break
                    else:
                        num1 += i
                for i in message.text[::-1]:
                    if i == '-':
                        break
                    else:
                        num2 += i
                res = int(num1) - int(num2[::-1])
                bot.reply_to(message, str(res))
            elif i in ['*']:
                for i in message.text:
                    if i == '*':
                        break
                    else:
                        num1 += i
                for i in message.text[::-1]:
                    if i == '*':
                        break
                    else:
                        num2 += i
                res = int(num1) * int(num2[::-1])
                bot.reply_to(message, str(res))


def square_number(message):
    global number
    number = int(message.text)**2
    bot.send_message(message.from_user.id, str(number))


bot.polling()
