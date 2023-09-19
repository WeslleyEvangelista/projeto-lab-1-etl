import csv
import json

csv_file = open('project_1.csv', 'r')
json_file = open('project_1.json', 'w')

field_names = ("FirstName", "LastName", "Email")
reader = csv.DictReader(csv_file, field_names)

for row in reader:
    json.dump(row, json_file)
    json_file.write('\n')