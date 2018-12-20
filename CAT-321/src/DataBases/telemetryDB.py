#from telRec import telRec 
class telemetryDB:

	def __init__(self):
		self.telemetry = []
		self.recordCount = 0

	#We are adding an entire telemetry record each time and also incrementing our counter
	def addRecord(self,telRec):
		self.telemetry.append(telRec)
		self.recordCount += 1

	#this gets the total number of records, or our counter recordCount
	def getNumRec(self):
		return self.recordCount

	#this gives us the most recent record which is in the back of the list
	def getLastRecord(self):
		return self.telemetry[self.recordCount - 1]

	#this allows us to look at any record we want
	def getRecord(self,i):
		return self.telemetry[i]

#def main (): 
#	t = telemetryDB()
#	dic = {} 
#	a = telRec(dic)
#	t.addRecord(a)
#	print(t.getNumRec())
#	print(t.getLastRecord())
#	print(t.getRecord(0))
#main()