import counter as ct

#This module is for the Functions to write the Data to a file and make it clearly arranged

def rawTimesPlayed(db, taskSorted=True, sortReversed=True):
    """Writes the options with the times they've been played to a file"""
    with open("raw_times_played.txt", "w") as _file:
        for i, j in ct.taskCount(db, taskSorted, sortReversed).items():
            _file.write(str(i) + " : " + str(j) + "\n")
        _file.write("\n" + "Public Games: " + str(ct.isPublicCounter(db)) + "\n")
        _file.write("Number of Games: " + str(len(db)))

def standard_subs()-> list:
    """Giving back a list with the standart subs"""
    with open("standart_subs.txt", "r") as subs:
        subreddits = subs.read().split(",")
    return subreddits

def timeSpans(db, frequ=5, limit=60):
    """Writing the Timespans into a file"""
    total_min = 0
    total_max = 0
    time_dict = ct.time_count(db, frequ, limit)
    with open("timespans.txt", "w") as _file:
        _file.write("Minimum Game Times:\n")
        #write min games
        for key in time_dict['min']:
            _file.write(key + " : " + time_dict['min'][key] + "\n")
            total_min += time_dict['min'][key]
        _file.write("\nMaximum Game Time:\n")
        #write max games
        for key in time_dict['max']:
            _file.write(key + " : " + time_dict['max'][key] + "\n")
            total_max += time_dict['max'][key]
        _file.write("\nTotal Max Games counted : " + str(total_max) + "\n")
        _file.write("Total Min Games counted : " + str(total_min) + "\n")

def sort_values(sortingDict : dict, reversed=True)-> dict:
    """Sorts a Dictionary... Idk how... It just does; reversed for High-Low"""
    sortedDict = {k: v for k, v in sorted(sortingDict.items(), key=lambda item: item[1], reverse=reversed)}
    return sortedDict

def slide_Durations(db, sorted=True, sortReversed=True, maxTime=120):
    """Writes the slide durations with the times they've been played to a file"""
    with open("slide_durations.txt", "w") as slides:
        slides.write("Slide Durations; Time : times played\n\n")
        durations = ct.slide_count(db, sorted, sortReversed, maxTime)
        for o, p in durations.items():
            slides.write(f"{str(o)} : {str(p)}\n")
        del durations["Other"]
        slides.write(f"\nMax-Duration: {max(durations.keys())}\n")
        slides.write(f"Min-Duration: {min(durations.keys())}\n")

def minimumEdges(db, sorted=True, sortReversed=True):
    """Writes the minimum Edges with the times they've been played to a file"""
    with open("minimum_edges.txt", "w") as edges:
        edges.write("Minimum Edges; Edges : times played\n\n")
        edges_dict = ct.minEdge_count(db, sorted, sortReversed)
        for o, p in edges_dict.items():
            edges.write(f"{str(o)} : {str(p)}\n")

def all(db):
    """Just run all functions available to get all data"""
    rawTimesPlayed(db)
    timeSpans(db)
    slide_Durations(db)
    minimumEdges(db)