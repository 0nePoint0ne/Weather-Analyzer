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
	
	df = pd.DataFrame(dataset, index)
	file.write(str(df.to_string()))
	file.close
	
def monthlySummary(year):
	monthlySummaryData = []
	
	file = open("dataSummary.txt","w")
	
	for x in range(len(dataset)):
		data = dataset[x - 1]

		if(int(index[x-1][5:7])):
			print(index[x-1][8:10] + " " +  str(data['Max Temp:']))
		
		
			
		#monthlySummaryData.append({'Highest Temp:': 0.0 ,'Lowest Temp:': 0.0, 'Total Monthly Snow:': 0.0, 'Total Monthly Rain:': 0.0, 'Total Monthly Percipitation:':0.0, 'Total Monthly Snow:': 0.0, 'Monthly Snow On Ground:': 0.0})
	#print(dataset)
	#print(dataset['Max Temp:'])
	
	

	
	#for i in monthlySummaryData:
		#print(i)
	
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