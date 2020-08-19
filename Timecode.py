import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import itertools


def Timecodes(input): #Input: filename für Zeit(gemittelt); Output: 2D-Liste mit nur Zeit

    Tk().withdraw()

    # Mittelwerte sind der Output aus LaRochelle Script. Positionen sind der Output aus Glasgow script, mit dem selben
    # timecode wie LaRochelle

    Mittelwerte = input

    DatenM = []

    with open(Mittelwerte) as csv_file:  # öffnet das gemittelte csv-file mit den Longitude und Latitude Daten
        csv_reader = csv.reader(csv_file, delimiter=',')  # initialisiert den Reader fürs csv

        for row in csv_reader:
            Zeit = row[:3]
            DatenM.append(Zeit)

        #print(DatenM)
        print("Timecodes finished")
        return DatenM


def TimecodesDays(input):
    Daten = []
    Daten_final = []
    check = 0

    with open(input) as csv_file:  # öffnet das gemittelte csv-file mit den Longitude und Latitude Daten
        csv_reader = csv.reader(csv_file, delimiter=',')  # initialisiert den Reader fürs csv

        for row in csv_reader:
            Zeit = row[:2]
            Daten.append(Zeit)

    Daten_final.append(Daten[0])
    for row1 in Daten:
        for row2 in Daten_final:
            if row1 == row2:
                check = 1
                break
        if check == 0:
            Daten_final.append(row1)

        check = 0

    print(Daten_final)
    return  Daten_final

#Tk().withdraw()


#input = askopenfilename()
#TimecodesDays(input)

