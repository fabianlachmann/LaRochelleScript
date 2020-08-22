import requests
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import json


#under construction
#problem töglich vs stündlich position
def Reykjavik_Fetch(GlasgowDumpfile,ReykjavikDumpfile,Daten,APIKeyReykjavik):

    data = []

    with open(GlasgowDumpfile) as csv_file:#öffnet das csv-file
        csv_reader = csv.reader(csv_file, delimiter=',') #initialisiert den Reader fürs csv
        for row in csv_reader:
            data.append(row)

    for i in data:

        Month = int(i[0])
        Day = int(i[1])
        Hour = int(i[2])


        if Day < 10:
            Day = '0' + str(Day)

        if Month < 10:
            Month = '0' + str(Month)

        Longitude = float(i[3])
        Latitude = float(i[4])

        #APIkeyReykjavik = 'cbf99eb3a48741f8940134148200608'
        url ='https://api.worldweatheronline.com/premium/v1/past-marine.ashx?'+'key='+APIKeyReykjavik+'&'+'format=json'+\
            '&date=2020-'+str(Month)+'-'+str(Day)+'&q='+str(Longitude)+','+str(Latitude)

        print(url)
        response = requests.get(url) #habs jetzt mit der requests library gemacht

        if response.status_code !=200:
            print("api-error occurred")
            if response.status_code == 400:
                print("bad request")
                #continue #sollte zur nächsten instanz des loops gehen
            elif response.status_code == 401:
                print("not authenticated")# möglicherweise wird das getriggert wenn der api-key keine credits mehr hat
                #hier sollt das API-key handling hinkommen, und dann mit nem goto wieder dahin wo url definiert wird

            elif response.status_code == 404:
                print("not found")
                #continue
            else:
                #continue
                print("s")


        file = response.json()#
        print(file)
        print(type(file))



        i.append(file['data']['weather'][0]['hourly'][Hour]['tempC'])
        i.append(file['data']['weather'][0]['hourly'][Hour]['windspeedKmph'])
        i.append(file['data']['weather'][0]['hourly'][Hour]['precipMM'])
        i.append(file['data']['weather'][0]['hourly'][Hour]['humidity'])
        i.append(file['data']['weather'][0]['hourly'][Hour]['visibility'])
        i.append(file['data']['weather'][0]['hourly'][Hour]['pressure'])
        i.append(file['data']['weather'][0]['hourly'][Hour]['cloudcover'])
        i.append(file['data']['weather'][0]['hourly'][Hour]['HeatIndexC'])
        i.append(file['data']['weather'][0]['hourly'][Hour]['DewPointC'])
        i.append(file['data']['weather'][0]['hourly'][Hour]['sigHeight_m'])
        i.append(file['data']['weather'][0]['hourly'][Hour]['swellHeight_m'])
        i.append(file['data']['weather'][0]['hourly'][Hour]['waterTemp_C'])


    print(data)


    with open(ReykjavikDumpfile, mode='w', newline='') as output:
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            csv_writer.writerow(row)


    print("Reykjavik finished")



Tk().withdraw()
Inputfile = askopenfilename()
Dumpfile = askopenfilename()
Reykjavik_Fetch(Inputfile,Dumpfile,[[7,16]],'cbf99eb3a48741f8940134148200608')