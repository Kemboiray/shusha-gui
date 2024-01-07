from pathlib import Path
from tkinter import ttk, Tk, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk
from ttkbootstrap import style
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

# import ttkbootstrap as ttk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# window = ttk.Window(
#     title="shusha", iconphoto="shusha.ico", size=(864, 605), resizable=(False, False)
# )

window = Tk()
window.geometry("864x605")
window.configure(bg="#2A2E31")
window.title("shusha")
# window.iconbitmap("shusha.ico")
im = Image.open("shusha.ico")
photo = ImageTk.PhotoImage(im)
window.wm_iconphoto(True, photo)
window.resizable(False, False)

# canvas = Canvas(
#     window,
#     bg="gray22",
#     height=605,
#     width=864,
#     bd=0,
#     highlightthickness=0,
#     relief="ridge",
# )

# canvas.place(x=0, y=0)
# canvas.create_rectangle(0.0, 541.0, 864.0, 605.0, fill="#2A2E31", outline="")

slider_img = PhotoImage(file=relative_to_assets("icons8-slider-64.png"))
slider_btn = Button(
    image=slider_img,
    bg="#2A2E31",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("slider clicked"),
    relief="flat",
)
slider_btn.place(x=340.0, y=548.0, width=50.0, height=50.0)

pause_img = PhotoImage(file=relative_to_assets("icons8-pause-button-64.png"))
pause2_btn = Button(
    image=pause_img,
    bg="#2A2E31",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("pause clicked"),
    relief="flat",
)
pause2_btn.place(x=285.0, y=548.0, width=50.0, height=50.0)

play_img = PhotoImage(file=relative_to_assets("icons8-circled-play-64.png"))
play2_btn = Button(
    image=play_img,
    bg="#2A2E31",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("play clicked"),
    relief="flat",
)
play2_btn.place(x=230.0, y=548.0, width=50.0, height=50.0)

# entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
# entry_bg_1 = canvas.create_image(115.0, 573.5, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_1.place(x=10.0, y=557.5, width=210.0, height=30.0)

# canvas.create_rectangle(0.0, 0.0, 864.0, 64.0, fill="#2A2E31", outline="")

settings_img = PhotoImage(file=relative_to_assets("icons8-slider_2-64.png"))
settings_btn = Button(
    image=settings_img,
    bg="#2A2E31",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("settings clicked"),
    relief="flat",
)
settings_btn.place(x=804.0, y=7.0, width=50.0, height=50.0)

log_img = PhotoImage(file=relative_to_assets("icons8-log-64.png"))
log_btn = Button(
    image=log_img,
    bg="#2A2E31",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("log clicked"),
    relief="flat",
)
log_btn.place(x=749.0, y=7.0, width=50.0, height=50.0)

down_img = PhotoImage(file=relative_to_assets("icons8-scroll-down-64.png"))
down_btn = Button(
    image=down_img,
    bg="#2A2E31",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("down clicked"),
    relief="flat",
)
down_btn.place(x=230.0, y=7.0, width=50.0, height=50.0)

up_img = PhotoImage(file=relative_to_assets("icons8-arrow-64.png"))
up_btn = Button(
    image=up_img,
    bg="#2A2E31",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("up clicked"),
    relief="flat",
)
up_btn.place(x=175.0, y=7.0, width=50.0, height=50.0)

pause1_btn = Button(
    image=pause_img,
    bg="#2A2E31",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("pause clicked"),
    relief="flat",
)
pause1_btn.place(x=120.0, y=7.0, width=50.0, height=50.0)

play1_btn = Button(
    image=play_img,
    bg="#2A2E31",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("play clicked"),
    relief="flat",
)
play1_btn.place(x=65.0, y=7.0, width=50.0, height=50.0)

add_img = PhotoImage(file=relative_to_assets("icons8-add-64.png"))
add_btn = Button(
    image=add_img,
    bg="#2A2E31",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("add clicked"),
    relief="flat",
)
add_btn.place(x=10.0, y=7.0, width=50.0, height=50.0)

style = ttk.Style()
style.configure("TTreeview", background="#2A2E31", foreground="white")
coldata = [
    {"text": "LicenseNumber", "stretch": False},
    "CompanyName",
    {"text": "UserCount", "stretch": False},
]

rowdata = [
    ("A123", "IzzyCo", 12),
    ("A136", "Kimdee Inc.", 45),
    ("A158", "Farmadding Co.", 36),
]

dt = Tableview(
    master=window,
    coldata=coldata,
    rowdata=rowdata,
    paginated=True,
    searchable=True,
    # bootstyle="outline-dark",
)
# stripecolor=(colors.light, None),

dt.place(x=0, y=64, width=864, height=477)
window.mainloop()
