import csv
import math
from tkinter import Tk
from tkinter.filedialog import askopenfilename
#Welche Stelle für was steht hab ich aus dem CSV-File rausgelesen, könnte als teilweise nicht ganz stimmen


def LaRochelle(directory,output):
    Tk().withdraw()

    # Zuerst wird nach der zu mittelenden Datei und dann nach der Output-location gefragt.
    #directory = askopenfilename()
    #output = askopenfilename()

    #Station,Timestamp,Year,Month,Day,Hour,Min,Sec,
    #0.46um,0.66um,0.89um,1.15um,1.45um,1.85um,2.55um,3.5um,4.5um,5.75um,7.25um,9um,11um,13um,15um,16.5um,DurationSample_s,FlowRate_ml/s

    with open(directory) as csv_file:#öffnet das csv-file
        csv_reader = csv.reader(csv_file, delimiter=',') #initialisiert den Reader fürs csv
        line_count = 0 # zählt wie viele Messungen es pro stunde gab

        werte = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  # liste, in der die werte addiert werden, länge = 16
        messungszeit = 0 # messungszeit wird hier addiert und dann am ende für den avg durch line_count geteilt
        flowrate = 0 # flowrate wird hier addiert und dann am ende für den avg durch line_count geteilt

        mittelwerte = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #0,1,2: Monat,Tag,Stunde 4-19: Mittelwerte Anz Teilchen 20,21: Avg Messungszeit, Avg Flowrate

        notnullcond =0

        for row in csv_reader:

            if row == [] or row[0]=="Station": # Sortiert leere Linien oder Linien mit Namen aus
                continue

            for i in range(len(werte)): # Check ob alle Werte =0 sind
                if int(row[i+8])!=0:
                    notnullcond =1
                    break

            if notnullcond == 0:
                continue

            if line_count == 0:
                monat = int(row[3])
                tag = int(row[4])
                stunde = int(row[5])

            line_count += 1

            if stunde != int(row[5]):

                avg_messungszeit = messungszeit/(line_count)
                avg_flowrate = flowrate/(line_count)

                flowrate = 0 #für nächste Stunde
                messungszeit = 0 #für nächste Stunde

                mittelwerte[19] = avg_messungszeit
                mittelwerte[20] = avg_flowrate

                mittelwerte[21] = line_count
                mittelwerte[0] = monat # damit wird dem Mittelwert ein Datum zugewiesen
                mittelwerte[1] = tag
                mittelwerte[2] = stunde



                for i in range(len(werte)):
                    mittelwerte[i+3]= (werte[i]/(line_count))*avg_messungszeit
                    werte[i] = 0 # für nächste Stunde

                with open(output, mode='a',newline='') as resultate: #a steht für append
                    resultatewriter = csv.writer(resultate, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    resultatewriter.writerow(mittelwerte)
                print(mittelwerte)

                line_count = 0 # damit es nur pro Stunde zählt


            for i in range(len(werte)): # Werten der row werden in die liste addiert und für flowrate und messungszeit korriegiert
                if (float(row[25])) == 0:
                    continue

                werte[i] += int(row[8+i]) / (float(row[25]))


            messungszeit += float(row[24])
            flowrate += float(row[25])




        # das folgende ist nötig, weil die letzte Stunde nicht durch den loop oben abgedeckt wird
        if line_count != 0:
            avg_messungszeit = messungszeit/line_count
            avg_flowrate = flowrate/line_count

            mittelwerte[19] = avg_messungszeit
            mittelwerte[20] = avg_flowrate

            mittelwerte[21] = line_count

            mittelwerte[0] = monat # damit wird dem Mittelwert ein Datum zugewiesen
            mittelwerte[1] = tag
            mittelwerte[2] = stunde

            for i in range(len(werte)):
                mittelwerte[i+3]= (werte[i]/line_count)*avg_messungszeit


            with open(output,mode='a',newline='') as resultate:
                resultatewriter = csv.writer(resultate, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                resultatewriter.writerow(mittelwerte)

            print(mittelwerte)

    return 1

