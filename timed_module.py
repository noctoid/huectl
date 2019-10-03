import time

def _get_hour():
    return time.localtime()[3]


def _get_min():
    return time.localtime()[4]


def calculate_brightness_by_time():
    h = _get_hour()
    m = _get_min()

    # if h >= 16 and h < 19:
    #     # getting things more bright
    #     return ((h-16)*60 + m)*100 // 180
    # elif h >= 19:
    #     # get brightness to max
    #     return 100
    # elif h >= 6:
    #     # set brightness to 0
    #     return 0
    # else:
    #     # set brightness to 1
    #     return 1

    if h < 6:
        # night light -> min brightness
        return 1
    elif h < 16:
        # day -> off
        return 0
    elif h < 19:
        # sunset -> getting bright
        return ((h-16)*60 + m)*100 // 180
    elif h < 22:
        return 100
    elif h < 23:
        return 100 - m*100 // 60
    else: # h = 23
        return 1
        




def calculate_color_by_time():
    h = _get_hour()
    m = _get_min()

    # if h > 16 and h < 20:
    #     return 0
    # elif h >= 20 and h < 23:
    #     # getting things more warm
    #     return ((h-20)*60 + m)*100 // 180
    # elif h >= 23:
    #     # get color to warm
    #     return 100
    # elif h >= 6:
    #     # set color to cool
    #     return 0
    # else:
    #     # set color to cool
    #     return 1

    if h < 6:
        return 100
    elif h < 16:
        return 0
    elif h < 20:
        return 0
    elif h < 23:
        return ((h-20)*60 + m)*100 // 180
    else: # h = 23
        return 100





