from telebot import types
import telebot

token= '6469988581:AAEc5LKxs0hy9ttda0iarqq-uJSmaqQXzKc'

my_chat_id=5574738971

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])

def start_message(message):

    keyboard = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)

    button1 = types.KeyboardButton(text="Услуги")

    button2= types.KeyboardButton(text="О нас")

    button3= types.KeyboardButton(text="Оставить заявку")

   

    

    keyboard.add(button1, button2,button3,)

    bot.send_message(message.chat.id, 'Приветствуем!Мы IT компания!Добро пожаловать', reply_markup=keyboard)
    

def info_func(message):

    keyboard = types.InlineKeyboardMarkup()

    url_button = types.InlineKeyboardButton(text="Ссылка на сайт", url="https://www.youtube.com/channel/UCpqvgYdwkVS8RvbtLl2VVqQ")

    keyboard.add(url_button)

    bot.send_message(message.chat.id, "Информация о компании", reply_markup=keyboard)


def send_requests(message):

    message=f'Новая заявка:{message.text}'

    bot.send_message(my_chat.id,message.mes)

    bot.send_message(message.chat.id, 'Спасибо за заявку!Наши специалисты скоро с вами свяжутся!')

def send_servive(message):
    bot.send_message(message.chat.id, '1.Составить годовой отчет')
    bot.send_message(message.chat.id, '2.Оплатить налоги за ТОО')
    bot.send_message(message.chat.id, '3.Расчитать бюджет')

def jls_extract_def(send_request):
    return send_request


@bot.message_handler(content_types=['text'])

def repeat_all_messages(message):

    if message.text.lower() == 'о нас':

        info_func(message)

    if message.text.lower() == 'оставить заявку':

        bot.send_message(message.chat.id, 'Будем рады вас обслужить! Оставьте свои контактные данные.')

        bot.register_next_step_handler(message,send_request)
    if message.text.lower() =='услуги':
        send_servive(message)





if __name__ == '__main__':
    
    
 bot.infinity_polling()




