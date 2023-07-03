import logging
from telegram import Update
from telegram import Updater, CommandHandler, MessageHandler, CallbackContext, MessageFilter
import openai

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на ваш собственный API ключ от BotFather
TELEGRAM_BOT_TOKEN = '6167500256:AAF_nDdGlgQQb1nZq2QT1Ut84bL4INICAXk'

# Замените 'YOUR_OPENAI_API_KEY' на ваш собственный ключ API от OpenAI
OPENAI_API_KEY = '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'

# Инициализация библиотеки OpenAI с использованием вашего ключа API
openai.api_key = OPENAI_API_KEY

# Настройка логгирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Обработчик команды /start
def start(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот, построенный на GPT-3 модели. Чем я могу помочь?')

# Обработчик текстовых сообщений
def respond_to_message(update: Update, _: CallbackContext) -> None:
    user_input = update.message.text

    # Здесь мы используем GPT-3 для получения ответа на сообщение пользователя
    response = generate_gpt3_response(user_input)

    update.message.reply_text(response)

# Функция для использования GPT-3 для генерации ответа
def generate_gpt3_response(user_input: str) -> str:
    # Здесь вы можете настроить параметры для GPT-3, если хотите
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=150,
        temperature=0.7,
        n=1,
        stop=None,
    )

    return response.choices[0].text.strip()

def main() -> None:
    # Инициализация Updater с вашим API токеном бота
    updater = Updater(TELEGRAM_BOT_TOKEN)

    # Получение диспетчера для регистрации обработчиков команд и сообщений
    dispatcher = updater.dispatcher

    # Регистрация обработчиков
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(MessageFilter.text & ~MessageFilter.command, respond_to_message))

    # Запуск бота
    updater.start_polling()

    # Запуск обработчика до принятия сигнала остановки
    updater.idle()

if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()
