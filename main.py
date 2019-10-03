from control import put_light_state, set_color_brightness
from timed_module import calculate_brightness_by_time, calculate_color_by_time

from random import randrange
from time import sleep, strftime


def run():
    brightness = calculate_brightness_by_time()
    color = calculate_color_by_time()
    set_color_brightness(color, brightness)
    print("["+strftime("%H:%M:%S")+"] Brightness -> "+str(brightness)+", Color -> "+str(color))


if __name__ == "__main__":
    # put_light_state(True, 100, 254, 16000)
    # while True:
    #     put_light_state(True, 254, 254, randrange(1,65000))
    #     sleep(0.025)
    while 1:
        run()
        sleep(60)
