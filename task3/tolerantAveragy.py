import sys
import math

class Stockdata(object):
    def __init__(self, csvstring):
        csValues = csvstring.split(',')
        self.timestamp = Timestamp(csValues[1])
        self.valueRange = float(csValues[5])

############## main #############################
dataDictionary = {}
# get and process input
for line in sys.stdin:
    try:
        csv = line.rstrip().split(',')
        stock = csv[0]
        ts = csv[1].lower()
        close = float(csv[5])

        if stock in dataDictionary:
            dataDictionary[stock][ts] = close
        else:
            dataDictionary[stock] = { ts:close }
    except:
        pass

###### finished data import ######
ks = sorted(dataDictionary)
for k in ks:
    avg = sum(dataDictionary[k].values())/len(dataDictionary[k].values())

    print '%s,%.2f' % (k, avg)
