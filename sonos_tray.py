import pystray
import soco
from PIL import Image, ImageDraw


def mute(zone):
    zone.mute = not zone.mute


def menu():
    for zone in soco.discover():

        def _mute():
            mute(zone)

        yield pystray.MenuItem(text=zone.player_name, action=_mute)


def create_image():
    image = Image.new("RGB", (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle((width // 2, 0, width, height // 2), fill=color2)
    dc.rectangle((0, height // 2, width // 2, height), fill=color2)

    return image


if __name__ == "__main__":
    icon = pystray.Icon("test name", menu=pystray.Menu(menu))

    width = 50
    height = 50
    color1 = (255, 255, 0)
    color2 = (0, 0, 255)

    icon.icon = create_image()

    icon.run()
