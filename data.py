import statistics
from settings import *


def readFileData(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            dataArray = f.read().split("\n")
        xArray = []
        yArray = []
        for line in dataArray:
            if len(line) > 1:
                x, y = line.split(",")
                xArray.append(float(x))
                yArray.append(float(y))
        return xArray, yArray
    except FileNotFoundError:
        return [], []


# Apply filters to the data
def getDataToShow(file):
    xArray, yArray = readFileData(file)
    filtered_x = xArray
    filtered_y = movingMedianFilter(yArray)
    return filtered_x, filtered_y


# Verandert de waarde door het gemiddelde van de 3 rond hem: i ->  avg(i-1, i, i+1) -> BESTE VOOR RUIS
def averageFilter(data, windowSize=3):
    if len(data) < windowSize:
        return data
    result = []
    for i in range(len(data)):
        start = max(0, i - windowSize // 2)
        end = min(len(data), i + windowSize // 2 + 1)
        window = data[start:end]
        result.append(sum(window) / len(window))
    return result


# Verandert de waarde door de mediaan van de 3 rond hem: i -> med(i-1, i, i+1) -> BESTE VOOR PIEKEN
def movingMedianFilter(data, windowSize=3):
    if len(data) < windowSize:
        return data
    result = []
    for i in range(len(data)):
        start = max(0, i - windowSize + 1)
        end = i + 1
        window = data[start:end]
        result.append(statistics.median(window))
    return result
