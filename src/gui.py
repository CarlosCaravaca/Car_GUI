import tkinter as tk
from tkinter import ttk
from cfg import *

'''
GUI
'''
#Root window
root = tk.Tk()
root.title("Car System")
root.geometry("540x360")
root.attributes('-fullscreen', False)
root.configure(background=color_background)

# Title Bar
#----------------------------------------------------------

#Title Bar
logoImage = tk.PhotoImage(file=logo_path)
logoLabel = tk.Label(image=logoImage)
logoLabel.place(x=6, y=8, height=36, width=36)

#Make title
#titleLabel1 = tk.Label(root, fg=color_make, bg=color_background, font=("Aldrich", 20), text=make)
#titleLabel1.place(x=42, y=8)

#Model title
titleLabel2 = tk.Label(root, fg=color_model, bg=color_background, font=("Aldrich", 14), text=model)
titleLabel2.place(x=42, y=14)

#Time title
timeLabel = tk.Label(root, fg=color_time, bg=color_background, font=("Aldrich", 16), text="00:00:00")
timeLabel.place(x=376, y=12)

#Status title
statusLabel = tk.Label(root, fg=color_status, bg=color_background, font=("Aldrich", 16), text="NOT_CONNECTED")
statusLabel.place(x=6, y=300)

# Pi Labels
#----------------------------------------------------------

piLabel = tk.Label(root, fg=color_pi, bg=color_background, font=("Aldrich", 16), text="Pi:")
piLabel.place(x=220, y=300)

pitempLabel = tk.Label(root, fg=color_temp, bg=color_background, font=("Aldrich", 16), text="0")
pitempLabel.place(x=280, y=300)
pitempxLabel = tk.Label(root, fg=color_c, bg=color_background, font=("Aldrich", 16), text='ºC')
pitempxLabel.place(x=310, y=300)

piclockLabel = tk.Label(root, fg=color_clock, bg=color_background, font=("Aldrich", 16), text="0")
piclockLabel.place(x=350, y=300)
piclockxLabel = tk.Label(root, fg=color_mhz, bg=color_background, font=("Aldrich", 16), text="MHz")
piclockxLabel.place(x=420, y=300)

# Left Labels
#----------------------------------------------------------

batteryLabel = tk.Label(root, fg=color_labels, bg=color_background, font=("Aldrich", 14), text="Voltaje:")
batteryLabel.place(x=labelsX, y=48)
batteryPercentageLabel = tk.Label(root, fg=color_values, bg=color_background, font=("Aldrich", 14), text="... V")
batteryPercentageLabel.place(x=valuesX, y=48)

waterLabel = tk.Label(root, fg=color_labels, bg=color_background, font=("Aldrich", 14), text="T. Refrigerante:")
waterLabel.place(x=labelsX, y=72)
waterPercentageLabel = tk.Label(root, fg=color_values, bg=color_background, font=("Aldrich", 14), text="... "+'ªC')
waterPercentageLabel.place(x=valuesX, y=72)

airLabel = tk.Label(root, fg=color_labels, bg=color_background, font=("Aldrich", 14), text="T. Entrada Aire:")
airLabel.place(x=labelsX, y=96)
airPercentageLabel = tk.Label(root, fg=color_values, bg=color_background, font=("Aldrich", 14), text="... "+'ºC')
airPercentageLabel.place(x=valuesX, y=96)

airflowLabel = tk.Label(root, fg=color_labels, bg=color_background, font=("Aldrich", 14), text="Caudal de aire:")
airflowLabel.place(x=labelsX, y=120)
airflowPercentageLabel = tk.Label(root, fg=color_values, bg=color_background, font=("Aldrich", 14), text="... g/s")
airflowPercentageLabel.place(x=valuesX, y=120)

lambdaLabel1 = tk.Label(root, fg=color_labels, bg=color_background, font=("Aldrich", 14), text="Lambda 1:")
lambdaLabel1.place(x=labelsX, y=144)
lambdaPercentageLabel1 = tk.Label(root, fg=color_values, bg=color_background, font=("Aldrich", 14), text="... mV")
lambdaPercentageLabel1.place(x=valuesX, y=144)

lambdaLabel2 = tk.Label(root, fg=color_labels, bg=color_background, font=("Aldrich", 14), text="Lambda 2:")
lambdaLabel2.place(x=labelsX, y=168)
lambdaPercentageLabel2 = tk.Label(root, fg=color_values, bg=color_background, font=("Aldrich", 14), text="... mV")
lambdaPercentageLabel2.place(x=valuesX, y=168)

ignitionLabel = tk.Label(root, fg=color_labels, bg=color_background, font=("Aldrich", 12), text="Avance encendido:")
ignitionLabel.place(x=labelsX, y=192)
ignitionPercentageLabel = tk.Label(root, fg=color_values, bg=color_background, font=("Aldrich", 14), text="... "+'º')
ignitionPercentageLabel.place(x=valuesX, y=192)

