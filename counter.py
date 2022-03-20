import functions as fc

# This module is for getting the data, standart sorted

def isPublicCounter(db):
    """Counts how many Games are public; gives back an int with the times played"""
    public_true = 0
    for row in db:
        if row["is_public"] == "true":
            public_true += 1
    return public_true

def taskCount(database, taskSorted=True, sortReversed=True):
    """Counts the Options with the times they've been played; returns dict with, standart sorted, tasks with times played"""
    task = database[0]["config"]["tasks"]
    # writing the tasks
    for row in database[1:]:
        for i in row["config"]["tasks"].keys():
            task[i] += row["config"]["tasks"][i]
    # If it should be sorted or not and in which Order
    if taskSorted == True:
        task = fc.sort_values(task, sortReversed)
    return task

def time_count(db, frequ=5, limit=60) -> dict:
    """Counts and Sorts the game times; returns two dicts: 1. Maximum Game times with times played, 2. Minimum Game times with times played"""
    times = {}
    times['min'] = {}
    times['max'] = {}
    # writing the timespans
    for i in range(frequ, limit+1, frequ):
        times['max'][str(i)] = 0
        times['min'][str(i)] = 0
    times["greater"] = 0
    for row in db:
        # setting variables for more efficeny and functionallity
        found = False
        start = 0
        stop = frequ+1
        max_min_list = {'min': round(row["config"]["minimumGameTime"]), 'max': round(
            row["config"]["maximumGameTime"])}

        for key in max_min_list:
            while found == False:
                if max_min_list[key] > limit:
                    times["greater"] = times["greater"] + 1
                    start, stop = 0, 0
                    found = True
                elif max_min_list[key] in range(start, stop):
                    times[key][str(stop-1)] = times[key][str(stop-1)] + 1
                    stop, start = 0, 0
                    found = True
                else:
                    start = stop
                    stop = stop + frequ
    return times

def slide_count(db, durationsSorted=True, sortReversed=True, maxTime=120):
    """Counts and sorts the slide durations; returns a dict with, standart sorted, slide duration with times played"""
    durations = {}
    durations["Other"] = 0
    for row in db:
        number = str(row["config"]["slideDuration"])
        if float(number) > float(maxTime):
            durations["Other"] += 1
        elif number in durations:
            durations[number] = durations[number] + 1
        else:
            durations[number] = 1
    if durationsSorted == True:
        durations = fc.sort_values(durations, sortReversed)
    return durations

def minEdge_count(db, edgesSorted=True, sortReversed=True):
    """Counts and sorts the minimum edges; returns a dict with, standart sorted, minimum edges with times played"""
    minEdges = {}
    for row in db:
        edges = str(row["config"]["minimumEdges"])
        if edges in minEdges:
            minEdges[edges] = minEdges[edges] + 1
        else:
            minEdges[edges] = 1
    if edgesSorted == True:
        minEdges = fc.sort_values(minEdges, sortReversed)
    return minEdges
