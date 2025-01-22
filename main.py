import google.generativeai as genai
import telebot

# Configure your Gemini API key
API_KEY = "AIzaSyAR1W8my5ETltKpwwZrld0zxF53VNYRsVo"
genai.configure(api_key=API_KEY)

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro')

# Telegram Bot Token
TELEGRAM_TOKEN = "7592033135:AAHl6LQ_M3r4LiZqrihPtpyfgt5bjYgphPk"

# Initialize the bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Command to start the bot
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Chatbot initialized! Start your conversation below. Type /exit to end the chat.")

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text

    if user_input == "/exit":
        bot.reply_to(message, "Chat ended. Goodbye!")
        return

    try:
        chat = model.start_chat()
        response = chat.send_message(user_input)
        bot.reply_to(message, f"Chatbot: {response.text}")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")

# Start the bot
if __name__ == "__main__":
    print("Starting bot...")
    bot.polling()
