from pyrogram import Client, filters

# Строки ниже не трогать
# Do not touch the lines below

api_id = 22817128
api_hash = '1979e639ba3b720fefe9af4499fbd15f'

# Строки выше не трогать
# Do not touch the lines above

# Выбор языка
# Language selection

language = 'en'
choice = str(input("Выберите язык/Select a language (ru/en):"))
if choice == 'ru':
    language = 'ru'

user = 'user' # Назовите своего пользователя \ Name your user
if user == 'user':
    if language == 'ru':
        input = str(input("Как вас зовут? (это необходимо чтобы различать аккаунты)"))
        if input == '':
            user = 'user'
        else:
            user = input
    else:
        input = str(input("What is your name? (this is necessary to distinguish between accounts)"))
        if input == '':
            user = 'user'
        else:
            user = input

client = Client(user, api_id, api_hash)

client.start()
client.stop()

if language == 'ru':
    print("Бот запущен")
else:
    print('Bot started')

@client.on_message(filters.command("send") & filters.me)
def send_handler(client, message):
    # Разбиение аргументов команды
    command = message.text.split(" ")
    message.delete()  

    if len(command) < 3:
        if language == 'ru':
            message.reply_text("Неверный формат команды! Используйте: /send <количество> <сообщение>")
        else:
            message.reply_text("Invalid command format! Use: /send <quantity> <message>")
        return

    try:
        count = int(command[1])
        text = " ".join(command[2:])

        for _ in range(count):
            client.send_message(message.chat.id, text)

        

    except ValueError:
        if language == 'ru':
            message.reply_text("Incorrect number of messages!")
        else:
            message.reply_text()

    except Exception as e:
        if language == 'ru':
            message.reply_text(f"Произошла ошибка: \n{str(e)}")
        else:
            message.reply_text(f"An error occurred: \n{str(e)}")

client.run()