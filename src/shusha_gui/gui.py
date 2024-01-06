
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame0")

# print(type(OUTPUT_PATH))

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("864x605")
window.configure(bg = "wheat")
window.title("shusha")
window.iconbitmap("shusha.ico")
window.resizable(False, False)


canvas = Canvas(
    window,
    bg = "gray22",
    height = 605,
    width = 864,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    541.0,
    864.0,
    605.0,
    fill="#2A2E31",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("icons8-slider-64.png"))
button_1 = Button(
    image=button_image_1,
    bg="#2A2E31",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=340.0,
    y=548.0,
    width=50.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("icons8-pause-button-64.png"))
button_2 = Button(
    image=button_image_2,
    bg="#2A2E31",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=285.0,
    y=548.0,
    width=50.0,
    height=50.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("icons8-circled-play-64.png"))
button_3 = Button(
    image=button_image_3,
    bg="#2A2E31",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=230.0,
    y=548.0,
    width=50.0,
    height=50.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    115.0,
    573.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=10.0,
    y=551.0,
    width=210.0,
    height=43.0
)

canvas.create_rectangle(
    0.0,
    0.0,
    864.0,
    64.0,
    fill="#2A2E31",
    outline="")

button_image_4 = PhotoImage(
    file=relative_to_assets("icons8-slider_2-64.png"))
button_4 = Button(
    image=button_image_4,
    bg="#2A2E31",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=804.0,
    y=7.0,
    width=50.0,
    height=50.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("icons8-log-64.png"))
button_5 = Button(
    image=button_image_5,
    bg="#2A2E31",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=749.0,
    y=7.0,
    width=50.0,
    height=50.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("icons8-scroll-down-64.png"))
button_6 = Button(
    image=button_image_6,
    bg="#2A2E31",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=230.0,
    y=7.0,
    width=50.0,
    height=50.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("icons8-arrow-64.png"))
button_7 = Button(
    image=button_image_7,
    bg="#2A2E31",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=175.0,
    y=7.0,
    width=50.0,
    height=50.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("icons8-pause-button-64.png"))
button_8 = Button(
    image=button_image_8,
    bg="#2A2E31",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=120.0,
    y=7.0,
    width=50.0,
    height=50.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("icons8-circled-play-64.png"))
button_9 = Button(
    image=button_image_9,
    bg="#2A2E31",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=65.0,
    y=7.0,
    width=50.0,
    height=50.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("icons8-add-64.png"))
button_10 = Button(
    image=button_image_10,
    bg="#2A2E31",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=10.0,
    y=7.0,
    width=50.0,
    height=50.0
)
window.mainloop()
