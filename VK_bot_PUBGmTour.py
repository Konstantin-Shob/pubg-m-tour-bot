import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

# API токен сообщества
mytoken = '038431fe77065c3bba87a7c9577d2aa7c4d2586eb401660d3115dbe8323b161fbbe2ed01adf293fff7dd1'

msg_help = """
• Вы можете в любой момент воспользоваться командами, указанными в меню, команды можно писать с заглавной и прописной буквой, с кавычками и без них. 

• В любой момент вы можете воспользоваться кнопкам, они упростят работу с ботом

• Вместо команд вы можете использовать индексы указанные после команд в [ ] ( например [1] - 1 )

• Если вы хотите связаться с администрацией - просто напишите сообщение, если оно не совпадает с какой либо из команд, то бот его проигнорирует, а администратор ответит как только сможет.

Для вызова меню используйте команду "Меню"
"""
msg_menu = """
Команды:

• Турниры [1]
• Рассылка [2]
• Помощь [3]
• Отзывы [4]
• Правила [5]
• Оставить предложение по улучшению группы [6]
"""
def menu_buttons(keyboard):
    keyboard.add_button('💰 Турниры 💰', color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_openlink_button('📬 Рассылка 📬', link='https://vk.cc/c2taZ7')
    keyboard.add_line()
    keyboard.add_button('❔ Помощь ❔', color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_openlink_button('🤔 Отзывы 🤔', link='https://vk.cc/c2vnrz')
    keyboard.add_line()
    keyboard.add_openlink_button('❕ Правила ❕', link='https://vk.cc/c2tb12')
    keyboard.add_line()
    keyboard.add_openlink_button('🆙 Предложить улучшение 🆙', link='https://vk.cc/c2xTHw')
msg_tour = """
Какой турнир вас интересует?

• Платный турнир [7]
• Практические игры [8]
• Кастомка [9]

❔ Тип турнира указывается в посте о турнире, если вы оставляете заявку на не существующийтурнир, она аннулируется

❗️Если вы хотите зарегистрировать на турнир несколько человек, то вам необходимо:
• Оплатить участие за всех игроков
• В заявке на участие указать ники всех игроков
"""
def tour_button(keyboard):
    keyboard.add_button('🔫 Платный турнир 🔫', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('🔥 Практические игры 🔥', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('🎯 Кастомка 🎯', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('☰ Меню ☰', color=VkKeyboardColor.PRIMARY)
msg_prakt  = """
На данный момент практические игры не проводятся. Мы вернем данный тип матчей, как только вырастет активность на кастомках

Регламент практических игр: https://vk.cc/c6tSMu

Для участия в практических играх вы должны иметь команду, при отсутствии таковой вы можете принимать участие в кастомках
"""
# Для регистрации на практические игры вам необходимо заполнить заявку: https://vk.cc/c6Qx8y
#
# Перед регистрацией, просим вас ознакомиться с регламентом: https://vk.cc/c6tSMu
#
# Для участия в практических играх вы должны иметь команду, при отсутствии таковой вы можете принимать участие в кастомках
def prak_button(keyboad):
    # keyboard.add_openlink_button('Заполнить заявку', link='https://vk.cc/c6tSMu')
    # keyboard.add_line()
    keyboard.add_openlink_button('Регламент', link='https://vk.cc/c6tSMu')
    keyboard.add_line()
    keyboard.add_button('🎯 Кастомки 🎯', color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button('🔙 Назад 🔙 (Туринры)', color=VkKeyboardColor.NEGATIVE)
msg_custom = """
Кастомка - игра без приза с бесплатным входом. Регистрироваться на неё не нужно. Данные для входа в лобби приходят всем, кто подписан на рассылку "Кастомки": https://vk.cc/c2taZ7

В нашем сообществе проводятся призовые кастомки. Подробнееузнать о них вы можете сдесь: https://vk.cc/c8RP2a

Приятной игры 😉
"""
def custom_button(keyboard):
    keyboard.add_openlink_button('📬 Рассылка 📬', link='https://vk.cc/c6tSMu')
    keyboard.add_line()
    keyboard.add_openlink_button('Призовые кастомки', link='https://vk.cc/c8RP2a')
    keyboard.add_line()
    keyboard.add_button('🔙 Назад 🔙 (Туринры)', color=VkKeyboardColor.NEGATIVE)
msg_platn = """
Как вам удобнее оплатить участие?

• Сбербанк [10]
• Qiwi [11]
• ЮMoney (Яндекс деньги) [12]
• Tinkoff [13]
"""
def platn_button(keyboard):
    keyboard.add_button('Сбербанк', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Qiwi', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('ЮMoney', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Tinkoff', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('🔙 Назад 🔙 (Туринры)', color=VkKeyboardColor.NEGATIVE)
msg_sber = """
Вам необходимо:

1) Оплатить участие по номеру карты: 4276 5400 4913 8823

2) Заполнить заявку на участие: https://vk.cc/c7SULa

3) Прислать скриншот, подтверждающий оплату участия

После выполнения всех действий ожидайте ответа администратора
"""
def sber_button(keyboard):
    keyboard.add_openlink_button('Заполнить заявку', link='https://vk.cc/c7SULa')
    keyboard.add_line()
    keyboard.add_button('🔙 Назад 🔙 (Платный туринр)', color=VkKeyboardColor.NEGATIVE)
msg_qiwi = """
Вам необходимо:

1) Оплатить участие по ссылке: qiwi.com/p/79171071552 или по номеру телефона +79171071552

2) Заполнить заявку на участие: https://vk.cc/c7SULa

3) Прислать скриншот в ЛС сообщества, подтверждающий оплату участия 

После выполнения всех действий ожидайте ответа администратора
"""
def qiwi_button(keyboard):
    keyboard.add_openlink_button('Оплатить участие', link='https://qiwi.com/p/79171071552')
    keyboard.add_line()
    keyboard.add_openlink_button('Заполнить заявку', link='https://vk.cc/c7SULa')
    keyboard.add_line()
    keyboard.add_button('🔙 Назад 🔙 (Платный туринр)', color=VkKeyboardColor.NEGATIVE)
msg_money = """
Вам необходимо:

1) Оплатить участие по номеру кошелька: 4100116067299663

2) Заполнить заявку на участие: https://vk.cc/c7SULa

3) Прислать скриншот в ЛС сообщества, подтверждающий оплату участия 

После выполнения всех действий ожидайте ответа администратора
"""
def money_button(keyboard):
    keyboard.add_openlink_button('Заполнить заявку', link='https://vk.cc/c7SULa')
    keyboard.add_line()
    keyboard.add_button('🔙 Назад 🔙 (Платный туринр)', color=VkKeyboardColor.NEGATIVE)
msg_tinkoff = """
Вам необходимо: 

1) Оплатить участие по номеру карты: 5536913964252247

2) Заполнить заявку на участие: https://vk.cc/c7SULa

3) Прислать скриншот, подтверждающий оплату участия 

После выполнения всех действий ожидайте ответа администратора
"""
def tinkoff_button(keyboard):
    keyboard.add_openlink_button('Заполнить заявку', link='https://vk.cc/c7SULa')
    keyboard.add_line()
    keyboard.add_button('🔙 Назад 🔙 (Платный туринр)', color=VkKeyboardColor.NEGATIVE)
msg_reviews = """Посмотреть или оставить отзывы о нашей работе можно по ссылке: https://vk.cc/c2vnrz

Мы будем рады, если вы оставите отзыв😉"""

keyboard = VkKeyboard(one_time=True)
# Функция посылающая сообщение
def write_msg(user_id, message):
    random_id = vk_api.utils.get_random_id()
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})
def write_msg_keyboard(user_id, message):
    random_id = vk_api.utils.get_random_id()
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id, 'keyboard': keyboard.get_keyboard()})
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=mytoken)
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.to_me:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            msg = event.text.lower()

            # Логика формирования ответа бота
            if (msg == "помощь" or msg == "\"Помощь\"" or msg == "❔ помощь ❔" or msg == "3" or msg == "[3]" or msg == "начать" or msg == "старт"):
                ans = msg_help
                keyboard.add_button('☰ Меню ☰', color=VkKeyboardColor.PRIMARY)
                write_msg_keyboard(event.user_id, ans)
                keyboard = VkKeyboard(one_time=True)
            elif (msg == "меню" or msg == "☰ меню ☰"):
                ans = msg_menu
                menu_buttons(keyboard)
                write_msg_keyboard(event.user_id, ans)
                keyboard = VkKeyboard(one_time=True)
            elif (msg == "💰 турниры 💰" or msg == "турниры" or msg == "туринир" or msg == "1" or msg == "[1]" or msg == "🔙 назад 🔙 (туринры)"):
                ans = msg_tour
                tour_button(keyboard)
                write_msg_keyboard(event.user_id, ans)
                keyboard = VkKeyboard(one_time=True)
            elif (msg == "🔥 практические игры 🔥" or msg == "практические игры" or msg == "праки" or msg == "8" or msg == "[8]"):
                ans = msg_prakt
                prak_button(keyboard)
                write_msg_keyboard(event.user_id, ans)
                keyboard = VkKeyboard(one_time=True)
            elif (msg == "🎯 кастомки 🎯" or msg == "🎯 кастомка 🎯" or msg == "кастомки" or msg == "кастомка" or msg == "кастом" or msg == "9" or msg == "[9]"):
                ans = msg_custom
                custom_button(keyboard)
                write_msg_keyboard(event.user_id, ans)
                keyboard = VkKeyboard(one_time=True)
            elif (msg == "🔫 платный турнир 🔫" or msg == "платный турнир" or msg == "платный" or msg == "7" or msg == "[7]" or msg == "🔙 назад 🔙 (платный туринр)"):
                ans = msg_platn
                platn_button(keyboard)
                write_msg_keyboard(event.user_id, ans)
                keyboard = VkKeyboard(one_time=True)
            elif (msg == "сбербанк" or msg == "сбер" or msg == "sber" or msg == "10" or msg == "[10]"):
                ans = msg_sber
                sber_button(keyboard)
                write_msg_keyboard(event.user_id, ans)
                keyboard = VkKeyboard(one_time=True)
            elif (msg == "qiwi" or msg == "киви" or msg == "11" or msg == "[11]"):
                ans = msg_qiwi
                qiwi_button(keyboard)
                write_msg_keyboard(event.user_id, ans)
                keyboard = VkKeyboard(one_time=True)
            elif (msg == "юmoney" or msg == "юмани" or msg == "money" or msg == "яндекс деньги" or msg == "яндекс" or msg == "12" or msg == "[12]"):
                ans = msg_money
                money_button(keyboard)
                write_msg_keyboard(event.user_id, ans)
                keyboard = VkKeyboard(one_time=True)
            elif (msg == "tinkoff" or msg == "tinkof" or msg == "тинькофф" or msg == "тинькоф" or msg == "13" or msg == "[13]"):
                ans = msg_tinkoff
                tinkoff_button(keyboard)
                write_msg_keyboard(event.user_id, ans)
                keyboard = VkKeyboard(one_time=True)
            elif (msg == "рассылка" or msg == "данные от лобби" or msg == "рассылки" or msg == "sms" or msg == "2" or msg == "2]"):
                ans = "Подписаться на рассылки можно по ссылке: https://vk.cc/c2taZ7"
                keyboard.add_openlink_button('Перейти к рассылкам', link='https://vk.cc/c2taZ7')
                keyboard.add_line()
                keyboard.add_button('☰ Меню ☰', color=VkKeyboardColor.PRIMARY)
                write_msg_keyboard(event.user_id, ans)
                keyboard = VkKeyboard(one_time=True)
            elif (msg == "отзывы" or msg == "отзыв" or msg == "оставить отзыв" or msg == "4" or msg == "[4]"):
                ans = msg_reviews
                keyboard.add_openlink_button('Отзывы', link='https://vk.cc/c2vnrz')
                keyboard.add_line()
                keyboard.add_button('☰ Меню ☰', color=VkKeyboardColor.PRIMARY)
                write_msg_keyboard(event.user_id, ans)
                keyboard = VkKeyboard(one_time=True)
            elif (msg == "правила" or msg == "5" or msg == "[5]"):
                ans = "Изучить правила нашего сообщества вы можете тут: https://vk.cc/c2tb12"
                keyboard.add_openlink_button('Правила', link='https://vk.cc/c2tb12')
                keyboard.add_line()
                keyboard.add_button('☰ Меню ☰', color=VkKeyboardColor.PRIMARY)
                write_msg_keyboard(event.user_id, ans)
                keyboard = VkKeyboard(one_time=True)
            elif (msg == "улучшение" or msg == "предложить улучшение" or msg == "предложение" or msg == "Оставить предложение по улучшению группы" or msg == "6" or msg == "[6]"):
                ans = "Оставить свое предложение по улучшению нашего сообщества вы можете по ссылке: https://vk.cc/c2xTHw"
                keyboard.add_openlink_button('Оставить предложение', link='https://vk.cc/c2xTHw')
                keyboard.add_line()
                keyboard.add_button('☰ Меню ☰', color=VkKeyboardColor.PRIMARY)
                write_msg_keyboard(event.user_id, ans)
                keyboard = VkKeyboard(one_time=True)

