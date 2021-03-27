import tkinter as tk
from gui import gui
'''
INIT CONNECTION
'''
def main():
	roots = tk.Tk()
	app = Demo1(roots)
	roots.mainloop()

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Open Car Status', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()

    def new_window(self):
        self.app = Demo2()

class Demo2:
    def __init__(self):
    	global root
    	root = tk.Tk()
    	gui(root)

    def close_windows(self):
        self.master.destroy()

if __name__ == '__main__':
    main()