import requests
import csv
from tkinter.filedialog import askopenfilename

import json


#under construction
#problem töglich vs stündlich position
def Reykjavik_Fetch(GlasgowDumpfile,ReykjavikDumpfile,Daten):
    data = []

    with open(GlasgowDumpfile) as csv_file:#öffnet das csv-file
        csv_reader = csv.reader(csv_file, delimiter=',') #initialisiert den Reader fürs csv
        for row in csv_reader:
            data.append(row)

    for i in Daten:
        Month = i[0]
        Day = i[1]


        if Day < 10:
            Day = '0' + str(Day)

        if Month < 10:
            Month = '0' + str(Month)

        Longitude =
        Latitude =

        key = 'cbf99eb3a48741f8940134148200608'
        url ='http://api.worldweatheronline.com/premium/v1/past-marine.ashx?'+'key='+key+'&'+'format=json'+\
            '&2020-'+str(Month)+'-'+str(Day)+'&q='+str(Longitude)+','+str(Latitude)

        print(url)
        response = requests.get(url) #habs jetzt mit der requests library gemacht

        if response.status_code !=200:
            print("api-error occurred")
            if response.status_code == 400:
                print("bad request")
                continue #sollte zur nächsten instanz des loops gehen
            elif response.status_code == 401:
                print("not authenticated")# möglicherweise wird das getriggert wenn der api-key keine credits mehr hat
                #hier sollt das API-key handling hinkommen, und dann mit nem goto wieder dahin wo url definiert wird

            elif response.status_code == 404:
                print("not found")
                continue
            else:
                continue


        file = response.json()# sollte die response in nen 2d array oder so umwandeln
        print(file)



    print(data)


    with open(ReykjavikDumpfile, mode='w', newline='') as output:
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            csv_writer.writerow(row)

    print("Glasgow finished")

    print("Reykjavik finished")
