import pandas as pd
import re
import xml.etree.ElementTree as ET

dataset = []
index = []

class monthWeather:
	def __init__(self, month, year, maxTemp, minTemp, meanTemp, heatDegDays, coolDegDays, totalRain, totalSnow, totalPrecipitation, snowOnGround):

		if(int(month) < 10):
			self.month = "0" + str(month)
		else:
			self.month = str(month)
		
		#self.month = month
		self.year = year
		self.maxTemp = maxTemp
		self.minTemp = minTemp
		self.meanTemp = meanTemp
		self.heatDegDays = heatDegDays
		self.coolDegDays = coolDegDays
		if(totalRain == None):
			self.totalRain = 0.0
		else:
			self.totalRain = totalRain
		if(totalSnow == None):
			self.totalSnow = 0.0
		else:
			self.totalSnow = totalSnow
		if(totalPrecipitation == None):
			self.totalPrecipitation = 0.0
		else:
			self.totalPrecipitation = totalPrecipitation
		if(snowOnGround == None):
			self.snowOnGround = 0
		else:
			self.snowOnGround = snowOnGround
		
		#self.displayData()
	def displayData(self):
		strdata = ''
		data = "The Date is " + str(self.year) + "/" + str(self.month) + "/" + str(self.day) + "  Max Temp: " + str(self.maxTemp) + " Min Temp: " + str(self.minTemp) 
		return strdata

class dailyWeather:
	def __init__(self, day, month, year, maxTemp, minTemp, meanTemp, heatDegDays, coolDegDays, totalRain, totalSnow, totalPrecipitation, snowOnGround):
		if(int(day) < 10):
			self.day = "0" + str(day)
		else:
			self.day = str(day)
			
		#self.day = day
		if(int(month) < 10):
			self.month = "0" + str(month)
		else:
			self.month = str(month)
		
		#self.month = month
		self.year = year
		self.maxTemp = maxTemp
		self.minTemp = minTemp
		self.meanTemp = meanTemp
		self.heatDegDays = heatDegDays
		self.coolDegDays = coolDegDays
		if(totalRain == None):
			self.totalRain = 0.0
		else:
			self.totalRain = totalRain
		if(totalSnow == None):
			self.totalSnow = 0.0
		else:
			self.totalSnow = totalSnow
		if(totalPrecipitation == None):
			self.totalPrecipitation = 0.0
		else:
			self.totalPrecipitation = totalPrecipitation
		if(snowOnGround == None):
			self.snowOnGround = 0
		else:
			self.snowOnGround = snowOnGround
		
		#self.displayData()
	def displayData(self):
		strdata = ''
		data = "The Date is " + str(self.year) + "/" + str(self.month) + "/" + str(self.day) + "  Max Temp: " + str(self.maxTemp) + " Min Temp: " + str(self.minTemp) 
		return strdata
		
def storeData(year):
	file = open("data.text", "w")

	for day in year:
		
		dataset.append({'Max Temp:': float(day.maxTemp),'Min Temp:': float(day.minTemp), 'Mean Temp:': day.meanTemp, 'Total Rain:': day.totalRain, 'Total Snow:': day.totalSnow, 'Total Percipitation:': day.totalPrecipitation, 'Snow On Ground:': day.snowOnGround})
		index.append(str(day.year + "-" + day.month + "-" + day.day))
	
	#print(dataset[2])
	df = pd.DataFrame(dataset, index)

	df.to_csv("data.csv")
	#print(df.to_string())
	file.write(str(df.to_string()))
	file.close
	
def monthlySummary(year):
	temp = {}
	
	file = open("dataSummary.txt","w")
	value = -1
	for data in dataset:
		temp = data
		
		print(index[value])
	#print(dataset)
	#print(dataset['Max Temp:'])
 
	#file.write(str(df))
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
	storeData(yearsWeather)
	monthlySummary(yearsWeather)
	
	
main()