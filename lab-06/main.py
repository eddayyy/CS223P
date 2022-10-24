# Author: Eduardo Nunez
# Author Email: eduardonunez@csu.fullerton.edu
# File: main.py, python

from weather import *
from calendar import *

readings_data = {}
weaather_data = {}
while True:
    x = int(input(f" *** TUFFY TITAN WEATHER LOGGER MAIN MENU\n\n1. Set data filename\n2. Add weather data\n3. Print daily report\n4. Print historical report\n9. Exit the program\n"))
    if x == 1:
        x = input("Enter data filename: ")
        read_data(x)
        
    elif x == 2:
        date = str(input("Enter date (YYYYMMDD): "))
        time = str(input("Enter time (hhmmss): "))
        datetime = date + time
        print(datetime)
        temp = input("Enter the temperature: ")
        humidity = input("Enter the humidity: ")
        rainfall = float(input("Enter rainfall: "))
        readings_data = {'t' : temp, 'h' : humidity, 'r' : rainfall}
        weather_data = {datetime : readings_data}
        write_data(weather_data, datetime)

    elif x == 3:
        report = report_daily(weather_data, datetime)
        print(report)
    elif x == 4:
        report_historical(weather_data)
        
    elif x == 9:
        exit()
    
        
        
        