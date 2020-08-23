import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def Cleanup(OutputFile_LaRochelle,GlasgowDumpfile,ReykjavikDumpfile,Output):
    Tk().withdraw()

    with open(GlasgowDumpfile, mode='w', newline='') as output:
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


    with open(ReykjavikDumpfile, mode='w', newline='') as output:
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


    with open(OutputFile_LaRochelle) as csv_file:#öffnet das csv-file
        csv_reader = csv.reader(csv_file, delimiter=',')
        with open(Output, mode='a', newline='') as resultate:
            resultatewriter = csv.writer(resultate, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in csv_reader:
                resultatewriter.writerow(row)

    with open(OutputFile_LaRochelle, mode='w', newline='') as output:
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)



#def CorrectInput():
