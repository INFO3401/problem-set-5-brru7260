import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def loadAndCleanData(fileName):
    openFile = pd.read_csv(fileName)
    openFile.fillna(value = 0, inplace = True)
    return openFile

def mergeData(df1, df2, column):
    df1[column] = df2[column]
    return df1

def printNewCSV(dataFrame, fileName):
    dataFrame.to_csv(fileName)
    return fileName

def plotTimeline(df, time, val):
    df.plot.line(x = time, y = val)
    plt.show()

def plotMultipleTimelines(df, time, val, cat):
    plt.style.use('ggplot')
    df.plot.line(x = time, y = [val, cat], figsize = (10,7))
    plt.show()