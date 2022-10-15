from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *




app = ApplicationBuilder().token("TOKEN").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
print('start server')
app.run_polling()