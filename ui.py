import telebot
from telebot import types
import constants
import requests
import time


API_TOKEN = constants.API_LENTA
bot = telebot.TeleBot(API_TOKEN)
'''
current_rudnik = ''
def r_t():
    global current_rudnik
    current_rudnik = 'r_t'


def r_o():
    global current_rudnik
    current_rudnik = 'r_o'


def r_k():
    global current_rudnik
    current_rudnik = 'r_k'


def r_s_s():
    global current_rudnik
    current_rudnik = 'r_s_s'

def zapasy(name_of_rudnik):
    print(name_of_rudnik)
    image = open('IMAGES/' + name_of_rudnik + '.png')
    return image
'''

# /start command handler; send start-message to the user
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, constants.TELEGRAM_START_MSG, parse_mode='HTML')


@bot.message_handler(content_types=['location'])
def send_message(message):
    bot.send_message(message.chat.id, 'Ближайший магазин находится по адресу: проспект Будённого, 18Б')
    bot.send_location(message.chat.id, 55.767366, 37.729100)


# /help command handler; send hello-message to the user
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        constants.HELP_MSG,
        parse_mode='HTML',
        reply_markup=constants.HELP_KEYBOARD,
        disable_web_page_preview=True)


@bot.message_handler(commands=['promo'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        constants.PROMO,
        parse_mode='HTML'
    )
'''
@bot.message_handler(commands=['secretsanta'])
def send_welcome(message):
    (name_of_guy, name_of_girl) = get_the_name(message.text)
    bot.send_message(message.chat.id, 'Твоя пара — это {}'.format(name_of_girl))
'''

'''
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'r_taymyr':
            bot.edit_message_text(
                constants.RUDNIK_DESC[0] + constants.RUDNIK_PLUS,
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                parse_mode='HTML',
                reply_markup=constants.RUDNIK_ADDITIONAL_INFO)
            r_t()

        if call.data == 'r_oktyabyrjskij':
            bot.edit_message_text(
                constants.RUDNIK_DESC[1] + constants.RUDNIK_PLUS,
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                parse_mode='HTML',
                reply_markup=constants.RUDNIK_ADDITIONAL_INFO)
            r_k()

        if call.data == 'r_komsomoljskij':
            bot.edit_message_text(
                constants.RUDNIK_DESC[2] + constants.RUDNIK_PLUS,
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                parse_mode='HTML',
                reply_markup=constants.RUDNIK_ADDITIONAL_INFO)
            r_k()

        if call.data == 'r_shakhta_skalistaja':
            bot.edit_message_text(
                constants.RUDNIK_DESC[3] + constants.RUDNIK_PLUS,
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                parse_mode='HTML',
                reply_markup=constants.SHAKHTA_INFO)
            r_s_s()

        if call.data == 'zapasy':
            bot.send_photo(call.message.chat.id, open('IMAGES/' + current_rudnik + '.png', 'rb'))

        if call.data == 'zatraty':
            if current_rudnik == 'r_t':
                bot.send_message(call.message.chat.id,
                                 'Капитальные затраты составили ' + constants.RUDNIK_ZATRATY[0] + 'млн долл.')
            if current_rudnik == 'r_o':
                bot.send_message(call.message.chat.id,
                                 'Капитальные затраты составили ' + constants.RUDNIK_ZATRATY[1] + 'млн долл.')
            if current_rudnik == 'r_k':
                bot.send_message(call.message.chat.id,
                                 'Капитальные затраты составили ' + constants.RUDNIK_ZATRATY[2] + 'млн долл.')
            else: pass

        if call.data == 'finito':
            if current_rudnik == 'r_t':
                bot.send_message(call.message.chat.id, constants.RUDNIK_FINISHED_IN_2015[0])
            if current_rudnik == 'r_o':
                bot.send_message(call.message.chat.id, constants.RUDNIK_FINISHED_IN_2015[1])
            if current_rudnik == 'r_k':
                bot.send_message(call.message.chat.id, constants.RUDNIK_FINISHED_IN_2015[2])

        if call.data == 'realization':
            bot.send_message(call.message.chat.id, constants.REAL)
        if call.data == 'works':
            bot.send_message(call.message.chat.id, constants.WORKS)

'''
# polling cycle
if __name__ == '__main__':
    while True:
        print('?/?')
        try:
            bot.polling(none_stop=True)
        except requests.exceptions.ConnectionError as e:
            print('There was requests.exceptions.ConnectionError')
            time.sleep(15)
