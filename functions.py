import counter as ct

#This module is for the Functions to write the Data to a file and make it clearly arranged

#Writes the options with the times they've been played to a file
def rawTimesPlayed(db, taskSorted=True, sortReversed=True):
    print(f"{bcolors.HEADER}=====Starting writing times to file====={bcolors.ENDC}")
    with open("raw_times_played.txt", "w") as _file:
        print(f"{bcolors.OKBLUE}Writing...{bcolors.ENDC}")
        for i, j in ct.taskCount(db, taskSorted, sortReversed).items():
            _file.write(str(i) + " : " + str(j) + "\n")
        _file.write("\n" + "Public Games: " + str(ct.isPublicCounter(db)) + "\n")
        _file.write("Number of Games: " + str(len(db)))
        print(f"{bcolors.OKBLUE}Done writing.{bcolors.ENDC}")
    print(f"{bcolors.HEADER}=====Ending writing times to file=====\n{bcolors.ENDC}")

#Giving back a list with the standart subs
def standard_subs():
    print(f"{bcolors.HEADER}=====Starting reading standard subs====={bcolors.ENDC}")
    with open("standart_subs.txt", "r") as subs:
        print(f"{bcolors.OKBLUE}Starting reading...{bcolors.ENDC}")
        subreddits = subs.read().split(",")
    print(f"{bcolors.HEADER}Done reading.{bcolors.ENDC}")
    print(f"{bcolors.HEADER}=====Ending reading standard subs=====\n{bcolors.ENDC}")
    return subreddits

#Writing the Timespans into a file
def timeSpans(db, frequ=5, limit=60):
    print(f"{bcolors.HEADER}=====Starting to write Timespans=====")
    total_min = 0
    total_max = 0
    time_dicts = ct.time_count(db, frequ, limit)
    with open("timespans.txt", "w") as _file:
        print(f"{bcolors.OKBLUE}Writing to file...{bcolors.ENDC}")
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
    print(f"{bcolors.HEADER}=====Done writing Timespans=====\n{bcolors.ENDC}")

#Sorts a Dictionary... Idk how... It just does; reversed for High-Low
def sort_values(sortingDict, reversed=True):
    print(f"{bcolors.OKBLUE}Sorting...{bcolors.ENDC}")
    sortedDict = {k: v for k, v in sorted(sortingDict.items(), key=lambda item: item[1], reverse=reversed)}
    print(f"{bcolors.OKBLUE}Done sorting.{bcolors.ENDC}")
    return sortedDict

#Some colors for better console feedback
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Writes the slide durations with the times they've been played to a file
def slide_Durations(db, sorted=True, sortReversed=True, maxTime=120):
    print(f"{bcolors.HEADER}=====Starting writing slide durations to file====={bcolors.ENDC}")
    with open("slide_durations.txt", "w") as slides:
        print(f"{bcolors.OKBLUE}Writing...{bcolors.ENDC}")
        slides.write("Slide Durations; Time : times played\n\n")
        durations = ct.slide_count(db, sorted, sortReversed, maxTime)
        for o, p in durations.items():
            slides.write(f"{str(o)} : {str(p)}\n")
        del durations["Other"]
        slides.write(f"\nMax-Duration: {max(durations.keys())}\n")
        slides.write(f"Min-Duration: {min(durations.keys())}\n")
        print(f"{bcolors.OKBLUE}Done writing.{bcolors.ENDC}")
    print(f"{bcolors.HEADER}=====Ending writing slide durations to file=====\n{bcolors.ENDC}")

#Writes the minimum Edges with the times they've been played to a file
def minimumEdges(db, sorted=True, sortReversed=True):
    print(f"{bcolors.HEADER}=====Starting writing minimum Edges to file====={bcolors.ENDC}")
    with open("minimum_edges.txt", "w") as edges:
        print(f"{bcolors.OKBLUE}Writing...{bcolors.ENDC}")
        edges.write("Minimum Edges; Edges : times played\n\n")
        edges_dict = ct.minEdge_count(db, sorted, sortReversed)
        for o, p in edges_dict.items():
            edges.write(f"{str(o)} : {str(p)}\n")
        print(f"{bcolors.OKBLUE}Done writing.{bcolors.ENDC}")
    print(f"{bcolors.HEADER}=====Ending writing minimum Edges to file=====\n{bcolors.ENDC}")