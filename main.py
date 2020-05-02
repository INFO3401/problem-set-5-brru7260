from utils import *
from covid import *

globalConfirmed = loadAndCleanData("confirmedGlobal.csv")
confirmed = correctDateFormatConfirmed(globalConfirmed)
#print(confirmed)

globalDeaths = loadAndCleanData("deathsGlobal.csv")
deaths = correctDateFormatDeaths(globalDeaths)

globalRecovered = loadAndCleanData("recoveredGlobal.csv")
recovered = correctDateFormatRecovered(globalRecovered)

globalData = mergeData(confirmed, recovered, "Recovered")
globalData = mergeData(globalData, deaths, "Deaths")

topCorrelations(globalData, "", 5)