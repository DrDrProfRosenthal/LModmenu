import csv

input_csv_filename = 'bereinigte_datei.csv'
output_csv_filename = 'schueler.csv'

# Definieren Sie die Spalte, anhand derer Sie Duplikate entfernen möchten (z.B., Spalte 1)
column_index = 0  # Index 0 entspricht der ersten Spalte

# Verwenden Sie ein Set, um eindeutige Werte in der ausgewählten Spalte zu speichern
unique_values = set()
# Erstellen Sie eine Liste für die neuen Zeilen (ohne Duplikate)
new_rows = []

with open(input_csv_filename, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Lesen Sie die Kopfzeile (wenn vorhanden)
    header = next(csv_reader, None)

    # Durchlaufen Sie jede Zeile in der Eingabe-CSV-Datei
    for row in csv_reader:
         if row[column_index] not in unique_values:
            if "(06g" in str(row[column_index]) or "(05g" in str(row[column_index]) or "(07g" in str(row[column_index]) or "(08G" in str(row[column_index]) or "(09g" in str(row[column_index])or "(10g" in str(row[column_index])or "(05f" in str(row[column_index]) or "(06f" in str(row[column_index])or "(07r" in str(row[column_index])or "(08r" in str(row[column_index])or "(09r" in str(row[column_index])or "(10r" in str(row[column_index])or "(07h" in str(row[column_index])or "(08h" in str(row[column_index])or "(09h" in str(row[column_index])or "(et" in str(row[column_index])or "(12t" in str(row[column_index])or "(13t" in str(row[column_index]):
                unique_values.add(row[column_index])
                new_rows.append(row)
            else:
                print('no cpy')

# Schreiben Sie die bereinigten Daten in die Ausgabe-CSV-Datei
with open(output_csv_filename, mode='w', newline='') as new_csv_file:
    csv_writer = csv.writer(new_csv_file)

    # Schreiben Sie die Kopfzeile (wenn vorhanden)
    if header:
        csv_writer.writerow(header)

    # Schreiben Sie die bereinigten Zeilen
    csv_writer.writerows(new_rows)

print(f'Duplikate in der CSV-Datei wurden entfernt. Die bereinigten Daten wurden in {output_csv_filename} gespeichert.')
