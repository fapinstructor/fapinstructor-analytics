import interpreter as ip
import counter as ct
import functions as fc

db = ip.interpret("game_config.csv")

print(ct.slide_count(db))