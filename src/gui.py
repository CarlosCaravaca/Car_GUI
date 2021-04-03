import tkinter as tk
from tkinter import ttk
from cfg import *
from PIL import Image, ImageTk
import obd
import time
import datetime
import os
import subprocess
import json

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
	
	obd.logger.setLevel(obd.logging.ERROR)

	connectionStatus = obd.OBDStatus.NOT_CONNECTED
	connection = None
	
	logValuesToFile = True
	logFileName = "/home/pi/obd2_values.txt"
	
	# Custom ELM-Voltage parser & command for my module
	def elmVoltageCustom(messages):
		return messages[0].frames[0].raw.lower().split('v')[0].replace('v', '')

	voltagecmd = obd.OBDCommand("ELM_VOLTAGECUSTOM", "Voltage custom", b"ATRV", 0, elmVoltageCustom, obd.ECU.UNKNOWN, False)
	
	class CarData:
		def __init__(self, connectionStatus, batteryVoltage, coolantTemperature, intakeTemperature, intakeAirflow, lambdaVoltage1, lambdaVoltage2, timingAdvance, engineLoad, throttle, speed, rpm):
			self.timestamp = int(round(time.time() * 1000))
			self.connectionStatus = connectionStatus
			self.batteryVoltage = batteryVoltage
			self.coolantTemperature = coolantTemperature
			self.intakeTemperature = intakeTemperature
			self.intakeAirflow = intakeAirflow
			self.lambdaVoltage1 = lambdaVoltage1
			self.lambdaVoltage2 = lambdaVoltage2
			self.timingAdvance = timingAdvance
			self.engineLoad = engineLoad
			self.throttle = throttle
			self.speed = speed
			self.rpm = rpm
		
	def QueryAndParseResultSpace(connection, cmd, roundDecimals):
		try:
			result = 0
			rawResult = connection.query(cmd)
	
			if rawResult != None and str(rawResult) != "None" and str(rawResult.value) != "atr":
				try:
					splittedStuff = str(rawResult.value)
					result = round(float(splittedStuff), roundDecimals)
			
					if roundDecimals is 0:
						result = int(result)
				except Exception as ex:
					print("Error: " + str(ex)) 
					result = -1
			else:
				print("[" + str(cmd) + "] No value received...")
				result = 0
			
		except Exception as excep:
			print("Error: " + str(excep))
			result = -1
		return result
	
	def CalculateLambdaPointerPosition(currentLambda, maxX, maxY, pointerWidth):
		finalPos = int(maxX / 2) - pointerWidth, 0, int(maxX / 2) + pointerWidth, 12
	
		try:
			lambdaPercent = float(currentLambda) / 1.0
			finalPos = (maxX * lambdaPercent) - pointerWidth, 0, (maxX * lambdaPercent) + pointerWidth, 12
		except:
			pass
	
		return finalPos
	
	def uiUpdate():
		global connectionStatus
		global connection
	
		#print("Updating UI...")
	
		time = datetime.datetime.now() + datetime.timedelta(hours=1)
		timeLabel.config(text=time.strftime("%H:%M:%S"))
	
		temp = subprocess.run(['cat', '/sys/class/thermal/thermal_zone0/temp'], stdout=subprocess.PIPE).stdout.decode('utf-8')
		pitempLabel.config(text=round(int(temp)/1000))
	
		clock = subprocess.run(['cat', '/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq'], stdout=subprocess.PIPE).stdout.decode('utf-8')
		piclockLabel.config(text=round(int(clock)/1000))
	
		if connection is not None:
			connectionStatus = connection.status()
			statusLabel.config(text=connectionStatus)
	
		# if we aren't connected, try to connect and add our custom voltage cmd
		if connectionStatus is obd.OBDStatus.NOT_CONNECTED or connection is None:
			connection = obd.OBD()
			connection.supported_commands.add(voltagecmd)
		
		if connectionStatus is obd.OBDStatus.CAR_CONNECTED:
			currentCarData = CarData(
				connectionStatus,
				QueryAndParseResultSpace(connection, voltagecmd, 2),
				QueryAndParseResultSpace(connection, obd.commands.COOLANT_TEMP, 0),
				QueryAndParseResultSpace(connection, obd.commands.INTAKE_TEMP, 0),
				QueryAndParseResultSpace(connection, obd.commands.MAF, 0),
				QueryAndParseResultSpace(connection, obd.commands.O2_B1S1, 2),
				QueryAndParseResultSpace(connection, obd.commands.O2_B1S2, 2),
				QueryAndParseResultSpace(connection, obd.commands.TIMING_ADVANCE, 2),
				QueryAndParseResultSpace(connection, obd.commands.ENGINE_LOAD, 0),
				QueryAndParseResultSpace(connection, obd.commands.THROTTLE_POS, 0),
				QueryAndParseResultSpace(connection, obd.commands.SPEED, 0),
				QueryAndParseResultSpace(connection, obd.commands.RPM, 0)
			)
		else:
			if connectionStatus is obd.OBDStatus.OBD_CONNECTED:
				currentCarData = CarData(connectionStatus, QueryAndParseResultSpace(connection, voltagecmd, 2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
			else:
				currentCarData = CarData(connectionStatus, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
	
		batteryPercentageLabel.config(text=str(currentCarData.batteryVoltage) + " V")
		waterPercentageLabel.config(text=str(currentCarData.coolantTemperature) +'ºC')
		airPercentageLabel.config(text=str(currentCarData.intakeTemperature) + 'ºC')
		airflowPercentageLabel.config(text=str(currentCarData.intakeAirflow) + " g/s")
		lambdaPercentageLabel1.config(text=str(currentCarData.lambdaVoltage1) + " mV")
		lambdaPercentageLabel2.config(text=str(currentCarData.lambdaVoltage2) + " mV")
		ignitionPercentageLabel.config(text=str(currentCarData.timingAdvance) + 'º')
		loadPercentageLabel.config(text=str(currentCarData.engineLoad) + " %")
		gasPercentageLabel.config(text=str(currentCarData.throttle) + " %")
		speedLabel.config(text=str(currentCarData.speed))
		revsLabel.config(text=str(currentCarData.rpm))
	
		loadBar["value"] = currentCarData.engineLoad
		gasBar["value"] = currentCarData.throttle
	
		lambdaPointer1Pos = CalculateLambdaPointerPosition(currentCarData.lambdaVoltage1, 180, 12)
		lambdaPointer2Pos = CalculateLambdaPointerPosition(currentCarData.lambdaVoltage2, 180, 12)
	
		lambda1BarCanvas.coords(lambda1Pointer, lambdaPointer1Pos[0], lambdaPointer1Pos[1], lambdaPointer1Pos[2], lambdaPointer1Pos[3],)
		lambda2BarCanvas.coords(lambda2Pointer, lambdaPointer2Pos[0], lambdaPointer2Pos[1], lambdaPointer2Pos[2], lambdaPointer2Pos[3],)
	
		# log data
		if logValuesToFile:
			with open(logFileName, "a") as logfile:
				logfile.write(json.dumps(currentCarData.__dict__) + "\n")
	
		master.after(250, uiUpdate)

	
	def quit():
		master.destroy()
		return True
	
	quitButton = tk.Button(master, text = 'GO BACK TO MENU', width = 70, command = quit, bg='grey', fg='firebrick1', activeforeground="Orange",
						activebackground="blue", font='Aldrich',relief='groove')
	quitButton.place(x=40, y=540)
	
	os.system("xset s off")
	os.system("xset dpms 0 0 0")
	os.system("xset -dpms s off")

	# hide the cursor
	os.system("unclutter &")

	uiUpdate()
	

		