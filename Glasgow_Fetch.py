#import urllib
#from urllib.request import urlopen
import requests
import json
import csv
from MergeScript import *
from tkinter import Tk
#run pip install requests in cmd before execution


def Glasgow_Fetch(DatenM,GlasgowDumpfile):#Input: Liste mit Zeitangaben
    data = []

    for i in DatenM:
        Month = i[0]
        Day = i[1]
        Hour = i[2]

        Monthadd = 0
        Dayadd = 0
        Houradd = 0


        if Hour == 23:
            if Month == 6 and Day == 30 and Hour == 23:
                Monthadd = Month + 1
                Dayadd = 1
                Houradd = 0

            elif Month == 7 and Day == 31 and Hour == 23:
                Monthadd = Month + 1
                Dayadd = 1
                Houradd = 0

            elif Month == 8 and Day == 31 and Hour == 23:
                Monthadd = Month + 1
                Dayadd = 1
                Houradd = 0


            elif Month == 9 and Day == 30 and Hour == 23:
                Monthadd = Month + 1
                Dayadd = 1
                Houradd = 0


            elif Month == 10 and Day == 31 and Hour == 23:
                Monthadd = Month + 1
                Dayadd = 1
                Houradd = 0

            else:
                Houradd = 0
                Dayadd = Day + 1

        else:
            Houradd = Hour + 1
            Dayadd = Day
            Monthadd = Month

        if Hour < 10:
            Hour = '0'+str(Hour)
            if Houradd < 10:
                Houradd = '0'+str(Houradd)

        if Day < 10:
            Day = '0'+str(Day)
            if Dayadd < 10:
                Dayadd = '0'+str(Dayadd)
        if Month < 10:
            Month = '0'+str(Month)
            if Monthadd < 10:
                Monthadd = '0'+str(Monthadd)

        url = 'https://services.marinetraffic.com/api/exportvesseltrack/b07448715b200b24ccc79909b6cf721ba0f55d3d/'+\
              'v:2/period:hourly/fromdate:2020-'+str(Month)+'-'+str(Day)+' '+str(Hour)+':00:00/todate:2020-'\
              +str(Monthadd)+'-'+str(Dayadd)+' '\
              +str(Houradd)+':00:00/mmsi:269266000/protocol:json'

        print(url)
        response = requests.get(url) #habs jetzt mit der requests library gemacht

        if response.status_code !=200:
            print("api-error occurred")
            if response.status_code == 400:
                print("bad request")
                continue #sollte zur nächsten instanz des loops gehen
            elif response.status_code == 401:
                print("not authenticated")
                continue
            elif response.status_code == 404:
                print("not found")
                continue
            elif response.status_code == 403:
                print("permission not correct")# möglicherweise wird das getriggert wenn der api-key keine credits mehr hat
                #hier sollt das API-key handling hinkommen, und dann mit nem goto wieder dahin wo url definiert wird


        file = response.json()# sollte die response in nen 2d array oder so umwandeln
        print(file)


        Daten = [Month,Day,Hour]
        Daten.append(file[0][3])#LON
        Daten.append(file[0][4])#LAT
        data.append(Daten)
    #print(data)


    with open(GlasgowDumpfile, mode='w', newline='') as output:
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            csv_writer.writerow(row)


Tk().withdraw()
Dumpfile = askopenfilename()
Glasgow_Fetch([[7,12,18]],Dumpfile)