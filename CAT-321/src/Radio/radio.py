from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
import serial 

# make other folders visible: 
import sys
sys.path.append('../')

# our own modules: 
from DataBases.commandBase import CommandBase
from DataBases.command import Command

# send data 
# questions to decide on 
# are we doing broadcast or unicast
# broadcast will send to all xbee devices
# unary will be one to one requires to instantiate a remoteXbee 
#  remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20040XXXXXX"))
# use device.send_data(remote_device, data)

# synchronus: This means the method waits until the transmit status response is received
# asynchronous: application does not block during the transmit process. send_data_async()

#The idea for the callback is to add the command to the command database every time a message is recieved 

#This code will be run when an xbee_message has been recieved 

#commandDB = None 

class Radio:
	#commandDB where all commands will be stored 
	commandDB = None ; 
	def __init__(self):
		self.serialPort = "/dev/tty.SLAB_USBtoUART" # port where Xbee is connected find by doing ls /dev/tty* on terminal	
		self.device = XBeeDevice(self.serialPort,9600)
		self.remote_device = RemoteXBeeDevice(self.device, XBee64BitAddress.from_hex_string("0013A200406343f7")) # "0013A20040XXXXXX"
		self.callback = None; # strores a reference to the radio callback function 


	def __repr__(self):
		return "Xbee Device at Port {0}\nopen = {1}".format(self.serialPort,self.device.is_open())
	def __str__(self):
		return "Xbee Device at Port {0}\nopen = {1}".format(self.serialPort,self.device.is_open())

	def openConnection(self):
		if (self.device != None and self.device.is_open() == False):
			self.device.open()
		

	def closeConnection(self):
		if (self.device != None and self.device.is_open()):
			self.device.close()
	

	def send(self, data):
		try:
			#self.openConnection()
			#self.device.send_data_broadcast(data)
			#self.device.send_data(self.remote_device,data)
			self.device.send_data_async(self.remote_device,data) #sent async
		except(KeyboardInterrupt): 
			print("something went wrong when sending data")



	def my_data_received_callback(xbee_message):
		address = xbee_message.remote_device.get_64bit_addr()
		data = xbee_message.data.decode("utf8")
		#store the XBbee into a command object for decoding etc...
		command = Command(xbee_message)
		# add this command to the command dataBase
		Radio.commandDB.addCommand(command)
		print("Received data from %s: %s" % (address, data))

	# opens the xbee device and sets the recieve call back 
	# parameters: database = command database to store commands 
	def setUP(self, database):
		Radio.commandDB = database
		self.openConnection()
		self.callback = Radio.my_data_received_callback
		self.device.add_data_received_callback(self.callback)


	#close xbeeconnection and delete callback 
	def terminate(self):
		#self.device.del_data_received_callback(self.callback)
		self.closeConnection()
