# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 14:58:00 2014

@author: jkim
"""

import datetime
from collections import OrderedDict

ADFile = open('/Users/jkim/Data/GroupByData/person_travel_dates_type.csv', 'r')
# this file has the values ordered by PERSON_ID and the dates
# As the program reads the file, it can assume the missing data by checking Type
# Find the dates match with Event_Type 

EventTypes = ["INVALID","REINSTATED","ArrivalPreboard","Imp_DOS_Depart","Arrival","ACTIVE","CORRECTION_REQ_CANCELLED","APPROVED","TERMINATED","CORRECTION_REQ_DENIED","REINSTATE_REQ_REQUESTED","REINSTATE_REQ_CANCELLED","FIN_DOS_APP","CORRECTION_REQ_PENDING","FIN_DOS_ISS","CANCELLED","COMPLETED","PENDING","Apprehension","REFUSAL","CIS_APP_APPRVED","DepartureAPPRND","DepartureNotBrd","Departure","I94FINCancel","CIS_APP_PENDING","INACTIVE","DENIED","APPEALED"]
prev_person_id = ''
prev_status = ''
events_list = []
irregular_persons_id = []
for line in ADFile:
    values = line.strip.split(',')
    numTotal += 1
    person_id = values[0] # check the line is for same person from prev.
    event_type = values[2] # check the type is different from prev.
    if prev_person_id == '' or person_id != prev_person_id:
        #empty even_type list : start over
        events_list.append(event_type)
        prev_person_id = person_id
        prev_status = ''
    if event_type in EventTypes:
        