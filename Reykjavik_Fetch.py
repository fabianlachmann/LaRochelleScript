import csv
import math
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import itertools

Tk().withdraw()

# Mittelwerte sind der Output aus LaRochelle Script. Positionen sind der Output aus Glasgow script, mit dem selben
# timecode wie LaRochelle

Mittelwerte = askopenfilename()
#Positionen=askopenfilename()

#Deklariert 2D-Array für alle Zeitcodes in Messungen und Daten in Messungen
ZeitM = []
DatenM = []

#Ordnet alle verfügbaren Zeicodes in Liste ZeitM ein


with open(Mittelwerte) as csv_file:  # öffnet das gemittelte csv-file mit den Longitude und Latitude Daten
    csv_reader = csv.reader(csv_file, delimiter=',')  # initialisiert den Reader fürs csv

    for row in csv_reader:
        Zeit1HM = row[:3]
        ZeitM.append(Zeit1HM)



    for row in ZeitM: #Ruft die ersten Zwei Einträge des Timestamp arrays auf: Datum
        Datum = row[:2]
        for row in DatenM: #Checkt ob sich das Datum im DatenM array befindet

            if Datum == row:
                continue
            else:
                DatenM.append(Datum)
                break

    print(DatenM)

