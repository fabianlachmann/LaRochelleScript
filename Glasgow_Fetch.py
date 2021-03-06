import requests
import json
from MergeScript import *
from tkinter import Tk
import time
#run pip install requests in cmd before execution



def Glasgow_Fetch(DatenM,GlasgowDumpfile,APIKeyGlasgow):#Input: Liste mit Zeitangaben
    data = []
    APIKeyGlasgowList = []
    i = 0
    n = 0

    with open(APIKeyGlasgow) as csv_file:
        row = csv.reader(csv_file, delimiter=',')
        for row1 in row:
            for key in row1:
                APIKeyGlasgowList.append(key)

    print(APIKeyGlasgowList)

    while i < len(DatenM):
        APIKey = APIKeyGlasgowList[n]
        Month = int(DatenM[i][0])
        Day = int(DatenM[i][1])
        Hour = int(DatenM[i][2])

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
                Monthadd = Month

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


        print("url")
        url = 'https://services.marinetraffic.com/api/exportvesseltrack/'+str(APIKey)+'/'+\
              'v:2/period:hourly/fromdate:2020-'+str(Month)+'-'+str(Day)+' '+str(Hour)+':00:00/todate:2020-'\
              +str(Monthadd)+'-'+str(Dayadd)+' '\
              +str(Houradd)+':00:00/mmsi:269266000/protocol:json'

        print(url)
        time.sleep(2)
        print("sleep")
        try:
            response = requests.get(url,timeout=30)
            print("response")
        except requests.exceptions.Timeout:
            continue

        print("request successful")

        if response.status_code !=200:
            print("api-error occurred")
            print(response.status_code)
            if response.status_code == 400:
                print("bad request")
                continue #sollte zur nächsten instanz des loops gehen
            elif response.status_code == 401:
                print("not authenticated")# möglicherweise wird das getriggert wenn der api-key keine credits mehr hat
                #hier sollt das API-key handling hinkommen, und dann mit nem goto wieder dahin wo url definiert wird
                #dann gehts nochmal durch die schleife mit dem neuen key
                n += 1
                continue
            elif response.status_code == 404:
                print("not found")
                continue
            else:
                continue


        file = response.json()# sollte die response in nen 2d array oder so umwandeln
        print(file)


        Daten = [Month,Day,Hour]
        if file == []:
            Daten.append(data[len(data)-1][3])#LON
            Daten.append(data[len(data)-1][4])#LAT
        else:
            Daten.append(file[0][3])#LON
            Daten.append(file[0][4])#LAT
        data.append(Daten)

        i+=1
        #end of loop

    #print(data)


    with open(APIKeyGlasgow, mode='w', newline='') as output:
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(APIKeyGlasgowList[n:])


    with open(GlasgowDumpfile, mode='w', newline='') as output:
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            csv_writer.writerow(row)


    print("Glasgow finished")

#Tk().withdraw()
#Dumpfile = askopenfilename()
#Glasgow_Fetch([[7,31,23]],Dumpfile,'b07448715b200b24ccc79909b6cf721ba0f55d3d')