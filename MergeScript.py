import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename



#sollte funktionieren
def Merge(Inputfiles, Outputfile):#Inputfiles als Array von str mit filelocations; Ouputfile als str mit directory
    with open(Outputfile, mode='a', newline='') as output:  # a steht für append
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


        for input in Inputfiles:
            with open(input) as input:  # öffnet das csv-file
                csv_reader = csv.reader(input, delimiter=',')  # initialisiert den Reader fürs csv
                for row in csv_reader:
                    csv_writer.writerow(row)



    return



#sollte funktionieren
def MergewithLaRochelle(inputfile,outputfile):#Input: str; Ouput: str
    #Soll die Satelliten- und Postitionsdaten mit dem Mittelwertfile mergen
    Data = []

    with open(outputfile) as output:  # öffnet das csv-file
        csv_reader = csv.reader(output, delimiter=',')
        for row in csv_reader:
            Data.append(row)

    with open(inputfile) as input:
        csv_reader = csv.reader(input,delimiter=',')

        for row in csv_reader:
            for i in range(len(Data)):
                if int(Data[i][0])==int(row[0]) and int(Data[i][1]) == int(row[1]) and int(Data[i][2])==int(row[2]):
                    for element in row[3:]:
                        Data[i].append(element)


    #aufpassen
    with open(outputfile,mode='w',newline='') as output:
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in Data:
            csv_writer.writerow(row)

    print("Merge finished")
    return





#---------------- für Test: -------------------

#Tk().withdraw()


#input = askopenfilename()
#output = askopenfilename()

#MergewithLaRochelle(input,output)






