import os
from telegram.ext import Updater, MessageHandler, Filters

def process_message(update.context):
    
    print(update)
    text = update.message.text

    if str(text).__contains__('#aporte'):
        context.bot.send_message(
            chat_id=@SantuaryRetroGameS3
            text=str(text).replace('#aporte', ' ') 

         )

    


if __name__== '__main__':

   updater = Updater(token=os.environ['Your_Token'], use_context=True)

   dp = updater.dispatcher
   dp.add_handler(MessageHandler(filter=Filters.text, callback=process_message)  
   updater.start_polling()

   updater.idle()
