import telebot
bot = telebot.TeleBot("6996267147:AAHg_GxoFX3XFyJiBBZTBqdIuE8vppS8ERM")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Что тебя беспокоит? ")
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.lower() == "голова":
        recommendations = "От головной боли рекомендуется:\n"\
                          "- Парацетамол\n"\
                          "- Цитрамон\n"\
                          "- Спазмалгон\n"\
                          "- Некст\n"\
                          "- Темпалгин\n"\
                          "- Нурофен"
        bot.send_message(message.chat.id, recommendations)
    elif message.text.lower() == "живот":
        recommendations = "От боли в животе рекомендуется:\n"\
                          "- Но-Шпа\n"\
                          "- Дюспаталин\n"\
                          "- Смекта\n"\
                          "- Мезим\n"\
                          "- Иберогаст\n"\
                          "- Ренни"
        bot.send_message(message.chat.id, recommendations)

    elif message.text.lower() == "горло":
        recommendations = "От боли в горле рекомендуется: \n"\
                                                "- Анти-Ангин формула\n"\
                                                "- Гексализ\n"\
                                                "- Гексорал\n"\
                                                "- Гомеовокс\n"\
                                                "- Граммидин"
        bot.send_message(message.chat.id, recommendations)
    elif message.text.lower() == "температура":
        recommendations = "От температуры рекомендуется: \n"\
                                                 "- Римантадин\n"\
                                                 "- Кагоцел\n"\
                                                 "- Анаферон\n"\
                                                 "- Циклоферон\n"\
                                                 "- Анаферон\n"\
                                                 "- Антигриппин\n"\
                                                 "- Агри\n"\
                                                 "- Цитовир-3"
        bot.send_message(message.chat.id, recommendations)
    elif message.text.lower() == "аллергия":
        recommendations = "От аллергии рекомендуется: \n"\
                                                 "- Авамис\n"\
                                                 "- Виброцил\n"\
                                                 "- Дезринит\n"\
                                                 "- Момат\n"\
                                                 "- Мометазон\n"\
                                                 "- Назаваль\n"\
                                                 "- Назарел\n"\
                                                 "- Назонекс"
        bot.send_message(message.chat.id, recommendations)
    elif message.text.lower() == "насморк":
        recommendations = "От насморка рекомендуется: \n"\
                                                 "- Омнитус\n"\
                                                 "- Панатус форте"
        bot.send_message(message.chat.id, recommendations)
    elif message.text.lower() == "кашель":
        recommendations ="От кашля рекомендуется: \n"\
                                                 "- Гербион\n"\
                                                 "- Флюдитек\n"\
                                                 "- Геделикс\n"\
                                                 "- Коделак Нео\n"\
                                                 "- Панатус форте"
        bot.send_message(message.chat.id, recommendations)
    elif message.text.lower() =="спасибо":
        bot.send_message(message.chat.id, "Пожалуйста! Выздоравливай!")
    else:
        recommendations = "Извини, мы не можем предложить таблетки для указанной боли"
        bot.send_message(message.chat.id, recommendations)
    if message.text.lower() == "stop":
        bot.send_message(message.chat.id, "Пока!")
bot.polling(none_stop=True)


