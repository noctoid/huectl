import requests
import json

def get_light_state():
    pass


def put_light_state(on, sat, bri, hue):
    if on == None:
        return

    try:
        req = requests.put(
            "http://10.0.4.142/api/-JgSQx-ZZV3uPsBi7xPzv3CI5K2XOAXHbnI7wg2R/lights/4/state",
            data = json.dumps({
                "on": on,
                "sat": sat,
                "bri": bri,
                "hue": hue
            })
        )
        req = requests.put(
            "http://10.0.4.142/api/-JgSQx-ZZV3uPsBi7xPzv3CI5K2XOAXHbnI7wg2R/lights/3/state",
            data = json.dumps({
                "on": on,
                "sat": sat,
                "bri": bri,
                "hue": hue
            })
        )
    except requests.exceptions.RequestException as e:
        print(e)
        raise

    return       

def set_color_brightness(color, brightness):
    """
    give color and brightness as an integer [0,100]
    color 0 -> cold; 100 -> warm
    brightness you know it :)
    """
    if brightness == 0:
        put_light_state(False, 0, 0, 16000)
    else:
        put_light_state(
            True,
            254 * color // 100,
            254 * brightness // 100,
            16000
        )
