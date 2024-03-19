from typing import Final
from telegram import *
from telegram.ext import *

TOKEN: Final = 'YOUR TOKEN' # INTRODUCE HERE YOUR BOTS TOKEN
BOT_USERNAME: Final = '@ BOT ' # INTRODUCE HERE YOUR BOTS @

# COMMANDS
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Start command message')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Help command message')

# RESPONSES

def handle_response(text: str) -> str:

    processed: str = text.lower()
    if 'how are you' in processed:
        return 'I\'m fine, thanks!'
    
    if 'hello' in processed:
        return 'Hi! Nice to see you'
    
    if 'bye' in processed:
        return 'Good bye!'
    
    return 'I didn\'t catch that'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group' :
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    
    print('Bot: ',response)
    await update.message.reply_text(response)

# Error handleing

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

# MAIN

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)
    
    print('Polling...')
    app.run_polling(poll_interval=5) # changing the poll_interval will change the seconds the bot checks for new messages
    # With this poll_interval it checkes every 5 seconds