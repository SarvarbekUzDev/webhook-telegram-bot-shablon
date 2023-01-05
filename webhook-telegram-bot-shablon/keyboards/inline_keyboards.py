from dp.keyboards.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup



like = InlineKeyboardButton(text="Like👍", callback_data="like")
mysite = InlineKeyboardButton(text="Your my website🚥", url="https://github.com/SarvarbekUzDev")
inline_markup = InlineKeyboardMarkup(variable_name="inline_markup").add(like, mysite)
