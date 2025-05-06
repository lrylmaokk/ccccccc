import telebot
import os
from datetime import datetime

TOKEN = '7010771282:AAHteXmjb7rVGW_x3DqaV9F9GPsg3y_fqj8'
ADMIN_IDS = ["6320839835"]
bot = telebot.TeleBot(TOKEN)

def is_admin(message):
    return str(message.chat.id) in ADMIN_IDS

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, (
        "<b><i>🐳 Zmap Proxy Premium New Version</i></b>\n\n"
        "<b>🇻🇳 Vietnamses Premium Proxy Commands</b>\n"
        " ➥ '<b>/scanvn</b>' • Get scan proxy Vietnam\n"
        " ➥ '<b>/stopvn</b>' • Stop scan Vietnam proxy\n"
        " ➥ '<b>/countvn</b>' • Check count proxy Vietnamses\n"
        " ➥ '<b>/extravn</b>' • Download list Vietnam proxy"
    ), parse_mode="HTML")

@bot.message_handler(commands=['scanvn', 'stopvn', 'countvn', 'extravn', 'scanmix', 'stopmix', 'countmix', 'extramix'])
def handle_command(message):
    command = message.text[1:]
    if not is_admin(message):
        bot.reply_to(message, "<blockquote><b>You are not allowed! Contact <u>@tcplegit</u></b></blockquote>", parse_mode="HTML")
        return

    if command == 'scanvn':
        if os.path.exists("all_temp.txt"): os.remove("all_temp.txt")
        os.system("screen python3 vn.py")
        bot.reply_to(message, "<blockquote><b>⚡Started⚡ Scan Vietnams proxies!</b></blockquote>", parse_mode="HTML")
    elif command == 'stopvn':
        os.system("pkill -f 'python3 vn.py'")
        bot.reply_to(message, "<blockquote><b>⚡Stopped⚡️ Vietnams proxy scanner.</b></blockquote>", parse_mode="HTML")
    elif command == 'countvn':
        if os.path.exists("all_temp.txt"):
            with open("all_temp.txt", "r") as f:
                total = sum(1 for _ in f)
            bot.reply_to(message, f"<blockquote><b>🌩 Total Vietnams proxies:</b> <code>{total}</code></blockquote>", parse_mode="HTML")
        else:
            bot.send_message(message.chat.id, "<blockquote><b>🌩 No Vietnams proxies found.</b></blockquote>", parse_mode="HTML")
    elif command == 'extravn':
        if os.path.exists("all_temp.txt"):
            filename = f"Vietnams {datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            os.rename("all_temp.txt", filename)
            with open(filename, "r") as f:
                count = sum(1 for _ in f)
            bot.send_document(message.chat.id, open(filename, "rb"), caption=f"<blockquote><b>Premium Vietnamses Proxies</b>\n<b>Total:</b> '<u>{count}</u>' <b>proxies</b></blockquote>", parse_mode="HTML")
            os.remove(filename)

bot.polling()