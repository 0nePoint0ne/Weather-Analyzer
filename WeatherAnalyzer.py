import re
import xml.etree.ElementTree as ET

class dailyWeather:
	def __init__(self, day, month, year, maxTemp, minTemp, meanTemp, heatDegDays, coolDegDays, totalRain, totalSnow, totalPrecipitation, snowOnGround):
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
		#self.displayData()
	def displayData(self):
		data = ''
		data = "The Date is " + str(self.year) + "/" + str(self.month) + "/" + str(self.day) + "  Max Temp: " + str(self.maxTemp) + " Min Temp: " + str(self.minTemp) 
		return data
		
def printData(args):
	file = open("data.txt", "w")
	for day in args:
		data = day.displayData()
		file.write(data + "\n")
	file.close

		
def main():
	yearsWeather = []

	tree = ET.parse('data.xml')
	root = tree.getroot()
	for child in root:
		if(str(child.tag) == 'stationdata'):
			#print( str(child.tag) + " " + str(child.attrib) +  " " + str(child.attrib['day']))
			yearsWeather.append(dailyWeather(child.attrib['day'], child.attrib['month'], child.attrib['year'], child[0].text,child[1].text,child[2].text,child[3].text,child[4].text,child[5].text,child[6].text,child[7].text,child[8].text))
	
	for day in yearsWeather:
		day.displayData()
		
	printData(yearsWeather)
main()