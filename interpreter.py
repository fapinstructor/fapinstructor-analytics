import csv
import json
from functions import bcolors as bc

# Converts the hole thing into a dict and changes the config to a dict; gives back the DB as a dict without the first line


def interpret(csvpath):
    print(f"{bc.HEADER}=====Starting interpreter...====={bc.ENDC}")
    try:
        print(f"{bc.OKBLUE}Starting interpretation...{bc.ENDC}")
        with open(csvpath, mode='r', errors='ignore') as csv_file:
            dictReader = csv.DictReader(csv_file)
            database = []
            print(f"{bc.OKBLUE}Starting to convert the config...{bc.ENDC}")
            for row in dictReader:
                row["config"] = json.loads(row["config"])
                database.append(row)
            print(f"{bc.OKBLUE}Done converting the config.{bc.ENDC}")
            print(f"{bc.OKBLUE}Done with interpretation.{bc.ENDC}")
            print(f"{bc.HEADER}=====Ending Interpreter====\n{bc.ENDC}")
            return database[1:]
    except FileNotFoundError:
        print(f"{bc.FAIL}Oops, something went wrong while interpreting the database!\nPlease check if you specified the right Path and try again.{bc.ENDC}")
    except:
        print(
            f"{bc.FAIL}Oops, something went wrong while interpreting the database!{bc.ENDC}")
