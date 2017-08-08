# coding=utf-8

import telebot
import base64
import shell
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands='execute', func=lambda message: message.chat.type == "private")
def send_command_result(message):
    if message.from_user.id in config.admins:
        bot.send_message(message.chat.id, "```\n" + shell.execute_one_line(shell.split_command(message.text)) + "\n```",
                         parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "Error: Permission denied.")


@bot.message_handler(commands='su_execute', func=lambda message: message.chat.type == "private")
def send_su_command_result(message):
    if message.from_user.id in config.admins:
        try:
            pwfile = open(config.password_file, "r")
            pwfile_content = pwfile.read()
            if pwfile_content is None or pwfile_content != "":
                pw = base64.urlsafe_b64decode(pwfile_content)[:-1]
                bot.send_message(message.chat.id, "```\n" + shell.execute_sudo(
                    shell.split_command(message.text), pw) + "\n```", parse_mode="Markdown")
        except Exception as e:
            bot.send_message(message.chat.id, e)
    else:
        bot.send_message(message.chat.id, "Error: Permission denied.")


@bot.message_handler(commands='set_password', func=lambda message: message.chat.type == "private")
def set_password(message):
    pwfile = open(config.password_file, "w")
    pwfile.write(base64.urlsafe_b64encode(shell.split_command(message.text)))
    pwfile.close()


bot.polling()
