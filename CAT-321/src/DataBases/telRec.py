class telRec:
	#don't forget to fetch before you code!!!
	def __init__(self, dict):
		self.time = dict.get('Time')
		self.lat = dict.get('Latitude')
		self.long = dict.get('Longitude')
		self.alt = dict.get('Altitude')
		self.roll = dict.get('roll')
		self.pitch = dict.get('pitch')	
		self.yaw = dict.get('yaw')	
		self.temp = dict.get('Temperature')
		self.pressure = dict.get('Pressure')
		self.hum = dict.get('Humidity')
		self.FC = 0
		self.everything = dict.values() 

	def __str__(self):
		str = "Telemetry Record: \n"
		str+= "--"*10 
		str += f"\nTime = {self.time}\nLatitude = {self.lat}\nLongitude = {self.long}\n\
		Altitude = {self.alt}\nRoll = {self.roll}\nPitch = {self.pitch}\nYaw = {self.yaw}\n\
		Temperature = {self.temp}\nPressure = {self.pressure}\nHumidity = {self.hum}\n"
		return str
	def __repr__(self):
		str = "Telemetry Record: \n"
		str+= "--"*10 
		str += f"\nTime = {self.time}\nLatitude = {self.lat}\nLongitude = {self.long}\n\
		Altitude = {self.alt}\nRoll = {self.roll}\nPitch = {self.pitch}\nYaw = {self.yaw}\n\
		Temperature = {self.temp}\nPressure = {self.pressure}\nHumidity = {self.hum}\n"
		return str
 
	
#the following methods are all similar, just for different attributes

	def setTime (self, time):
		self.time = time

	def setLatitude (self,lat):
		#dict['latitude'] = lat
		self.lat  = lat 

	def setLongitude (self, lon):	
		#telRec['longitude'] = lon
		self.lon  = lon

	def setAltitude (self,alt):
		#dict['altitude'] = alt
		self.alt = alt

	def setRoll (self,roll):
		#dict['roll'] = roll
		self.roll  = roll

	def setPitch (self,pitch):
		#dict['pitch'] = pitch
		self.pitch  = pitch

	def setYaw (self,yaw):
		#dict['yaw'] = yaw
		self.yaw = yaw 			

	def setTemperature (self,temp):
		#dict['temperature'] = temp
		self.temp  = temp

	def setPressure (self, pressure):
		self.pressure = pressure

	def setHumidity (self,hum):
		#dict['humidity'] = hum
		self.hum  = hum	

	def addFC (self,faultC):
		self.FC = faultC