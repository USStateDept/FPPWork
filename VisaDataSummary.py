"""
FPU / Visa Data Analysis Summary Program
Created 9/9/2014
DOS/EDIP/DID/GIS/JKIM
"""
import datetime
from collections import OrderedDict

class Person:
    vd_id = 0
    person_id = 0
    fin = 0
    history = []
    def __init__(self, vd_id, person_id):
        self.vd_id = vd_id
        self.person_id = person_id        
class EventDate:
    eType = 'A'
    eDate = datetime.date()
    def __init__(self, yyyy, mm, dd, eType):
        self.eDate(yyyy,mm,dd)
        self.eType = eType        
ADFile = open('/Data/AnalyticsPilotDataSet.txt', 'r')
#    ADFile = line.strip().split('\t') for line in tsv
eventList = []
personList = set()
seen = set()
numDup = 0
numTot = 0
numDestination = 0
for line in ADFile:
    numTot += 1
    line_lower = line.strip().lower()
    col = line.strip().split('\t')
    if line_lower in seen:
        numDup += 1
    else: 
        seen.add(line_lower)
    eventList.insert(len(eventList),col[21])
    # DoB check since it's only month and year
    dob = col[2].split('/')
    if len(dob) == 2:
        dobyear = dob[1]
        dobmonth = dob[0]
    # check ID & Person_ID_FK & FIN (null in Depart)
    Person(col[0],col[1])
    personList.add(Person)        
#DeDup the event List as IDs
uniqueEvents = OrderedDict.fromkeys(eventList)    
print "Unique Events: ", len(uniqueEvents)    
print "Duplicates: ", numDup
print "Total records read: ", numTot
