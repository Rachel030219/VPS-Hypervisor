# coding=utf-8

import telebot
import shell
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands='execute', func=lambda message: message.chat.type == "private")
def send_command(message):
    if message.from_user.id in config.admins:
        bot.send_message(message.chat.id, "```\n" + shell.execute_one_line(message.text) + "\n```",
                         parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "Error: Permission denied.")


bot.polling()
