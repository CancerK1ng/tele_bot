import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/2193800188773011180.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("roll")
    item2 = types.KeyboardButton("Как дела?")
    item3 = types.KeyboardButton("Часто задоваемый вопрос")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Доброе утро хозяин, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный, чтобы ты не был одиноким'.format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'roll':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == 'Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Чувствую себя отлично, а Вы?', reply_markup=markup)

        elif message.text == 'Часто задоваемый вопрос':

            markup1 = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Яна_цист", callback_data='beka')
            item2 = types.InlineKeyboardButton("Daka", callback_data='daka')
            markup1.add(item1, item2)
            bot.send_message(message.chat.id, 'Кто из них плово играет:', reply_markup=markup1)


        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить(')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
            elif call.data == 'beka':
                bot.send_message(call.message.chat.id, 'Правильно)')
            elif call.data == 'daka':
                bot.send_message(call.message.chat.id, 'Правильно)')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Кто из них плово играет:",
                                  reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="Test")

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
