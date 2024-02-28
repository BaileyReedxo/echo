import telebot
import time

TOKEN = '6867200323:AAFSKQcYhJmBiDW8cq5foJajmpyrAXbj790'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Ignore messages inside parentheses
    if "(" in message.text and ")" in message.text:
        return

    # Print the message type for debugging
    print(f"Received message type: {message.content_type}")

    # Echo back text messages
    if message.text:
        # Introduce a delay of 15 seconds
        time.sleep(6)
        bot.send_message(message.chat.id, message.text)

    # Echo back images
    elif message.photo:
        file_id = message.photo[-1].file_id
        # Introduce a delay of 15 seconds
        time.sleep(5)
        bot.send_photo(message.chat.id, file_id)

    # Echo back stickers
    elif message.sticker:
        # Introduce a delay of 15 seconds
        time.sleep(5)
        bot.send_sticker(message.chat.id, message.sticker.file_id)

# Handle media content in edited messages as well
@bot.edited_message_handler(func=lambda message: True)
def echo_edited(message):
    # Handle edited messages in the same way as regular messages
    echo_all(message)

if __name__ == "__main__":
    bot.polling(none_stop=True)
