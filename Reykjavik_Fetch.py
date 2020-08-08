import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import itertools
#yeet

Tk().withdraw()

# Mittelwerte sind der Output aus LaRochelle Script. Positionen sind der Output aus Glasgow script, mit dem selben
# timecode wie LaRochelle

Mittelwerte = askopenfilename()
#Positionen=askopenfilename()

#Deklariert 2D-Array für alle Zeitcodes in Mittelwerte und Daten in Mittelwerteq
ZeitM = [] #Monat, Tag, Stunde
DatenMfinal = [] #Monat, Tag
DatenM = [] #Monat, Tag mit duplikaten
#Ordnet alle verfügbaren Zeicodes in Liste ZeitM ein


with open(Mittelwerte) as csv_file:  # öffnet das gemittelte csv-file mit den Longitude und Latitude Daten
    csv_reader = csv.reader(csv_file, delimiter=',')  # initialisiert den Reader fürs csv

    for row in csv_reader:
        Zeit = row[:2]
        DatenM.append(Zeit)


    #print(DatenM)
    DatenMsortedTuple = list(set(tuple(sorted(sub)) for sub in DatenM)) #entfernt Duplikate

    DatenMsortedList = [list(elem) for elem in DatenMsortedTuple] #Konvertiert die Liste aus Tupeln in eine Nested list
    #print(DatenMsortedList)


    for element in DatenMsortedList: #Reorganisiert die Nested List in Monat, Tag Format
        a = element[1]
        b = element[0]
        OrderedDate = [a,b]
        DatenMfinal.append(OrderedDate)
    print(DatenMfinal)







