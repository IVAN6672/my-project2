import telebot
import random
token = ('AAGJ9ZS1gTk1cQeDbxfEPXt4-SBhvgWr8wA')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот про глобальное потепление. Напиши /causes чтобы узнать причины потепления. Напиши /solutions чтобы узнать, как его сдерживать и /meme чтоб посмотреть мемы")



@bot.message_handler(commands=['causes'])
def send_welcome(message):
    bot.reply_to(message, "Причины глобального потепления: 1. Сжигание топлива (уголь, нефть, газ) → CO₂. 2. Вырубка лесов → меньше поглощается CO₂. 3. Животноводство → метан от коров. 4. Промышленность и транспорт → выбросы газов.")



@bot.message_handler(commands=['solutions'])
def send_welcome(message):
    bot.reply_to(message, "Сдерживать солнечное потепление (глобальное потепление) можно, сочетая законодательные меры, использование технологий и изменение образа жизни. Учёные предлагают идеи, которые призваны «блокировать» солнечное излучение и снизить его негативное воздействие на климат Земли, но солнечная геоинженерия не является решением проблемы. Она не устраняет причину потепления — избыточное содержание углекислого газа в атмосфере.")


pogoda = random.choise
