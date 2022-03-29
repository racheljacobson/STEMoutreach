import csv
from array import array
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats



# read excel data file, convert to csv
from csvTest import csvData

#read csv file

file=csv.reader(r"C:\Users\Rachel\Documents\nbarookieCSV.csv")

#function to convert excel data to csv, if we are given an excel document
def file_converter(data):
    read_file = pd.read_excel(r"C:\Users\Rachel\Documents\nba rookie data.xlsx", sheet_name="nba rookies",
                              usecols="G:L")
    csvData = read_file.to_csv(r'C:\Users\Rachel\Documents\rookie_csv.csv', index=bool, header=True)
    read = csv.reader(csvData)
    num_students = len(list(read))



# use numpy to convert each column into percentiles
# adds percentile rank as columns into dataframe
def percentile_converter(q, file):
    # sorts values in ascending order
    file['StRank'] = file.usecols = ('F').sort_values(pct=True)
    file['VRank'] = file.usecols = ('G').sort_values(pct=True)
    file['QRank'] = file.usecols = ('H').sort_values(pct=True)
    file['ARank'] = file.usecols = ('I').sort_values(pct=True)
    file['SpRank'] = file.usecols = ('J').sort_values(pct=True)

    columnNames=file.usecols('F:J')
    for (columnName, columnData) in csvData.iteritems():
        name = columnName
        contents = columnData.values
        csvData.sort_values([name],
                            axis=0,
                            ascending=[False],
                            inplace=True)
        my_percentile()

    my_percentile(csvData)

    csvData.sort_values(["Vertical"],
                        axis=0,
                        ascending=[False],
                        inplace=True)
    my_percentile(csvData)

    print(df)
    # prints the table with percentiles
    # use these Percentile Ranks in to plot radar charts


# mathematical function to convert data to percentiles (percentiles determined based only on dataset values)
def my_percentile(data, percentile):
    n = len(data)
    p = n * percentile / 100
    if p.is_integer():
        return sorted(data)[int(p)]
    else:
        return sorted(data)[int(math.ceil(p)) - 1]


def get_userScore():
    strength = input("Enter your strength result: ")
    # convert_scores(strength, )
    percentileSt = stats.percentileofscore(df['StRank'], strength, kind='rank')
    vertical = input("Enter your vertical result: ")
    percentileV = stats.percentileofscore(df['VRank'], vertical, kind='rank')
    quickness = input("Enter your quickness result: ")
    percentileQ = stats.percentileofscore(df['QRank'], quickness, kind='rank')
    agility = input("Enter your agility result: ")
    percentileA = stats.percentileofscore(df['ARank'], agility, kind='rank')
    speed = input("Enter your speed result: ")
    percentileSp = stats.percentileofscore(df['SpRank'], speed, kind='rank')
    array = [percentileSt, percentileV, percentileQ, percentileA, percentileSp]
# graphFunct(array)

# def graphFunct(array):
# insert prince's code for radar plot
