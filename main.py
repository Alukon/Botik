import telebot # Создаем экземпляр бота
import  random
bot = telebot.TeleBot('5599447629:AAF9jE_ELt7PrMRM0kj4uShgK2i7DlSJFd0')
@bot.message_handler(commands=["start"]) # Функция, обрабатывающая команду /start
def start(m, res=False):
    bot.send_message(m.chat.id, 'Бот тут. Напишите мне что-нибудь )')
@bot.message_handler(content_types=["text"]) # Получение сообщений от юзера
def handle_text(message):
    bot.send_message(message.chat.id, 'Ваше сообщение: ' + message.text)
print ('Бот запущен')
bot.polling(none_stop=True, interval=0) # Запускаем бота
# контроль изменений
print(2+2)
print(3+3)