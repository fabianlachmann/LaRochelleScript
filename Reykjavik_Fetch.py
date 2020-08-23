import requests
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import json


#under construction
#problem töglich vs stündlich position
def Reykjavik_Fetch(GlasgowDumpfile,ReykjavikDumpfile,Daten,APIKeyReykjavik):

    data = []
    APIKeyReykjavikList = []
    n = 0
    i=0

    with open(APIKeyReykjavik) as csv_file:
        row = next(csv.reader(csv_file, delimiter=','))
        for key in row:
            APIKeyReykjavikList.append(key)



    with open(GlasgowDumpfile) as csv_file:#öffnet das csv-file
        csv_reader = csv.reader(csv_file, delimiter=',') #initialisiert den Reader fürs csv
        for row in csv_reader:
            data.append(row)

    while i < len(data):
        APIKey = APIKeyReykjavikList[n]
        Month = int(data[i][0])
        Day = int(data[i][1])
        Hour = int(data[i][2])


        if Day < 10:
            Day = '0' + str(Day)

        if Month < 10:
            Month = '0' + str(Month)

        Longitude = float(data[i][3])
        Latitude = float(data[i][4])

        #APIkeyReykjavik = 'cbf99eb3a48741f8940134148200608'
        url ='https://api.worldweatheronline.com/premium/v1/past-marine.ashx?'+'key='+APIKey+'&'+'format=json'+\
            '&date=2020-'+str(Month)+'-'+str(Day)+'&q='+str(Latitude)+','+str(Longitude)

        print(url)
        try:
            response = requests.get(url,timeout= 20) #habs jetzt mit der requests library gemacht
        except TimeoutError:
            continue

        if response.status_code !=200:
            print("api-error occurred")
            print(response.status_code)
            if response.status_code == 400:
                print("bad request")
                continue #sollte zur nächsten instanz des loops gehen
            elif response.status_code == 401:
                print("not authenticated")# möglicherweise wird das getriggert wenn der api-key keine credits mehr hat
                #hier sollt das API-key handling hinkommen, und dann mit nem goto wieder dahin wo url definiert wird
                n+=1
                continue
            elif response.status_code == 404:
                print("not found")
                continue
            else:
                continue



        file = response.json()
        print(file)
        print(type(file))



        data[i].append(file['data']['weather'][0]['hourly'][Hour]['tempC'])
        data[i].append(file['data']['weather'][0]['hourly'][Hour]['windspeedKmph'])
        data[i].append(file['data']['weather'][0]['hourly'][Hour]['precipMM'])
        data[i].append(file['data']['weather'][0]['hourly'][Hour]['humidity'])
        data[i].append(file['data']['weather'][0]['hourly'][Hour]['visibility'])
        data[i].append(file['data']['weather'][0]['hourly'][Hour]['pressure'])
        data[i].append(file['data']['weather'][0]['hourly'][Hour]['cloudcover'])
        data[i].append(file['data']['weather'][0]['hourly'][Hour]['HeatIndexC'])
        data[i].append(file['data']['weather'][0]['hourly'][Hour]['DewPointC'])
        data[i].append(file['data']['weather'][0]['hourly'][Hour]['sigHeight_m'])
        data[i].append(file['data']['weather'][0]['hourly'][Hour]['swellHeight_m'])
        data[i].append(file['data']['weather'][0]['hourly'][Hour]['waterTemp_C'])

        i+=1

    print(data)


    with open(APIKeyReykjavik, mode='w', newline='') as output:
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(APIKeyReykjavikList[n:])


    with open(ReykjavikDumpfile, mode='w', newline='') as output:
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            csv_writer.writerow(row)


    print("Reykjavik finished")



#Tk().withdraw()
#Inputfile = askopenfilename()
#Dumpfile = askopenfilename()
#print(Dumpfile)
#Reykjavik_Fetch(Inputfile,Dumpfile,[[7,16]],'cbf99eb3a48741f8940134148200608')