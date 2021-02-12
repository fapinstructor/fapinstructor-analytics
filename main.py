import interpreter as ip
import counter as ct
import functions as fc

db = ip.interpret("game_config.csv")

fc.timeSpans(db)
