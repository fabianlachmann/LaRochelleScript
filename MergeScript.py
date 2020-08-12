import csv


#noch nicht getestet
def Merge(Inputfiles, Outputfile):#Inputfiles als Array von str mit filelocations; Ouputfile als str mit directory
    with open(Outputfile, mode='a', newline='') as output:  # a steht für append
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


        for input in Inputfiles:
            with open(input) as input:  # öffnet das csv-file
                csv_reader = csv.reader(input, delimiter=',')  # initialisiert den Reader fürs csv
                for row in csv_reader:
                    csv_writer.writerow(row)



    return



#noch nicht getestet
def MergewithLaRochelle(inputfile,outputfile)#Input: str; Ouput: str
    #Soll die Satelliten- und Postitionsdaten mit dem Mittelwertfiel mergen
    Data = []

    with open(outputfile) as output:  # öffnet das csv-file
        csv_reader = csv.reader(output, delimiter=',')
        for row in csv_reader:
            Data.append(row)

    with open(inputfile) as input
        csv_reader = csv.reader(input,delimiter=',')

        for row in csv_reader:
            for i in range(len(Data)):
                if Data[i][:3]==row[:3]:
                    Data[i].append(row)



    with open(outputfile) as output:
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in Data:
            csv_writer.writerow(row)









