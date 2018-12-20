from DataBases.commandBase import CommandBase
from Radio.radio import Radio
from DataBases.command import Command
from DataBases.telRec import telRec
from DataBases.telemetryDB import telemetryDB
import socket
import time
import sys
from termcolor import colored

TCP_IP = '127.0.0.1'
#TCP_IP = 'aerohab.eduroam.gmu.edu'

TCP_PORT = 50001
BUFFER_SIZE = 1024
MESSAGE = "t"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
	#initializes Radio and command dataBase 
	cmdDB = CommandBase()
	teleDB = telemetryDB()
	radio = Radio()
	#Setting up radio call back and initializing the internal dataBase 
	radio.setUP(cmdDB)
	print("Im here")
	# open socket for tcpclient 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connectServer(); 

	while(True):
		try:
			if(cmdDB.isEmpty() == False): 
				command = cmdDB.getCommand() #get a fresh command
				#execute command

			# get position in intervals 
			s.send(MESSAGE) 
			data = s.recv(BUFFER_SIZE) #recieves sata 
			teleDB.append(parseData(data)) # save in data base 
			radio.send(data)

			# send last record in intervals

		except (KeyboardInterrupt, socket.error):
			print("terminated") # close Xbee connection 
			radio.terminate()
			try:
					print("terminated") # close Xbee connection 
					radio.terminate()
					s.send("close")
					s.close()
					print (colored("Connection closed",'red'))
					sys.exit()
			except socket.error:
				s.close()
				print (colored("Connection closed unexpectedly. Check Server state...",'red'))
				sys.exit()

def connectServer():
	try:
		s.connect((TCP_IP, TCP_PORT))
	except:
		print (colored("Connection refused to (" + str(TCP_IP) + "," + str(TCP_PORT) + ").", 'red'))
		sys.exit()

def parseData():
	dictionary= {} 
	sensorData = sensorData.split(",")
	time = sensorData[0]
	dictionary[keys[0]] = time
	keys.pop(0) 	
	sensorData.pop(0) 
	i = 0 
	while i < len(sensorData):
		number = sensorData[i]
		if(number != "n/a"):
			dictionary[keys[i]] = float(sensorData[i])
		else: 
			dictionary[keys[i]] = None
		i+= 1
	return telRec(dictionary)

main()

