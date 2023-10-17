

#
# main problem with this file: maybe you need to copy the code, insert it in a nodepad file, then change that file to .py and open it here
# visual studio has some problems regarding öüä etc but if you load a file save somewhere else it works somehow
#

import csv
import re

input_csv_filename = 'bereinigte_datei.csv'
output_csv_filename = 'UserNamesLaKurzel.csv'

# Definieren Sie die Spalte, anhand derer Sie Duplikate entfernen möchten (z.B., Spalte 1)
column_index = 0  # Index 0 entspricht der ersten Spalte

def transferToLStr(g):
    
    input_string = str(g).strip("[]'")
    pattern = r'\d'
    
    if re.search(pattern, input_string):
        parts = input_string.split(',')
        name_parts = parts[1].split()
        vornamenStr=""
        x=0
        for i  in name_parts:
            x = x+1
            if x < len(name_parts):
                if x+1 == len(name_parts): # wemm x beim vorletzten ist
                    vornamenStr = vornamenStr+i
                else:
                    vornamenStr = vornamenStr+i+"."   
 
        parts = parts[0].split()


        nachnamenString =""
        y=0
        vollerName=""

        for i  in parts:
            y = y+1

            if y <= len(parts):
                if y == len(parts):
                    vollerName = [vornamenStr+nachnamenString+"."+i]  
                    return vollerName
                    #print(vollerName)
                else:
                
                    nachnamenString = nachnamenString+"."+i
    else:
        parts = input_string.split(',')
        name_parts = parts[1].split()        
        return [name_parts[len(name_parts)-1].strip("()'")]



# Erstellen Sie eine Liste für die neuen Zeilen (ohne Duplikate)
new_rows = []


with open(input_csv_filename, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Lesen Sie die Kopfzeile (wenn vorhanden)
    header = next(csv_reader, None)

    # Durchlaufen Sie jede Zeile in der Eingabe-CSV-Datei
    for row in csv_reader:
          print(str(row))   
          print(row) 
          print(type(row))
          new_rows.append(transferToLStr(row))
          
        
        
          
     

# Schreiben Sie die bereinigten Daten in die Ausgabe-CSV-Datei
with open(output_csv_filename, mode='w', newline='') as new_csv_file:
    csv_writer = csv.writer(new_csv_file)

    # Schreiben Sie die Kopfzeile (wenn vorhanden)
    if header:
        csv_writer.writerow(header)

    # Schreiben Sie die bereinigten Zeilen
    print(new_rows)
    #print(type(new_rows))
    
    csv_writer.writerows(new_rows)

print(f'Duplikate in der CSV-Datei wurden entfernt. Die bereinigten Daten wurden in {output_csv_filename} gespeichert.')
