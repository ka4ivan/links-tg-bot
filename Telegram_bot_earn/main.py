import telebot
import xlsxwriter
import datetime as dt
from telebot import types
joinedFile = open("C:/Users/ivank/PycharmProjects/Telegram_bot_earn/joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()
count = 1
workbook = xlsxwriter.Workbook('messages.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, 'Дата')
worksheet.write(0, 1, 'Час')
worksheet.write(0, 2, 'Тип повідомлення')
worksheet.write(0, 3, 'Відправник')
worksheet.write(0, 4, 'ID відправника')
worksheet.write(0, 5, 'Повідомлення та ID стікера')
worksheet.write(0, 6, 'Емоція стікера')
bot = telebot.TeleBot('5532021713:AAFbbD9azHC98-H9lJij6TTYAr8kBLiNGR0')


@bot.message_handler(commands=['start'])
def start(message):
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("C:/Users/ivank/PycharmProjects/Telegram_bot_earn/joined.txt", "a")
        joinedFile.write(str(message.chat.id)+"\n")
        joinedUsers.add(message.chat.id)
    bot.send_message(message.chat.id, f'👋 Привіт, {message.from_user.first_name} {message.from_user.last_name}.🎉 Вітаємо у нашому боті 🎉')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    earn = types.KeyboardButton('🎯 Завдання')
    sos = types.KeyboardButton('🆘 Тех. Підтримка')
    ad = types.KeyboardButton('📱 Рекламний кабінет')
    donation = types.KeyboardButton('❤ Підтримати бота')
    markup.add(earn).row(sos, ad).add(donation)
    bot.send_message(message.chat.id, f'🤔 Оберіть ваш варіант 💭', reply_markup=markup)


@bot.message_handler(commands=['ad_mailing'])
def mess(message):
    for user in joinedUsers:
        bot.send_message(user, message.text[message.text.find(' '):])

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "🎯 Завдання"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        alpha = types.KeyboardButton('🅰 Альфа Банк(Україна)')
        abank = types.KeyboardButton('🍏 A-банк')
        pumb = types.KeyboardButton('(NEW!)🅿 Пумб')
        mono = types.KeyboardButton('Ⓜ Моно Банк')
        mara = types.KeyboardButton('💵 Mara wallet')
        trx = types.KeyboardButton('💱 TRX AIRDROP! BS BOT(Телеграм бот)')
        exit = types.KeyboardButton('🔙 Назад')
        markup.add(alpha, abank, pumb, mono, mara, trx).add(exit)
        bot.send_message(message.chat.id, f'ℹ Список завдань на даний момент 👀', reply_markup=markup)
    elif (message.text == "🅰 Альфа Банк(Україна)"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посилання Alfa Bank", url="https://hi.alfabank.ua/22W7rFLY7qrNEFb78"))
        bot.send_message(message.chat.id, text="\tВстанови додаток Sense за посиланням нижче та оформи картку Альфа-Банку Україна. Отримай 100 гривень на свій рахунок!\n\n💰Дохід: 100 грн;\n\n👥Реферальна система: 100 грн;\n\n🅰️Абузити: НЕ можна.\n\n💸Вивід: картка Альфа банку(далі по бажанню)", reply_markup=markup)
    elif (message.text == "Ⓜ Моно Банк"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посилання Mono Bank", url="https://monobank.ua/r/ThLjzJ"))
        bot.send_message(message.chat.id, text=f"\tТут все дуже просто.\nОформлюємо картку Моно банку та отримуємо 50 гривень на свій кешбек рахунок\n\n💰Дохід: 50 грн;\n\n👥Реферальна система: 50 грн;\n\n🅰️Абузити: НЕ можна.\n\n💸Вивід: картка Моно банку(далі по бажанню)", reply_markup=markup)
    elif (message.text == "(NEW!)🅿 Пумб"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посилання ПУМБ", url="https://mobile-app.pumb.ua/SbTcPg6uvh1pQxqy5"))
        bot.send_message(message.chat.id, text=f"\tТримайте роздачу від відомого банку 'Пумб'. Він роздає новим користувачам 50 грн за відкриття віртуальної карти та 50 грн за кожного запрошеного друга. Що потрібно робити ? ⬇️\n\n1. скачуємо додаток (лише з телефону) \n2. проходимо просту реєстрацію та відкриваємо картку \n3. проходимо верифікацію за 3 хв з допомогою додатка 'Дія' \n4. поповнюємо карточку та робимо оплату від 100 грн. Все це відбувається без комісії!!!!! \n\n💰Дохід: 50 грн;\n\n👥Реферальна система: 50 грн;\n\n🅰️Абузити: НЕ можна.\n\n💸Вивід: картка банку Пумб(далі по бажанню)", reply_markup=markup)
    elif (message.text == "🍏 A-банк"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посилання A-банк", url="https://abank24.page.link/MTSt"))
        bot.send_message(message.chat.id, text=f"\t1. Замов картку «Зелена» за посиланням \n2. Отримай картку та 50 грн на рахунок кешбеку\n3. Тільки 18+, інакше не працює\n\n💰Дохід: 50 грн;\n\n👥Реферальна система: 50 грн;\n\n🅰️Абузити: НЕ можна.\n\n💸Вивід: картка А-банку банку(далі по бажанню)", reply_markup=markup)
    elif (message.text == "💵 Mara wallet"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посилання Mara Wallet", url="https://mara.xyz/me/MGY9CU"))
        bot.send_message(message.chat.id, text="\tЗареєструйтеся в  Mara Wallet і отримуйте винагороди в доларах США. Вивід після офіційного запуску проєкту. За реєстрацію $2 та за кожного друга плюс $1\n\n💰Дохід: $2;\n\n👥Реферальна система: $1;\n\n🅰️Абузити: Mожна.\n\n💸Вивід: будь-який крипто-гаманець", reply_markup=markup)
    elif (message.text == "💱 TRX AIRDROP! BS BOT(Телеграм бот)"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посилання на trx бота", url="https://t.me/investua_bs_bot?start=1475790039"))
        bot.send_message(message.chat.id, text="\tОтримаємо щоденний бонус в один клік, плюс працює реферальна система яку можна абузити. Вивід в крипті trx tron. Працює тільки для українських телефонних номерів\n\n💰Дохід: 20-100 trx tron;\n\n👥Реферальна система: 1 trx (якщо ваш реферал когось запросить, ви отримуєте відсоток);\n\n🅰️Абузити: Можна.\n\n💸Вивід: крипто-гаманець trx tron", reply_markup=markup)
    elif (message.text == "🔙 Назад"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        earn = types.KeyboardButton('🎯 Завдання')
        sos = types.KeyboardButton('🆘 Тех. Підтримка')
        ad = types.KeyboardButton('📱 Рекламний кабінет')
        donation = types.KeyboardButton('❤ Підтримати бота')
        markup.add(earn).row(sos, ad).add(donation)
        bot.send_message(message.chat.id, f'🤔 Оберіть ваш варіант 💭', reply_markup=markup)
    elif (message.text == "🆘 Тех. Підтримка"):
        markup = types.InlineKeyboardMarkup()
        photo = open('what-is-bot-management.png', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, text="\tПри будь-яких питаннях звертайтесь до нашого менеджера: @Christooo1", reply_markup=markup, parse_mode='html')
    elif (message.text == "📱 Рекламний кабінет"):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📺Зв'язатись по питанням реклами", url="https://t.me/Christooo1"))
        bot.send_message(message.chat.id, text="\t📋Інформація рекламного кабінету:\n\nℹ  За допомогою кнопки «📺Зв'язатись по питанням реклами», ви зможете додати свій канал в нашого бота, або ж запустити банерний пост\n\n<b>Вартість додавання вашого каналу в бота</b> \n\n💳1 тиждень: 50 USDT TRC20 \n💳1 місяць: 160 USDT TRC20\n\n<b>Вартість банерного поста:</b>\n\n💳1 пост: 10 USDT TRC20\n💳3 пост: 25 USDT TRC20\n\n👨‍💼 Менеджер по рекламі - @Christooo1", reply_markup=markup, parse_mode='html')
    elif (message.text == "❤ Підтримати бота"):
        markup = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, text="\tПідтримка працездатності бота\n❤️‍🔥Ми працюємо тільки завдяки вам та задля вас\n\nРеквізити (жмякни по ньому):\n\nⓂМоно банк: <code>5375411418536319</code>\n\n💱BTC: <code>bc1qup63zllhsn9vmzwn2atm2jp6wwldhkn0h7yxau</code>\n\n💵USDT Tether20: <code>TCYB6trdKVeEk6SDdcpDHyNASgQudhpirT</code>\n\nНас підтримали:\nПоки що ніхто 😿", reply_markup=markup, parse_mode='html')
    else:
        bot.send_message(message.chat.id, '❌ Невідома команда!\n\nВи відправили повідомлення напряму в чат бота, або структура меню була змінена Адміном.\n\nℹ  Не відправляйте прямих повідомлень боту або обновіть Меню, натисніть /start', parse_mode='html')
    global count
    if message.content_type == 'text':
        if message.text != 'Покажи переписки':
            worksheet.write(count, 0, str(dt.datetime.now().date()))
            worksheet.write(count, 1, str(dt.datetime.now().time())[0:8])
            worksheet.write(count, 2, 'текст')
            worksheet.write(count, 3, str(message.from_user.first_name) + ' ' + str(message.from_user.last_name))
            worksheet.write(count, 4, message.from_user.id)
            worksheet.write(count, 5, message.text)
            count += 1
        else:
            workbook.close()



@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    global count
    if message.content_type == 'sticker':
        if message.text != 'Покажи переписки':
            worksheet.write(count, 0, str(dt.datetime.now().date()))
            worksheet.write(count, 1, str(dt.datetime.now().time())[0:8])
            worksheet.write(count, 2, 'стікер')
            worksheet.write(count, 3, str(message.from_user.first_name) + ' ' + str(message.from_user.last_name))
            worksheet.write(count, 4, message.from_user.id)
            worksheet.write(count, 5, message.sticker.file_id)
            worksheet.write(count, 6, message.sticker.emoji)
            count += 1
        else:
            workbook.close()

bot.polling(none_stop=True)
