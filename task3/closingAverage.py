import sys
import math

dataDictionary = {}

# get and process data
for line in sys.stdin:
    try:
        csValues = line.split(',')
        stock = csValues[0]
        closing = float(csValues[5])

        if stock in dataDictionary:
            dataDictionary[stock].append(closing)
        else:
            dataDictionary[stock] = [closing]
    except:
        pass
###### finished data import ######


ks = sorted(dataDictionary)
for k in ks:
    avg = sum(dataDictionary[k])/len(dataDictionary[k])
    print '%s,%.2f' % (k, avg)
