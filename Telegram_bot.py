from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

#Bot token
TOKEN = "My Telegram bot token goes here"

#Function for the command /start
async def start(update: Update, context):
    await update.message.reply_text("Hi!, im a test Bot. Type /help to see what i can do.")

#Help Menu
async def help(update: Update, context):
    Help_menu = (
        "🚀 **Available Commands:**\n"
        "/start - starts the bot and receives a welcome message.\n"
        "/help - Shows this command list.\n"
        "\n✨Send me any message and i will reply automaticly!."
    )
    await update.message.reply_text(Help_menu)

#Function to control the text messages 
async def handle_message(update: Update, context):
    user_message = update.message.text
    await update.message.reply_text(f"Message received: {user_message}")

#Bot setting
def main():
    #Create aplication for the bot
    app = ApplicationBuilder().token(TOKEN).build()

    #Add command and messages drivers
    app.add_handler(CommandHandler("start", start))  #/Start command
    app.add_handler(CommandHandler("help", help))    #/Help command
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  #Normal messages

    #Initialize bot
    print("Bot working...")
    app.run_polling()

if __name__ == "__main__":
    main()
