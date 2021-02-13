import functions as fc

#This module is for getting the data, mostly unsorted

#Counts how many Games are public, gives back int with the times played
def isPublicCounter(db):
    public_true = 0
    for row in db:
        if row["is_public"] == "true":
            public_true += 1
    return public_true

#Counts the Options with the times they've been played; returns dict with, standart sorted, tasks and times played
def taskCount(database, taskSorted=True, sortReversed=True):
    task = database[0]["config"]["tasks"]
    #writing the tasks
    for row in database[1:]:
        for i in row["config"]["tasks"].keys():
            task[i] += row["config"]["tasks"][i]
    #If it should be sorted or not and in which Order
    if taskSorted == True:
        task = fc.sort_values(task, sortReversed)
    return task

#Counts and Sorts the game times
def time_count(db, frequ=5, limit=60):
    times = {}
    #writing the timespans
    for i in range(frequ, limit+1, frequ):
        times[str(i)] = 0
    times["greater"] = 0
    max = times.copy()
    min = times.copy()
    for row in db:
        #setting variables for more efficeny and functionallity
        max_found = False
        min_found = False
        max_start, min_start = 0, 0
        max_stop, min_stop = frequ+1, frequ+1
        min_number = round(row["config"]["minimumGameTime"])
        max_number = round(row["config"]["maximumGameTime"])
        
        #First for the max Game Time
        while max_found == False:
            if max_number > limit:
                max["greater"] = max["greater"] + 1
                max_stop, max_start = 0, 0
                max_found = True
            elif max_number in range(max_start, max_stop):
                max[str(max_stop-1)] = max[str(max_stop-1)] + 1
                max_stop, max_start = 0, 0
                max_found = True
            else:
                max_start = max_stop
                max_stop = max_stop + frequ
        
        #Second for the min Game Time
        while min_found == False:
            if min_number > limit:
                min["greater"] = min["greater"] + 1
                min_stop, min_start = 0, 0
                min_found = True
            elif min_number in range(min_start, min_stop):
                min[str(min_stop-1)] = min[str(min_stop-1)] + 1
                min_stop, min_start = 0, 0
                min_found = True
            else:
                min_start = min_stop
                min_stop = min_stop + frequ
    return max, min

#Counts and sorts the slide durations
def slide_count(db, durationsSorted=True, sortReversed=True):
    durations = {}
    for row in db:
        number = str(row["config"]["slideDuration"])
        if number in durations:
            durations[number] = durations[number] + 1
        else:
            durations[number] = 1
    if durationsSorted == True:
        durations = fc.sort_values(durations, sortReversed)
    return durations