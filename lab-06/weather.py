# Author: Eduardo Nunez
# Author Email: eduardonunez@csu.fullerton.edu
# File: main.py, python

import math
import json
from calendar import *
import datetime 

def read_data(filename: str) -> dict:
  try:
    with open(filename, 'r') as f:
        return json.load(f)
  except FileNotFoundError:
    return {}
    
    
def write_data(data, filename):
        with open(filename, 'w') as fn:
            json.dump(data, fn)
            
def max_temperature(data, date):
    max_temp = -100
    for key in data:
        if key[0:8] == date:
            if max_temp < data[key]['t']:
                max_temp = data[key]['t'] 
    return max_temp

def min_temperature(data, date):
    min_temp = 100
    for key in data:
        if key[0:8] == date:
            if min_temp > data[key]['t']:
                min_temp = data[key]['t']               
    return min_temp    

def max_humidity(data, date):
    max_humidity = -100
    for key in data:
        if key[0:8] == date:
            if max_humidity < data[key]['h']:
                max_humidity = data[key]['h']                  
    return max_humidity


def min_humidity(data, date):
    min_humidity = 100
    for key in data:
        if key[0:8] == date:
            if min_humidity > data[key]['h']:
                min_humidity = data[key]['h']                  
    return min_humidity

def tot_rain(data, date):
    tot_rain = 0
    for key in data:
        tot_rain += data[key]['r']
    return tot_rain

def report_daily(data, date):
    year = date[0:4]
    month = month_name[int(date[6:8])]
    day = str(int(date[6:8]))
    hour = str(int(date[8:10]))
    minute = str(int(date[10:12]))
    second = str(int(date[12:14]))
    temp = data[date]['t']
    hum = data[date]['h']
    rain = data[date]['r']
    report = f'========================= DAILY REPOPRT =========================\nDate                  Time  Temperature  Humidity  Rainfall\n===================  ========  ===========  ========  ========\n{month}  {day}, {year}\t      {hour}:{minute}:{second}\t {temp}\t    {hum}\t\t {rain}'

    return report

def report_historical(data):

    report =          "============================== HISTORICAL REPORT ===========================\n"
    report = report + "                          Minimum      Maximum   Minumum   Maximum     Total\n"
    report = report + "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    report = report + "====================  ===========  ===========  ========  ========  ========\n"

    reported = list()

    for key, value in data.items():
        date_time = key
        date = date_time[0:8]
        month_datetime = date_time.date_time.strptime(str(int((date_time[4:6]))), '%m')
        month = month_datetime.strftime("%B")

        if date not in reported:
            max_temp = max_temperature(data=data, date=date)
            min_temp = min_temperature(data=data, date=date)
            max_humid = max_humidity(data=data, date=date)
            min_humid = min_humidity(data=data, date=date)
            tot_rainfall = tot_rain(data=data, date=date)
            reported.append(date)
            report = report + month + ' ' + str(int(key[6:8])) + ', ' + key[0:4] + '               ' + str(min_temp) + '           ' + str(max_temp) + '        ' + str(min_humid) + '        ' + str(max_humid) + '      ' + "{:.2f}".format(tot_rainfall) + '\n'

    return report