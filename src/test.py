import tkinter as tk
from cfg import *

'''
INIT CONNECTION
'''

'''
GUI
'''
#Root window
root = tk.Tk()
root.title("Car System")
root.geometry("480x320")
root.attributes('-fullscreen', True)
root.configure(background=color_background)

#Title Bar
logoImage = tk.PhotoImage(file=logo_path)
logoLabel = tk.Label(image=logoImage)
logoLabel.place(x=6, y=2, height=36, width=36)

#Make title
titleLabel1 = tk.Label(root, fg=color_make, bg=color_background, font=("Aldrich, 20"), text=make)
titleLabel1.place(x=42, y=8)

#Model title
titleLabel2 = tk.Label(root, fg=color_model, bg=color_background, font=("Aldrich, 14"), text=model)
titleLabel2.place(x=120, y=14)

#Time title
timeLabel = tk.Label(root, fg=color_time, bg=color_background, font=("Aldrich, 16"), text="00:00:00")
timeLabel.place(x=376, y=12)

#Status title
statusLabel = tk.Label(root, fg=color_status, bg=color_background, font=("Aldrich, 16"), text="NOT_CONNECTED")
statusLabel.place(x=376, y=12)

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE
    }

window = tk.Tk()

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name, bg=color, fg='tomato')
    label.pack()

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

#frame_a.pack()
#frame_b.pack()

window.mainloop()