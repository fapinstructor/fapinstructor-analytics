import csv
import json

def interpret(csvpath):
    # Converts the hole thing into a dict and changes the config to a dict; gives back the DB as a dict without the first line
    try:
        with open(csvpath, mode='r', errors='ignore') as csv_file:
            dictReader = csv.DictReader(csv_file)
            database = []
            for row in dictReader:
                row["config"] = json.loads(row["config"])
                database.append(row)
            return database[1:]
    except FileNotFoundError:
        print("Oops, something went wrong while interpreting the database!\nPlease check if you specified the right Path and try again.")
    except:
        print(
            f"Oops, something went wrong while interpreting the database!")
