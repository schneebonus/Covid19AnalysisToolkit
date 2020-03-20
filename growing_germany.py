import time
import requests
from datetime import datetime
from collections import defaultdict

# Base url of morgenpost api
base_url = "https://interaktiv.morgenpost.de/corona-virus-karte-infektionen-deutschland-weltweit/data/"

# endpoints of the api
path_current = "Coronavirus.current.v2.csv"     # this is used to request the latest date
path_history = "Coronavirus.history.v2.csv"	# not used but might be interesting in the future (-> plot history and see the (exponential?) function)
path_timeline = "Coronavirus.timeline.v2.csv"	# not used but might be interesting in the future (-> plot history of germany, europe and the world)

# timestamp for the request
timestamp = int(time.time())

# do the request and show the result
r = requests.get(base_url + path_history + "?" + str(timestamp))
r.encoding = r.apparent_encoding	# fix encoding... it is 2020... encoding still fucked up

current_stats = r.text
current_stats_lines = current_stats.split("\n")

def extract_region_infection_sum_for_time(t, location, timeline):
	sum = 0
	for entry in timeline[t]:
		if entry[0] == location or entry[1] == location:
			sum += int(entry[2])
	return sum

# create a dictionary that uses the time as key
timeline = defaultdict(list)
for line in current_stats_lines[1:]:
	split = line.split(",")
	if len(split) >= 5:
		timeline[split[2]].append([split[0], split[1], split[5], split[6], split[7]])

past = 0
growth_history = []
keys = [k for k in timeline.keys()]
keys.sort()
for k in keys:
	present = extract_region_infection_sum_for_time(k, "Deutschland", timeline)
	if past is not 0:
		growth_number = round(((present - past ) / past) * 100,2)
		growth_history.append(growth_number)
		if growth_number > 0:
			doubeling_in = round(70 / growth_number,1)
			growth = "+" + str(growth_number) + "% zum Vortag"
		else:
			growth = ""
	else:
		growth = ""
		growth_history.append(0)
	print('{0:20}{1:25}{2:20}'.format(k, str(present) + " Infektionen", growth))
	past = present

average = 0
for i in range(1, 8):
	average += growth_history[0 - i]
average = round(average / 7,2)
doubeling_in = round(70 / average,1)
print("")
print("Durchschnittliches tägliches Wachstum der letzten 7 Tage: " + str(average) + "%")
print("Eine Verdopplung fand im Schnitt alle "+str(doubeling_in) + " Tage statt")
print("Prognose für den nächsten Tag: " + str(int(past * (1 + (average / 100)))) + " bestätigte Infektionen")
