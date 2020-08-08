import urllib.request as request
import json
import csv
#
def Glasgow_Fetch(DatenM):

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
        with request.urlopen('http://data.nba.net/prod/v2/2018/teams.json') as response:
            if response.getcode() == 200:
                source = response.read()
                data = json.loads(source)
                print(data)
            else:
                print('An error occurred while attempting to retrieve data from the API.')
        print(url)









Glasgow_Fetch([[6,1,23]])