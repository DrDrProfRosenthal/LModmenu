import csv

input_csv_filename = 'bereinigte_datei.csv'
output_csv_filename = 'UserNames.csv'

# Definieren Sie die Spalte, anhand derer Sie Duplikate entfernen m�chten (z.B., Spalte 1)
column_index = 0  # Index 0 entspricht der ersten Spalte

# Verwenden Sie ein Set, um eindeutige Werte in der ausgew�hlten Spalte zu speichern




# Split the input string into parts
def transferToLStr(input_string):
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
    print(parts)

    nachnamenString =""
    y=0
    vollerName=""

    for i  in parts:
        y = y+1
        print(len(parts))
        print(i)
        if y <= len(parts):
            if y == len(parts):
                vollerName = vornamenStr+nachnamenString+"."+i  
                print(vollerName)
            else:
                nachnamenString = nachnamenString+"."+i








# Erstellen Sie eine Liste f�r die neuen Zeilen (ohne Duplikate)
new_rows = []

with open(input_csv_filename, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Lesen Sie die Kopfzeile (wenn vorhanden)
    header = next(csv_reader, None)

    # Durchlaufen Sie jede Zeile in der Eingabe-CSV-Datei
    for row in csv_reader:
          print(row)   
          new_rows.append(transferToLStr(row))
     

# Schreiben Sie die bereinigten Daten in die Ausgabe-CSV-Datei
with open(output_csv_filename, mode='w', newline='') as new_csv_file:
    csv_writer = csv.writer(new_csv_file)

    # Schreiben Sie die Kopfzeile (wenn vorhanden)
    if header:
        csv_writer.writerow(header)

    # Schreiben Sie die bereinigten Zeilen
    csv_writer.writerows(new_rows)

print(f'Duplikate in der CSV-Datei wurden entfernt. Die bereinigten Daten wurden in {output_csv_filename} gespeichert.')
