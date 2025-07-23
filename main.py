from rubika import Robot

bot = Robot("BEIBH0SDMUGGIRYVBEYMTPMHRTZVKYZWUXRRLDQHSWRUCOAQAFFJLNOIOTNPXGNQ")

@bot.on_message
def handle_message(msg):
    user_guid = msg['author_guid']
    text = msg.get("text", "")

    if text == "/start":
        buttons = [
            [{"text": "باز کردن برنامه 📲", "link": "https://mahdishamiahar.github.io/VIPZEXNETBOT/"}],
            [{"text": "دریافت نرم‌افزار 🧠", "link": "https://mahdishamiahar.github.io/app.VIPZEXNET/"}],
            [{"text": "سایت رسمی 🌐", "link": "https://mahdishamiahar.github.io/Web.VIPZEXNET/"}],
            [{"text": "پشتیبانی 💬", "link": "https://rubika.ir/Mahdi_shami89"}],
            [{"text": "خرید سرویس 💳", "link": "https://rubika.ir/Mahdi_shami89"}]
        ]
        bot.send_message(user_guid, "👇 لطفاً یکی از گزینه‌های زیر را انتخاب کنید:", inline_buttons=buttons)
    else:
        bot.send_message(user_guid, "❓ لطفاً فقط دستور /start را ارسال کنید.")

bot.run()