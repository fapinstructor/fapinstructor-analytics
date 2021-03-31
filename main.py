import interpreter as ip
import counter as ct
import functions as fc
import time
start_time = time.time()

db_name = input("What's the name and path of the database-file?\n(With format ending, leave empty for standard (game_config.csv) >")
if db_name == "":
    db_name = "game_config.csv"

db = ip.interpret(db_name)

time_taken = time.time() - start_time
print(f"==================================================\n"
    "Done, took {time_taken} seconds."
    )