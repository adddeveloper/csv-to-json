import csv
import json

csv_file = input("csv file name:")

def csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)

    with open(json_file, 'w') as jsonfile:
        jsonfile.write(json.dumps(data, indent=4))

# Example usage

json_file = 'data.json'
csv_to_json(csv_file, json_file)
