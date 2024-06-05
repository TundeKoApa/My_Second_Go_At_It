#data project practice with PANDAS Module
# import statistics
# print(statistics.stdev([1,7,5,8]))
#data variable/ an array
# cumulativeRev = ()
# productCat = ()


# import statistics
#data variable

import pandas as pd
def MeanMedianStDev(list):
    df = pd.DataFrame(list)
    # print(df)
    print("Mean, Median, St.Deviation: ",
    df.mean(numeric_only=True), df.median(numeric_only=True),df.std(numeric_only=True))
    print()

    # df = pd.DataFrame(list)
    # print(list, "Median: ", df.median(numeric_only=True))
    # print()
    # df = pd.DataFrame(list)
    # print(list, "Standard Deviation: ", df.std(numeric_only=True))
    # print()
    # df = pd.DataFrame(spring)
    # print("Spring Median: ", df.median(numeric_only=True))
    # print()
    # df = pd.DataFrame(fall)
    # print("Fall Standard Deviation: ", df.std(numeric_only=True))
    # print()
    # df = pd.DataFrame(spring)
    # print("Spring Standard Deviation: ", df.std(numeric_only=True))

spring = []
fall = []
importedCSV = pd.read_csv(r"C:\Users\Phub Lama\Downloads\sample_grades.csv")
# print(importedCSV)
file = open(r"C:\Users\Phub Lama\Downloads\sample_grades.csv", 'r')
for line in file:
    # print(line.strip())
    line = line.rstrip().split(",")
    # print(list)
    if line[1] == 'Spring 2016':
        spring.append(eval(line[2]))
    else:
        fall.append(eval(line[2]))
file.close()
# print("Spring: ", spring)
# print("Fall: ", fall)
# print()
# MeanMedianStDev(fall)
print("Spring 2016:")
MeanMedianStDev(spring)
print("Fall 2016:")
MeanMedianStDev(fall)



