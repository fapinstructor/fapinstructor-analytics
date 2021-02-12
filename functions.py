import counter as ct

#This module is for the Functions to write the Data to a file and make it clearly arranged

#Writes the Options with the times they've been played to a file
def rawTimesPlayed(db, taskSorted, sortReversed):
    with open("raw_times_played.txt", "w") as _file:
        for i, j in ct.taskCount(db, taskSorted, sortReversed).items():
            _file.write(str(i) + " : " + str(j) + "\n")
        _file.write("\n" + "Public Games: " + str(ct.isPublicCounter(db)) + "\n")
        _file.write("Number of Games: " + str(len(db)))

#Giving back a list with the standart subs
def standart_subs():
    with open("standart_subs.txt", "r") as subs:
        subreddits = subs.read().split(",")
    return subreddits


def timeSpans(db, frequ=5, limit=60):
    total_min = 0
    total_max = 0
    time_dicts = ct.time_count(db, frequ, limit)
    with open("timespans.txt", "w") as _file:
        _file.write("Maximum Game Times:\n")
        #write max games
        for i, j in time_dicts[0].items():
            _file.write(str(i) + " : " + str(j) + "\n")
            total_max += j
        _file.write("\nMinimum Game Time:\n")
        #write min games
        for n, u in time_dicts[1].items():
            _file.write(str(n) + " : " + str(u) + "\n")
            total_min += u
        _file.write("\nTotal Max Games counted : " + str(total_max) + "\n")
        _file.write("Total Min Games counted : " + str(total_min) + "\n")

#Sorts a Dictionary... Idk how... It just does; reversed for Hgh-Low
def sort(sortingDict, reversed=True):
    sortedDict = {k: v for k, v in sorted(sortingDict.items(), key=lambda item: item[1], reverse=reversed)}
    return sortedDict