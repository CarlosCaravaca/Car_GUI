import tkinter as tk
from tkinter import ttk
from cfg import *
from PIL import Image, ImageTk

'''
GUI
'''
def gui():
	#master window
	master = tk.Tk()
	master.title("Car System")
	master.geometry("1024x600")
	master.attributes('-fullscreen', False)
	master.configure(background=color_background)

	# Title Bar
	#----------------------------------------------------------

	#Title Bar
	logoImage = Image.open(r'D:\Users\Lidia\Documents\Carlos\Car_GUI\img\seat_logo.png')
	image = ImageTk.PhotoImage(logoImage)

	logoLabel = tk.Label(image=image)
	logoLabel.image = image
	#logoLabel.grid(column=1)
	logoLabel.place(x=10, y=0, height=108, width=108)
	'''
	logoImage = tk.PhotoImage(file=)
	logoLabel = tk.Label(image=logoImage)
	logoLabel.lift()
	logoLabel.place(x=6, y=8, height=36, width=36)
	logoLabel.lift()
	'''
	#Make title
	#titleLabel1 = tk.Label(master, fg=color_make, bg=color_background, font=("Aldrich", 20), text=make)
	#titleLabel1.place(x=42, y=8)

	#Model title
	titleLabel2 = tk.Label(master, fg=color_model, bg=color_background, font=("Aldrich", 32), text=model)
	#titleLabel2.grid(column=2)
	titleLabel2.place(x=126, y=40)

	#Time title
	timeLabel = tk.Label(master, fg=color_time, bg=color_background, font=("Aldrich", 32), text="00:00:00")
	timeLabel.place(x=800, y=40)

	#Status title
	statusLabel = tk.Label(master, fg=color_status, bg=color_background, font=("Aldrich", 26), text="NOT_CONNECTED")
	statusLabel.place(x=18, y=485)

	# Pi Labels
	#----------------------------------------------------------

	piLabel = tk.Label(master, fg=color_pi, bg=color_background, font=("Aldrich", 26), text="Pi:")
	piLabel.place(x=500, y=485)

	pitempLabel = tk.Label(master, fg=color_temp, bg=color_background, font=("Aldrich", 26), text="0")
	pitempLabel.place(x=600, y=485)
	pitempxLabel = tk.Label(master, fg=color_c, bg=color_background, font=("Aldrich", 26), text='ºC')
	pitempxLabel.place(x=700, y=485)

	piclockLabel = tk.Label(master, fg=color_clock, bg=color_background, font=("Aldrich", 26), text="0")
	piclockLabel.place(x=800, y=485)
	piclockxLabel = tk.Label(master, fg=color_mhz, bg=color_background, font=("Aldrich", 26), text="MHz")
	piclockxLabel.place(x=900, y=485)

	# Left Labels
	#----------------------------------------------------------

	batteryLabel = tk.Label(master, fg=color_labels, bg=color_background, font=("Aldrich", 22), text="Voltaje:")
	batteryLabel.place(x=labelsX, y=110)
	batteryPercentageLabel = tk.Label(master, fg=color_values, bg=color_background, font=("Aldrich", 22), text="... V")
	batteryPercentageLabel.place(x=valuesX, y=110)

	waterLabel = tk.Label(master, fg=color_labels, bg=color_background, font=("Aldrich", 22), text="T. Refrigerante:")
	waterLabel.place(x=labelsX, y=150)
	waterPercentageLabel = tk.Label(master, fg=color_values, bg=color_background, font=("Aldrich", 22), text="... "+'ºC')
	waterPercentageLabel.place(x=valuesX, y=150)

	airLabel = tk.Label(master, fg=color_labels, bg=color_background, font=("Aldrich", 22), text="T. Entrada Aire:")
	airLabel.place(x=labelsX, y=190)
	airPercentageLabel = tk.Label(master, fg=color_values, bg=color_background, font=("Aldrich", 22), text="... "+'ºC')
	airPercentageLabel.place(x=valuesX, y=190)

	airflowLabel = tk.Label(master, fg=color_labels, bg=color_background, font=("Aldrich", 22), text="Caudal de aire:")
	airflowLabel.place(x=labelsX, y=230)
	airflowPercentageLabel = tk.Label(master, fg=color_values, bg=color_background, font=("Aldrich", 22), text="... g/s")
	airflowPercentageLabel.place(x=valuesX, y=230)

	lambdaLabel1 = tk.Label(master, fg=color_labels, bg=color_background, font=("Aldrich", 22), text="Lambda 1:")
	lambdaLabel1.place(x=labelsX, y=270)
	lambdaPercentageLabel1 = tk.Label(master, fg=color_values, bg=color_background, font=("Aldrich", 22), text="... mV")
	lambdaPercentageLabel1.place(x=valuesX, y=270)

	lambdaLabel2 = tk.Label(master, fg=color_labels, bg=color_background, font=("Aldrich", 22), text="Lambda 2:")
	lambdaLabel2.place(x=labelsX, y=310)
	lambdaPercentageLabel2 = tk.Label(master, fg=color_values, bg=color_background, font=("Aldrich", 22), text="... mV")
	lambdaPercentageLabel2.place(x=valuesX, y=310)

	ignitionLabel = tk.Label(master, fg=color_labels, bg=color_background, font=("Aldrich", 22), text="Avance encendido:")
	ignitionLabel.place(x=labelsX, y=350)
	ignitionPercentageLabel = tk.Label(master, fg=color_values, bg=color_background, font=("Aldrich", 22), text="... "+'º')
	ignitionPercentageLabel.place(x=valuesX, y=350)

	loadLabel = tk.Label(master, fg=color_labels, bg=color_background, font=("Aldrich", 26), text="Carga motor:")
	loadLabel.place(x=labelsX, y=395)
	loadPercentageLabel = tk.Label(master, fg=color_values, bg=color_background, font=("Aldrich", 26), text="... %")
	loadPercentageLabel.place(x=valuesX, y=395)

	gasLabel = tk.Label(master, fg=color_labels, bg=color_background, font=("Aldrich", 26), text="Acelerador:")
	gasLabel.place(x=labelsX, y=440)
	gasPercentageLabel = tk.Label(master, fg=color_values, bg=color_background, font=("Aldrich", 26), text="... %")
	gasPercentageLabel.place(x=valuesX, y=440)

	# Right Labels
	#----------------------------------------------------------

	speedLabel = tk.Label(master, fg=color_speed, bg=color_background, font=("Aldrich", 45), text="0")
	speedLabel.place(x=580, y=110)
	kmhLabel = tk.Label(master, fg=color_kmh, bg=color_background, font=("Aldrich", 45), text="km/h")
	kmhLabel.place(x=720, y=110)

	revsLabel = tk.Label(master, fg=color_revs, bg=color_background, font=("Aldrich", 40), text="0")
	revsLabel.place(x=580, y=170)
	uminLabel = tk.Label(master, fg=color_umin, bg=color_background, font=("Aldrich", 40), text="rpm")
	uminLabel.place(x=720, y=170)

	# Gauges
	#----------------------------------------------------------

	#speedGauge = tk.Canvas(master, bg=color_background, width=180, height=200)
	#speedGauge.place(x=680, y=140)
	#speedGauge.create_arc(10, 10, 170, 190, style="arc", width=20, start=-10, extent=170, outline=color_speed, tags=('arc2'))
	#speedGauge.create_arc(10, 10, 170, 190, style="arc", width=20, start=160, extent=20, outline=color_speed, tags=('arc1'))

	#polyPoints = [(100, 40), (110, 100), (100, 110), (90, 100)]
	#polyNeedle = speedGauge.create_polygon(polyPoints, fill='white')

	# Bars
	#----------------------------------------------------------


	lambdaBarsLabel = tk.Label(master, fg=color_lambda_h, bg=color_background, font=("Aldrich", 18), text="Aire/Gasolina:")
	lambdaBarsLabel.place(x=580, y=240)
	lambdaBarsLabel2 = tk.Label(master, fg=color_lambda_f, bg=color_background, font=("Aldrich", 18), text="Pobre                                 Rico")
	lambdaBarsLabel2.place(x=580, y=340)

	lambda1BarCanvas = tk.Canvas(master, bg=color_background, width=360, height=24, borderwidth=0, highlightthickness=0)
	lambda1BarCanvas.create_rectangle(0, 2, 80, 10, fill=color_lambda_1bad)
	lambda1BarCanvas.create_rectangle(60, 2, 140, 10, fill=color_lambda_1okay)
	lambda1BarCanvas.create_rectangle(140, 2, 220, 10, fill=color_lambda_1good)
	lambda1BarCanvas.create_rectangle(220, 2, 300, 10, fill=color_lambda_1okay)
	lambda1BarCanvas.create_rectangle(300, 2, 360, 10, fill=color_lambda_1bad)
	lambda1Pointer = lambda1BarCanvas.create_rectangle(176, 0, 184, 11, fill='white')
	lambda1BarCanvas.place(x=580, y=282 + 1)

	lambda2BarCanvas = tk.Canvas(master, bg=color_background, width=360, height=24, borderwidth=0, highlightthickness=0)
	lambda2BarCanvas.create_rectangle(0, 2, 80, 10, fill=color_lambda_1bad)
	lambda2BarCanvas.create_rectangle(60, 2, 140, 10, fill=color_lambda_1okay)
	lambda2BarCanvas.create_rectangle(140, 2, 220, 10, fill=color_lambda_1good)
	lambda2BarCanvas.create_rectangle(220, 2, 300, 10, fill=color_lambda_1okay)
	lambda2BarCanvas.create_rectangle(300, 2, 360, 10, fill=color_lambda_1bad)
	lambda2Pointer = lambda2BarCanvas.create_rectangle(176, 0, 184, 11, fill='white')
	lambda2BarCanvas.place(x=580, y=312 + 1)

	gasLoadTheme = ttk.Style()
	gasLoadTheme.theme_use('clam')
	gasLoadTheme.configure("loadBarTheme.Horizontal.TProgressbar", background=color_load_bar, troughcolor=color_background, bordercolor="gray30")

	loadBar = ttk.Progressbar(master, style="loadBarTheme.Horizontal.TProgressbar", orient="horizontal", length=360, mode="determinate", maximum=100)
	loadBar.place(x=580, y=410)

	gasBarTheme = ttk.Style()
	gasBarTheme.theme_use('clam')
	gasBarTheme.configure("gasBarTheme.Horizontal.TProgressbar", background=color_gas_bar, troughcolor=color_background, bordercolor="gray30")

	gasBar = ttk.Progressbar(master, style="gasBarTheme.Horizontal.TProgressbar", orient="horizontal", length=360, mode="determinate", maximum=100)
	gasBar.place(x=580, y=455)
	
	def quit():
		master.destroy()
		return True
	
	quitButton = tk.Button(master, text = 'GO BACK TO MENU', width = 70, command = quit, bg='grey', fg='firebrick1', activeforeground="Orange",
						activebackground="blue", font='Aldrich',relief='groove')
	quitButton.place(x=40, y=540)
	

		