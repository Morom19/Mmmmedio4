from flask import Flask, request, jsonify
   import google.generativeai as genai
   from telegram import Update, Bot
   from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

   app = Flask(__name__)

   # Configure your Gemini API key
   API_KEY = "AIzaSyAR1W8my5ETltKpwwZrld0zxF53VNYRsVo"
   genai.configure(api_key=API_KEY)

   # Initialize the Telegram Bot
   TELEGRAM_TOKEN = "7592033135:AAHl6LQ_M3r4LiZqrihPtpyfgt5bjYgphPk"
   bot = Bot(token=TELEGRAM_TOKEN)
   dispatcher = Dispatcher(bot, None, workers=0)

   # Initialize the generative model
   model = genai.GenerativeModel('gemini-pro')

   def start(update, context):
       update.message.reply_text('Welcome! Send me a message and I will respond.')

   def handle_message(update, context):
       user_input = update.message.text
       chat = model.start_chat()
       try:
           response = chat.send_message(user_input)
           update.message.reply_text(response.text)
       except Exception as e:
           update.message.reply_text(f"An error occurred: {e}")

   # Set up command and message handlers
   dispatcher.add_handler(CommandHandler("start", start))
   dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

   @app.route('/webhook', methods=['POST'])
   def webhook():
       update = Update.de_json(request.get_json(force=True), bot)
       dispatcher.process_update(update)
       return 'ok'

   if __name__ == "__main__":
       app.run(port=5000)
