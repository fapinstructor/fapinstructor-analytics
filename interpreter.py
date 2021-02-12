import csv
import json

#Converts the hole thing into a dict and changes the config to a dict; gives back the DB as a dict without the first line
def interpret(csvpath):
    with open(csvpath, mode='r' , errors='ignore') as csv_file:
        dictReader = csv.DictReader(csv_file)
        database = []
        for row in dictReader:
            row["config"]=json.loads(row["config"])
            database.append(row)
        return database[1:]