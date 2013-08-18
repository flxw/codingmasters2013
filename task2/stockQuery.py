import sys
import math

class Timestamp(object):
    def __init__(self, s):
        # if we get the whole data string
        if '/' in s:
            s = s.split('/')[2].split(' ')[1].upper()

        # if we only get the hours and minutes
        self.hours, self.minutes = s.split(':')
        self.hours = int(self.hours)

        if 'PM' in self.minutes:
            self.hours += 12

        self.minutes = int(self.minutes[:-2])

    def __eq__(self, other): 
        return self.hours == other.hours and self.minutes == other.minutes


class Stockdata(object):
    def __init__(self, csvstring):
        csValues = csvstring.split(',')
        self.timestamp = Timestamp(csValues[1])
        self.valueRange = math.fabs(float(csValues[3]) - float(csValues[4]))

############## main #############################
query = None
dataDictionary = {}
# get and process input
for line in sys.stdin:
    try:
        if query == None:
            query = line
            continue

        stock = line.rstrip().split(',')[0]

        if stock in dataDictionary:
            dataDictionary[stock].append(Stockdata(line))
        else:
            dataDictionary[stock] = [Stockdata(line)]
    except:
        pass

# process query
queryTime, queryStExch = query.rstrip().split(',')
queryTime = Timestamp(queryTime)

###### finished data import ######
for sd in dataDictionary[queryStExch]:
    if queryTime == sd.timestamp:
        print '%.2f' % sd.valueRange
