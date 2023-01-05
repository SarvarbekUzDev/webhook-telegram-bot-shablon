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
    def __init__(self, variable_name, resize_keyboard=True) -> None:
        self.resize_keyboard = resize_keyboard
        self.variable_name = variable_name
        self.data_ = ReplyKeyboardMarkup.data_
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

        
        self.data_[f"{self.variable_name}"]["keyboard"] = list_
        self.data_[f"{self.variable_name}"]["resize_keyboard"] = self.resize_keyboard
        return self.data_
