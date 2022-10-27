import os
import csv
import json

os.system('wget "https://docs.google.com/spreadsheets/d/19VzXj0JtoNKn1WQ1EZ_kc0DP7lh0LSrwPACBIVO1fmo/export?format=csv" -O perf-appear.csv')

entries = {
    "entries":[]
}

with open('perf-appear.csv') as f:
    rows = csv.reader(f)
    headers = None
    for i, row in enumerate(rows):
        if i == 0:
            headers = row
        else:
            entry = {}
            for j, header in enumerate(headers):
                entry[header] = row[j]
            entries["entries"].append(entry)

if len(entries["entries"]) > 0:
    with open('../data/perfappear.json', 'w') as f:
        json.dump(entries, f)