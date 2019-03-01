from bs4 import BeautifulSoup
import requests
import re
import string

def cleanPrice(text):
    text = ''.join(x for x in text if x in string.printable)
    return text.split("+")[0]

def getSortedPriceObject(allStations):
    stationDict = {}
    
    for station in allStations:
        location    = station['location']
        price       = float(cleanPrice(station["price"]))
        stationDict[location] = price
    
    sortedObj = sorted(stationDict.items(), key = lambda k: k[1])
    return sortedObj

class FuelModule:
    def __init__(self, fuel_type=None):
        if fuel_type is not None:
            self.url    = "https://fuelprice.io/qld/gold-coast/?fuel_type={}&show_stations=1".format(fuel_type)
        else:
            self.url    = "https://fuelprice.io/qld/gold-coast/?fuel_type=ulp91&show_stations=1"
            
        self.r          = requests.get(self.url)
        self.html       = self.r.text


    def createObject(self):
        html                = self.html
        soup                = BeautifulSoup(html, 'html.parser')
        fuelSummary         = soup.find("div", attrs={"id": "fuel-summary"}).text
        lastUpdated         = soup.find("p", attrs={"class": "last-updated clear"}).text.split("Views")[0]
        cheapestNotice      = soup.find("p", attrs={"class": "notice winner clear"}).text
        allStations         = soup.find_all("li", attrs={"class": re.compile(r"^station_brand-\d+$")})
        allStations         = [{"location": station.text.split("$")[0], "price": station.text.split("$")[1]} for station in allStations]

        sortedPriceObject   = getSortedPriceObject(allStations)

        return {
            "summary":          fuelSummary, 
            "last_updated":     lastUpdated, 
            "cheapest_notice":  cheapestNotice,
            "all_stations":     allStations,
            "sorted_prices":    sortedPriceObject
        }