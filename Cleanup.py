import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def Cleanup(OutputFile_LaRochelle,GlasgowDumpfile,ReykjavikDumpfile,Output):
    Tk().withdraw()

    GlasgowDumpfile.truncate(0)
    ReykjavikDumpfile.truncate(0)


    with open(OutputFile_LaRochelle) as csv_file:#öffnet das csv-file
        csv_reader = csv.reader(csv_file, delimiter=',')
        with open(Output, mode='a', newline='') as resultate:
            resultatewriter = csv.writer(resultate, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in csv_reader:
                resultatewriter.writerow(row)

    OutputFile_LaRochelle.truncate(0)


#def CorrectInput():
