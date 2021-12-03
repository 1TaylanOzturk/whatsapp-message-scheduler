import webbrowser
import pyautogui
import threading
import json
import time



def send_message():
    url = 'https://web.whatsapp.com/send?phone=' + element["target"] + '&text=' + element["message"]
    webbrowser.open(url)
    timer = threading.Timer(10, lambda: pyautogui.press("enter"))
    timer.run()

localtime = time.localtime()
with open("src/.config/targets.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    global length_of_data
    length_of_data = len(data)
if length_of_data == 1:
    print(f"There is {length_of_data} message to send, it has been scheduled.")
else:
    print(f"There are {length_of_data} messages to send, all of them have been scheduled.")
    print("Make sure wifi of your mobile phone is enabled\n")

for element in data:
    hours = localtime.tm_hour
    minutes = localtime.tm_min
    seconds = localtime.tm_sec
    current_total_seconds = hours * 3600 + minutes * 60 + seconds
    target_total_seconds = int(element["hour"]) * 3600 + int(element["minute"]) * 60
    diff = target_total_seconds - current_total_seconds

    print(f"Next message will be delivered after {diff} seconds.")
    timer = threading.Timer(diff, send_message)
    timer.run()
    
    
  

