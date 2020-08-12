import csv

def Merge(Inputfiles, Outputfile):#Inputfiles als Array von str mit filelocations; Ouputfile als str mit directory
    with open(Outputfile) as output:#öffnet das csv-file
        csv_reader = csv.reader(output, delimiter=',') #initialisiert den Reader fürs csv


        for input in Inputfiles:
            with open(input) as input:  # öffnet das csv-file
                csv_reader = csv.reader(input, delimiter=',')  # initialisiert den Reader fürs csv
