# Whatsapp Message Scheduler

You can schedule your messages on whatsapp-web with this project.

## Installation

```bash
git clone https://github.com/Unreol-Freedom/whatsapp-message-scheduler.git
cd whatsapp-message-scheduler/
pip3 install -r requirements.txt
```

## Usage

There are two main Python scripts: `main.py` and `configuration_gui.py`
You can edit the target which is going to get your scheduled message on time when you run `configuration_gui.py`
You can schedule your message when you run `main.py`.

---

###### Example Usage:

```bash
python3 configuration_gui.py
```

![ss](https://user-images.githubusercontent.com/81323808/131787084-3c7b772b-98fb-44da-86fc-d3fe367937dc.png)
When you click the `save` button, it saves your datas that you entered to the json.

---

![ss](https://user-images.githubusercontent.com/81323808/131787089-e182bf2c-36b0-40a6-b558-77bb555495d9.png)

If you want to edit the json specifically you can click the `edit` button. You can edit the json in the interface that will be opened. You can click the `reset` button to reset the content of json, this makes the content of the json initial.

---

And after configuration, you can run `main.py`

```bash
python3 main.py
```

You are going to get something like this:

```
There is 1 message to send, it has been scheduled.
Next message will be delivered after 35 seconds.


Make sure wifi of your mobile phone is enabled
```

After 35 seconds, whatsapp-web will be opened and after 10 seconds your message will be delivered by PyAutoGUI:

```python
timer = threading.Timer(10, lambda: pyautogui.press("enter"))
timer.run()
```

---

## Credits

<img src="https://avatars.githubusercontent.com/u/81323808?v=4" width="100px"></img>
