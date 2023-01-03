class ReplyKeyboardButton:
    """
    ReplyKeyboardButton
    """
    def __init__(self) -> None:
        pass

    def __new__(self, text) -> dict:
        response =  {"text":f"{text}"}
        return response


class ReplyKeyboardMarkup:
    """
    ReplyKeyboardMarkup
    """
    data_ = {}
    def __init__(self, resize_keyboard=True) -> None:
        self.resize_keyboard = resize_keyboard
        self.data_ = ReplyKeyboardMarkup.data_

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

        
        self.data_["keyboard"] = list_
        self.data_["resize_keyboard"] = self.resize_keyboard
        return self.data_
