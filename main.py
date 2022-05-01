import pyperclip
import json
import pystray
import PIL.Image
import time
import os


def on_clicked(icon_object, item):
    file = open("logins.json", "r")
    data = json.load(file)
    file.close()

    pyperclip.copy(data[str(item)]['password'])
    time.sleep(1)
    pyperclip.copy(data[str(item)]['email'])


with open("logins.json", "r+") as f:
    login_data = json.load(f)
    accounts = [pystray.MenuItem(name, on_clicked) for name in login_data.keys()]
    accounts.append(pystray.MenuItem("Open Logins File", lambda x, y: os.startfile("logins.json")))
    accounts.append(pystray.MenuItem("Exit", lambda icon_object, item: icon_object.stop()))

image = PIL.Image.open("icon.ico")
icon = pystray.Icon("Battle.net Logins", image, menu=pystray.Menu(*accounts))

icon.run()
