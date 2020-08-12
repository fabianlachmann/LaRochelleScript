import csv

def Merge(Inputfiles, Outputfile):#Inputfiles als Array von str mit filelocations; Ouputfile als str mit directory
    with open(Outputfile, mode='a', newline='') as output:  # a steht für append
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


        for input in Inputfiles:
            with open(input) as input:  # öffnet das csv-file
                csv_reader = csv.reader(input, delimiter=',')  # initialisiert den Reader fürs csv
                for row in csv_reader:
                    csv_writer.writerow(row)



    return