loadLabel = tk.Label(root, fg=color_labels, bg=color_background, font=("Aldrich", 16), text="Carga motor:")
loadLabel.place(x=labelsX, y=228)
loadPercentageLabel = tk.Label(root, fg=color_values, bg=color_background, font=("Aldrich", 16), text="... %")
loadPercentageLabel.place(x=valuesX, y=228)

gasLabel = tk.Label(root, fg=color_labels, bg=color_background, font=("Aldrich", 16), text="Acelerador:")
gasLabel.place(x=labelsX, y=260)
gasPercentageLabel = tk.Label(root, fg=color_values, bg=color_background, font=("Aldrich", 16), text="... %")
gasPercentageLabel.place(x=valuesX, y=260)

# Left Labels
#----------------------------------------------------------

speedLabel = tk.Label(root, fg=color_speed, bg=color_background, font=("Aldrich", 32), text="0")
speedLabel.place(x=280, y=48)
kmhLabel = tk.Label(root, fg=color_kmh, bg=color_background, font=("Aldrich", 32), text="km/h")
kmhLabel.place(x=370, y=48)

revsLabel = tk.Label(root, fg=color_revs, bg=color_background, font=("Aldrich", 20), text="0")
revsLabel.place(x=280, y=96)
uminLabel = tk.Label(root, fg=color_umin, bg=color_background, font=("Aldrich", 20), text="rpm")
uminLabel.place(x=370, y=96)

# Gauges
#----------------------------------------------------------

#speedGauge = tk.Canvas(root, bg=color_background, width=180, height=200)
#speedGauge.place(x=680, y=140)
#speedGauge.create_arc(10, 10, 170, 190, style="arc", width=20, start=-10, extent=170, outline=color_speed, tags=('arc2'))
#speedGauge.create_arc(10, 10, 170, 190, style="arc", width=20, start=160, extent=20, outline=color_speed, tags=('arc1'))

#polyPoints = [(100, 40), (110, 100), (100, 110), (90, 100)]
#polyNeedle = speedGauge.create_polygon(polyPoints, fill='white')

# Bars
#----------------------------------------------------------


lambdaBarsLabel = tk.Label(root, fg=color_lambda_h, bg=color_background, font=("Aldrich", 12), text="Aire/Gasolina:")
lambdaBarsLabel.place(x=280, y=130)
lambdaBarsLabel2 = tk.Label(root, fg=color_lambda_f, bg=color_background, font=("Aldrich", 12), text="Pobre                  Rico")
lambdaBarsLabel2.place(x=280, y=196)

lambda1BarCanvas = tk.Canvas(root, bg=color_background, width=180, height=12, borderwidth=0, highlightthickness=0)
lambda1BarCanvas.create_rectangle(0, 2, 40, 10, fill=color_lambda_1bad)
lambda1BarCanvas.create_rectangle(30, 2, 70, 10, fill=color_lambda_1okay)
lambda1BarCanvas.create_rectangle(70, 2, 110, 10, fill=color_lambda_1good)
lambda1BarCanvas.create_rectangle(110, 2, 150, 10, fill=color_lambda_1okay)
lambda1BarCanvas.create_rectangle(150, 2, 180, 10, fill=color_lambda_1bad)
lambda1Pointer = lambda1BarCanvas.create_rectangle(88, 0, 92, 11, fill='white')
lambda1BarCanvas.place(x=280, y=154 + 1)

lambda2BarCanvas = tk.Canvas(root, bg=color_background, width=180, height=12, borderwidth=0, highlightthickness=0)
lambda2BarCanvas.create_rectangle(0, 2, 40, 10, fill=color_lambda_2bad)
lambda2BarCanvas.create_rectangle(30, 2, 70, 10, fill=color_lambda_2okay)
lambda2BarCanvas.create_rectangle(70, 2, 110, 10, fill=color_lambda_2good)
lambda2BarCanvas.create_rectangle(110, 2, 150, 10, fill=color_lambda_2okay)
lambda2BarCanvas.create_rectangle(150, 2, 180, 10, fill=color_lambda_2bad)
lambda2Pointer = lambda2BarCanvas.create_rectangle(88, 0, 92, 11, fill='white')
lambda2BarCanvas.place(x=280, y=178 + 1)

gasLoadTheme = ttk.Style()
gasLoadTheme.theme_use('clam')
gasLoadTheme.configure("loadBarTheme.Horizontal.TProgressbar", background=color_load_bar, troughcolor=color_background, bordercolor="gray30")

loadBar = ttk.Progressbar(root, style="loadBarTheme.Horizontal.TProgressbar", orient="horizontal", length=180, mode="determinate", maximum=100)
loadBar.place(x=280, y=228)

gasBarTheme = ttk.Style()
gasBarTheme.theme_use('clam')
gasBarTheme.configure("gasBarTheme.Horizontal.TProgressbar", background=color_gas_bar, troughcolor=color_background, bordercolor="gray30")

gasBar = ttk.Progressbar(root, style="gasBarTheme.Horizontal.TProgressbar", orient="horizontal", length=180, mode="determinate", maximum=100)
gasBar.place(x=280, y=260)