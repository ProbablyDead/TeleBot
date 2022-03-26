import telebot
import sqlite3
from sqlite3 import Error

####################################################################### FUNCTIONS
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        # print("Connection to SQLite DB successful")
    except Error:
        print(f"The error '{Error}' occurred")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        # print("Query executed successfully")
    except Error:
        print(f"The error '{Error}' occurred")

####################################################################### VARIABLES
chats = []
bot = telebot.TeleBot("5221893562:AAHl63BKeIWYOOdBti1AlXPsfrNKr1NGIs8")
database = create_connection("tele.sqlite")

####################################################################### DATABASE

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL
);
"""

execute_query(database, create_users_table)

####################################################################### BOT INSTRUCTIONS
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello, it's a <b>News Feed</b> bot", parse_mode="html")


@bot.message_handler(commands=["push"])
def push_text(message):
    chats.append(message.text.replace("/push ", " "))


@bot.message_handler(commands=["show"])
def show(message):
    if len(chats) == 0:
        bot.send_message(message.chat.id, "array is empty")
    else:
        for i in chats:
            bot.send_message(message.chat.id, i)


# @bot.message_handler(commands=["forward"])
# def forward(message):
#     chatID = message.text.replace("/forward ", "")
#     bot.forward_message(chatID, message.chat.id, message.message_id)

bot.polling(none_stop=True)
