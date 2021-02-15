import interpreter as ip
import counter as ct
import functions as fc

db_name = input("What's the name and path of the database-file?\n(With format ending, leave empty for standard (game_config.csv) >")
if db_name == "":
    db_name = "game_config.csv"

db = ip.interpret(db_name)