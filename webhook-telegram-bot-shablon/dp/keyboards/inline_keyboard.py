class InlineKeyboardButton:
    """
    ReplyKeyboardButton
    """
    def __init__(self) -> None:
        pass

    def __new__(self, text, callback_data=None, url=None) -> dict:
        response =  {"text":f"{text}"}
        if callback_data:
            response["callback_data"] = callback_data
        else:
            response["url"] = url

        return response


class InlineKeyboardMarkup:
    """
    ReplyKeyboardMarkup
    """
    data_ = {}
    def __init__(self) -> None:
        self.data_ = InlineKeyboardMarkup.data_

    # Add Button
    def add(self, *data:dict) -> dict:
        list_ = []
        rgs = 0
        for i in data:
            if i == True:
                rgs = 1
            elif rgs:
                list_[-1].append(i)
                rgs = 0
            else:
                list_.append([i])

        
        self.data_["inline_keyboard"] = list_
        return self.data_
