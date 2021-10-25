def get_description():
    """
    傳出亂數的天氣狀況
    """

    from random import choice
    possibilities = ["下雨", "下雪", "陰天", "晴天", "大太陽", "颱風"]
    return choice(possibilities)