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
    def __init__(self, variable_name) -> None:
        self.variable_name = variable_name
        self.data_ = InlineKeyboardMarkup.data_
        self.data_[f"{variable_name}"] = {}

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

        
        self.data_[f"{self.variable_name}"]["inline_keyboard"] = list_
        return self.data_
