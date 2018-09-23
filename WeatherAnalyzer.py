import pandas as pd
import re
import xml.etree.ElementTree as ET

dataset = []
index = []

class dailyWeather:
	def __init__(self, day, month, year, maxTemp, minTemp, meanTemp, heatDegDays, coolDegDays, totalRain, totalSnow, totalPrecipitation, snowOnGround):
		if(int(day) < 10):
			self.day = "0" + str(day)
		else:
			self.day = str(day)
		
		#self.day = int(day)
		if(int(month) < 10):
			self.month = "0" + str(month)
		else:
			self.month = str(month)
		
		#self.month = month
		self.year = year
		self.maxTemp = float(maxTemp)
		self.minTemp = float(minTemp)
		self.meanTemp = float(meanTemp)
		self.heatDegDays = heatDegDays
		self.coolDegDays = coolDegDays
		if(totalRain == None):
			self.totalRain = 0.0
		else:
			self.totalRain = float(totalRain)
		if(totalSnow == None):
			self.totalSnow = 0.0
		else:
			self.totalSnow = float(totalSnow)
		if(totalPrecipitation == None):
			self.totalPrecipitation = 0.0
		else:
			self.totalPrecipitation = float(totalPrecipitation)
		if(snowOnGround == None):
			self.snowOnGround = 0
		else:
			self.snowOnGround = float(snowOnGround)
		
		#self.displayData()
	def displayData(self):
		strdata = ''
		data = "The Date is " + str(self.year) + "/" + str(self.month) + "/" + str(self.day) + "  Max Temp: " + str(self.maxTemp) + " Min Temp: " + str(self.minTemp) 
		return strdata
		
def storeData(year):
	file = open("data.txt", "w")

	for day in year:
		
		dataset.append({'Year:': day.year ,'Month:': day.month, 'Day:': day.day ,'Max Temp:': float(day.maxTemp),'Min Temp:': float(day.minTemp), 'Mean Temp:': day.meanTemp, 'Total Rain:': day.totalRain, 'Total Snow:': day.totalSnow, 'Total Percipitation:': day.totalPrecipitation, 'Snow On Ground:': day.snowOnGround})
		#index.append(str(day.year + "-" + day.month + "-" + day.day))
	
	
	
	
	df = pd.DataFrame(dataset)
	
	df['TimeStamp:'] = df['Year:'] + '/' + df['Month:'] + '-' + df['Day:']
	
	
	
	print(df[['TimeStamp:','Max Temp:', 'Min Temp:', 'Mean Temp:', 'Total Rain:', 'Total Snow:', 'Total Percipitation:', 'Snow On Ground:' ]].to_string(index = False))
	file.write(str(df.to_string(index = False)))
	file.close
	df.to_csv('year.csv')
	
def monthlySummary(year):
	file = open("dataSummary.txt","w")

	
	months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	df = pd.DataFrame(dataset)
	df['TimeStamp:'] = df['Year:'] + '/' + df['Month:']
	#df['Average Temp:'] = df.groupby(['Max Temp:', 'Min Temp:']).apply(lambda x: x['ID_2'].sum()/len(x))
	
	
	monthlySummary = {'Month:': months, 'Highest Temp:': df.groupby('Month:')['Max Temp:'].max(),'Lowest Temp:': df.groupby('Month:')['Min Temp:'].min(), 'Total Monthly Rain:': df.groupby('Month:')['Total Rain:'].sum(), 'Total Monthly Snow:': df.groupby('Month:')['Total Snow:'].sum(), 'Total Monthly Percipitation:': df.groupby('Month:')['Total Percipitation:'].sum()}
	sdf = pd.DataFrame(monthlySummary)
	
	
	print(sdf.to_string(index = False))
	

	file.write(str(sdf.to_string(index = False)))
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