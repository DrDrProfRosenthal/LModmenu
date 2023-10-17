import csv

# Definieren Sie den Dateinamen Ihrer Eingabe-CSV-Datei
input_csv_filename = 'li_elements2.csv'

# Definieren Sie den Dateinamen Ihrer Ausgabe-CSV-Datei
output_csv_filename = 'bereinigte_datei.csv'

# Definieren Sie die Spalte, anhand derer Sie Duplikate entfernen möchten (z.B., Spalte 1)
column_index = 0  # Index 0 entspricht der ersten Spalte

# Verwenden Sie ein Set, um eindeutige Werte in der ausgewählten Spalte zu speichern
unique_values = set()

# Erstellen Sie eine Liste für die neuen Zeilen (ohne Duplikate)
new_rows = []


excluded_texts = ['Lehrkr', 'Eltern','bereinstimmungen']


# Öffnen Sie die Eingabe-CSV-Datei zum Lesen
with open(input_csv_filename, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Lesen Sie die Kopfzeile (wenn vorhanden)
    header = next(csv_reader, None)

    # Durchlaufen Sie jede Zeile in der Eingabe-CSV-Datei
    for row in csv_reader:
        # Überprüfen Sie, ob der Wert in der ausgewählten Spalte eindeutig ist
        if row[column_index] not in unique_values:
            if "Lehrkr" in str(row[column_index]) or "Eltern" in str(row[column_index]) or "bereinstimmungen" in str(row[column_index]) or "Lernende" in str(row[column_index]) or "suche ..." in str(row[column_index])or "header" in str(row[column_index]):
                print('no cpy')
            else:
                unique_values.add(row[column_index])
                new_rows.append(row)


# Schreiben Sie die bereinigten Daten in die Ausgabe-CSV-Datei
with open(output_csv_filename, mode='w', newline='') as new_csv_file:
    csv_writer = csv.writer(new_csv_file)

    # Schreiben Sie die Kopfzeile (wenn vorhanden)
    if header:
        csv_writer.writerow(header)

    # Schreiben Sie die bereinigten Zeilen
    csv_writer.writerows(new_rows)

print(f'Duplikate in der CSV-Datei wurden entfernt. Die bereinigten Daten wurden in {output_csv_filename} gespeichert.')
