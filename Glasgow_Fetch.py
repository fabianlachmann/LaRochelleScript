import urllib.request
import csv

def Glassgow_Fetch(DatenM):

    for i in DatenM:
        Month = i[0]
        Day = i[1]
        Hour = i[2]

        Monthadd = Month
        Dayadd = Day
        Houradd = Hour + 1


        if Hour == 23:
            Dayadd = Day + 1
            Houradd = 0

        if Month == 6 and Day == 30 and Hour == 23:
            Monthadd == Month + 1
            Dayadd == 1
            Houradd == 0
        if Month == 7 and Day == 31 and Hour == 23:
            Monthadd == Month + 1
            Dayadd == 1
            Houradd == 0
        if Month == 8 and Day == 31 and Hour == 23:
            Monthadd == Month + 1
            Dayadd == 1
            Houradd == 0
        if Month == 9 and Day == 30 and Hour == 23:
            Monthadd == Month + 1
            Dayadd == 1
            Houradd == 0
        if Month == 10 and Day == 31 and Hour == 23:
            Monthadd == Month + 1
            Dayadd == 1
            Houradd == 0



        url = 'https://services.marinetraffic.com/api/exportvesseltrack/b07448715b200b24ccc79909b6cf721ba0f55d3d/'+'v:2/period:hourly/fromdate:2020-'+Month+'-'+Day' '+Hour+':00:00/todate:2020-'+Monthadd+'-'+Dayadd+' '+Houradd+':00:00/mmsi: 269266000 / prot






