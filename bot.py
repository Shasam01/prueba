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

   updater = Updater(token=os.environ['1966570588:AAG5HiKbmieozaH9LnNDL-6h4F_wVUqg-I8'], use_context=True)

   dp = updater.dispatcher
   dp.add_handler(MessageHandler(filter=Filters.text, callback=process_message)  
   updater.start_polling()

   updater.idle()
