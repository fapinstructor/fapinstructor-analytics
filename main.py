import interpreter as ip
import functions as fc
import time

db_name = input("What's the name and path of the database-file?\n(With format ending, leave empty for standard (game_config.csv) >")
db_name = "game_config.csv" if db_name == "" else db_name
start_time = time.time()
db = ip.interpret(db_name)

fc.all(db)

time_taken = time.time() - start_time
print(f"==================================================\n"
    f"Done, took {time_taken} seconds."
    )