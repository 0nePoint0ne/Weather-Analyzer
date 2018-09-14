import re
class dailyWeather:
	def __init__(self, day, month, year, maxTemp, minTemp, meanTemp, heatDegDays, coolDegDays, totalRain, totalSnow, totalPrecipitation, snowOnGround, dirOfMaxGust, speedOfMaxGust):
		self.day = day
		self.month = month
		self.year = year
		self.maxTemp = maxTemp
		self.minTemp = minTemp
		self.meanTemp = meanTemp
		self.heatDegDays = heatDegDays
		self.coolDegDays = coolDegDays
		self.totalRain = totalRain
		self.totalSnow = totalSnow
		self.totalPrecipitation = totalPrecipitation
		self.snowOnGround = snowOnGround
		self.dirOfMaxGust = dirOfMaxGust
		self.speedOfMaxGust = speedOfMaxGust
		
def main():
	status = 0
	da = ''
	file = open("eng-daily-01012017-12312017.xml", "r")
	data = file.read()
	text = data.split('<stationdata ')
	#print(file.read())
	yearsWeather = []
	for i in range(365):
		yearsWeather.append(dailyWeather(1, 2, 3, 0,2,3,4,5,6,7,8,9,10,11))
	for ob in text[3:4]:
		print(" ")
		#print(ob)
		print(" ")
		newText = ''
		x = 0
		for x in range(len(ob)):
			
			if(status == 1):
				if(ob[x] == '>' or ob[x] == '<' or ob[x] == '"'):
					status = 0
				elif(ob[x] != '>' or ob[x] != '<' or ob[x] != '"'):
					newText += ob[x]
			elif(status == 0):
				if(ob[x] == '>' or ob[x] == '<' or ob[x] == '"'):
					status = 1
					newText += " "
		
		da = newText.split(" ")
		for a in da:
			print(a)
			#print(ob.find("Maximum Temperature"))
	#	print(newText)
		print(" ")
main()