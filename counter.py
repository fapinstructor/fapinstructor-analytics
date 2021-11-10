import functions as fc

# This module is for getting the data, standart sorted

# Counts how many Games are public; gives back an int with the times played


def isPublicCounter(db):
    print(f"{fc.bcolors.HEADER}=====Starting Public Games Counter====={fc.bcolors.ENDC}")
    public_true = 0
    print(f"{fc.bcolors.OKBLUE}Starting to count...{fc.bcolors.ENDC}")
    for row in db:
        if row["is_public"] == "true":
            public_true += 1
    print(f"{fc.bcolors.OKBLUE}Done counting.{fc.bcolors.ENDC}")
    print(f"{fc.bcolors.HEADER}=====Ending Counter=====\n{fc.bcolors.ENDC}")

    return public_true

# Counts the Options with the times they've been played; returns dict with, standart sorted, tasks with times played


def taskCount(database, taskSorted=True, sortReversed=True):
    print(f"{fc.bcolors.HEADER}=====Starting Options Counter====={fc.bcolors.ENDC}")
    task = database[0]["config"]["tasks"]
    # writing the tasks
    print(f"{fc.bcolors.OKBLUE}Writing to Dict...{fc.bcolors.ENDC}")
    for row in database[1:]:
        for i in row["config"]["tasks"].keys():
            task[i] += row["config"]["tasks"][i]
    print(f"{fc.bcolors.OKBLUE}Done writing{fc.bcolors.ENDC}")
    # If it should be sorted or not and in which Order
    if taskSorted == True:
        task = fc.sort_values(task, sortReversed)
    print(f"{fc.bcolors.HEADER}=====Ending Options Counter=====\n{fc.bcolors.ENDC}")
    return task

# Counts and Sorts the game times; returns two dicts: 1. Maximum Game times with times played, 2. Minimum Game times with times played


def time_count(db, frequ=5, limit=60) -> dict:
    print(f"{fc.bcolors.HEADER}=====Starting Time Counter====={fc.bcolors.ENDC}")
    times = {}
    times['min'] = {}
    times['max'] = {}
    # writing the timespans
    print(f"{fc.bcolors.OKBLUE}Writing the timespans...{fc.bcolors.ENDC}")
    for i in range(frequ, limit+1, frequ):
        times['max'][str(i)] = 0
        times['min'][str(i)] = 0
    times["greater"] = 0
    print(f"{fc.bcolors.OKBLUE}Done writing Timespans.{fc.bcolors.ENDC}")
    print(f"{fc.bcolors.OKBLUE}Counting Times...{fc.bcolors.ENDC}")
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

    print(f"{fc.bcolors.OKBLUE}Done counting Times.{fc.bcolors.ENDC}")
    print(f"{fc.bcolors.HEADER}=====Ending Time Counter=====\n{fc.bcolors.ENDC}")
    return times

# Counts and sorts the slide durations; returns a dict with, standart sorted, slide duration with times played


def slide_count(db, durationsSorted=True, sortReversed=True, maxTime=120):
    print(f"{fc.bcolors.HEADER}=====Starting Slide Duration Counter====={fc.bcolors.ENDC}")
    durations = {}
    durations["Other"] = 0
    print(f"{fc.bcolors.OKBLUE}Starting to count...{fc.bcolors.ENDC}")
    for row in db:
        number = str(row["config"]["slideDuration"])
        if float(number) > float(maxTime):
            durations["Other"] += 1
        elif number in durations:
            durations[number] = durations[number] + 1
        else:
            durations[number] = 1
    print(f"{fc.bcolors.OKBLUE}Done counting durations.{fc.bcolors.ENDC}")
    if durationsSorted == True:
        durations = fc.sort_values(durations, sortReversed)
    print(f"{fc.bcolors.HEADER}=====Ending Slide Duration Counter=====\n{fc.bcolors.ENDC}")
    return durations

# Counts and sorts the minimum edges; returns a dict with, standart sorted, minimum edges with times played


def minEdge_count(db, edgesSorted=True, sortReversed=True):
    print(f"{fc.bcolors.HEADER}=====Starting minimum Edge Counter====={fc.bcolors.ENDC}")
    minEdges = {}
    print(f"{fc.bcolors.OKBLUE}Starting to count...{fc.bcolors.ENDC}")
    for row in db:
        edges = str(row["config"]["minimumEdges"])
        if edges in minEdges:
            minEdges[edges] = minEdges[edges] + 1
        else:
            minEdges[edges] = 1
    print(f"{fc.bcolors.OKBLUE}Done counting durations.{fc.bcolors.ENDC}")
    if edgesSorted == True:
        minEdges = fc.sort_values(minEdges, sortReversed)
    print(f"{fc.bcolors.HEADER}=====Ending minimum Edge Counter=====\n{fc.bcolors.ENDC}")
    return minEdges
