from dp.keyboards.reply_keyboard import ReplyKeyboardButton, ReplyKeyboardMarkup


button1 = ReplyKeyboardButton(text="State🚥")
button2 = ReplyKeyboardButton(text="Inline Keyboard⌨️")
btn_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(button1, button2)