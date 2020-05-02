import pandas as pd
import pprint as pprint
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

def correctDateFormatConfirmed(dataFrame):
    dataFrame = dataFrame.melt(id_vars = dataFrame.columns[0:4], var_name = "Date", value_name = "Confirmed")
    dataFrame["Date"] = pd.to_datetime(dataFrame["Date"])
    return dataFrame

def correctDateFormatDeaths(dataFrame):
    dataFrame = dataFrame.melt(id_vars = dataFrame.columns[0:4], var_name = "Date", value_name = "Deaths")
    dataFrame["Date"] = pd.to_datetime(dataFrame["Date"])
    return dataFrame

def correctDateFormatRecovered(dataFrame):
    dataFrame = dataFrame.melt(id_vars = dataFrame.columns[0:4], var_name = "Date", value_name = "Recovered")
    dataFrame["Date"] = pd.to_datetime(dataFrame["Date"])
    return dataFrame

def aggregateCountry(df, column, country):
    data = df.loc[df["Country/Region"] == country]
    countryData = data.groupby("Date", as_index = False).sum()
    return countryData[column]

def computeCorrelation(candidate1, candidate2):
    return candidate1.corr(candidate2)

def getUnique(dupList):
   checked = []
   for i in dupList:
       if i not in checked:
           checked.append(i)
   return checked


def topCorrelations(df, column, n):
    countries = df["Country/Region"]
    countries = getUnique(countries)
    countryCorrs = {}
    i=0
    while (i < len(countries)):
        count1 = countries[i]
        count1Data = aggregateCountry(df, column, count1)
        j=i+1
        while(j < len(countries)):
            count2 = countries[j]
            count2Data = aggregateCountry(df, column, count2)
            corr = computeCorrelation(count1Data, count2Data)
            name = count1 + " vs " + count2
            countryCorrs[name] = corr
            j+=1
        i+=1
    sortedCorrs = {k: v for k, v in sorted(countryCorrs.items(), key=lambda item: item[1])}
    print(sortedCorrs)