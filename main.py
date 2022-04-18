import tkinter as tk
import pyautogui
from threading import Thread
root = tk.Tk()
root.title("Auto Hotkey")
root.geometry("800x800")
inputs = []


def remove_input(index: int):
    inputs[index]['button'].destroy()
    inputs[index]['input'].destroy()
    inputs.pop(index)


def get_keys() -> list:
    return [i['input'].get() for i in inputs]


def make_input():
    input = tk.Entry(root, width=20)

    btn = tk.Button(
        root, width=4, height=1, text="-", command=lambda: remove_input(inputs.index({'input': input, 'button': btn})))

    inputs.append({'input': input, 'button': btn})
    input.grid(padx=40, pady=30, row=inputs.index(
        {'input': input, 'button': btn}), column=0)
    btn.grid(pady=10, row=inputs.index(
        {'input': input, 'button': btn}), column=1)


toogle = False


def hotkey(*keys):
    while toogle:
        pyautogui.hotkey(*keys)


def spam(btn: tk.Button):
    global toogle
    toogle = not toogle

    keys = get_keys()

    thread = Thread(target=hotkey, args=(keys))
    thread.daemon = True
    thread.start()
    if toogle and len(inputs) > 0:
        btn.config(text="Stop Spamming")
    else:
        btn.config(text="Start Spamming")


plus_btn = tk.Button(root, text="Add Hotkey", command=make_input, bg="green")
plus_btn.place(anchor=tk.CENTER, relx=0.5, rely=0.05)

start_spamming = tk.Button(root, text="Start Spamming",
                           command=lambda: spam(start_spamming), bg="red")
start_spamming.place(anchor=tk.CENTER, relx=0.5, rely=0.2)

root.mainloop()
