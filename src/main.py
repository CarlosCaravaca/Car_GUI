import tkinter as tk
from gui import gui
from PIL import Image, ImageTk

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
        self.master.geometry("1024x600")
        self.master.configure(background='black')
        self.frame = tk.Frame(self.master)
        logoImage1 = Image.open(r'D:\Users\Lidia\Documents\Carlos\Car_GUI\img\maxresdefault.png')
        image1 = ImageTk.PhotoImage(logoImage1)
        logoLabel1 = tk.Label(image=image1)
        logoLabel1.image = image1
        self.button1 = tk.Button(self.master, text = 'Open Car Status', width = 400, height=225, command = self.car_diagnosis,image=image1,bg='black')
        #self.button1.grid(row=0,column=0,padx=20,pady=20)
        self.button1.place(x=50,y=30)
        logoImage2 = Image.open(r'D:\Users\Lidia\Documents\Carlos\Car_GUI\img\maps.png')
        image2 = ImageTk.PhotoImage(logoImage2)
        logoLabel2 = tk.Label(image=image2)
        logoLabel2.image = image2
        self.button2 = tk.Button(self.master, text = 'Open Car Status', width = 400, height=225, command = self.car_diagnosis,image=image2)
        #self.button2.grid(row=0,column=1,padx=20,pady=20)
        self.button2.place(x=550,y=30)
        logoImage3 = Image.open(r'D:\Users\Lidia\Documents\Carlos\Car_GUI\img\camera.png')
        image3 = ImageTk.PhotoImage(logoImage3)
        logoLabel3 = tk.Label(image=image3)
        logoLabel3.image = image3
        self.button3 = tk.Button(self.master, text = 'Open Car Status', width = 400, height=225, command = self.car_diagnosis,image=image3)
        #self.button3.grid(row=1,column=0,padx=20,pady=20)
        self.button3.place(x=50,y=330)
        logoImage4 = Image.open(r'D:\Users\Lidia\Documents\Carlos\Car_GUI\img\rear.png')
        image4 = ImageTk.PhotoImage(logoImage4)
        logoLabel4 = tk.Label(image=image4)
        logoLabel4.image = image4
        self.button4 = tk.Button(self.master, text = 'Open Car Status', width = 400, height=225, command = self.car_diagnosis,image=image4)
        #self.button4.grid(row=1,column=1,padx=20,pady=20)
        self.button4.place(x=550,y=330)
        self.frame.pack()

    def car_diagnosis(self):
        self.master.destroy()
        self.app = Demo2()

class Demo2:
    def __init__(self):
        gui()
    def __del__(self):
        main()

if __name__ == '__main__':
    main()