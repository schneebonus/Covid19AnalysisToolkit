import time
import requests
from datetime import datetime

# Base url of morgenpost api
base_url = "https://interaktiv.morgenpost.de/corona-virus-karte-infektionen-deutschland-weltweit/data/"

# endpoints of the api
path_current = "Coronavirus.current.v2.csv"     # this is used to request the latest date
path_history = "Coronavirus.history.v2.csv"	# not used but might be interesting in the future (-> plot history and see the (exponential?) function)
path_timeline = "Coronavirus.timeline.v2.csv"	# not used but might be interesting in the future (-> plot history of germany, europe and the world)

# timestamp for the request
timestamp = int(time.time())

# do the request and show the result
r = requests.get(base_url + path_current + "?" + str(timestamp))
r.encoding = r.apparent_encoding	# fix encoding... it is 2020... encoding still fucked up

current_stats = r.text
current_stats_lines = current_stats.split("\n")


def extract_running_cases_for_location(location):
	sum = 0
	for line in current_stats_lines:
		parsed_line = line.split(",")
		if parsed_line[0] == location or (len(parsed_line)>1 and parsed_line[1] == location):
			number = number = int(parsed_line[4]) - int(parsed_line[5]) -int(parsed_line[6])
			sum += int(number)
	return sum

# define regions and their population
# Key is the name of the region (should match the names of the Berliner Morgenpost 'CSV API')
# Value is the population
population = {
	'Deutschland':		83019213,	# https://de.wikipedia.org/wiki/Liste_der_deutschen_Bundesl%C3%A4nder_nach_Bev%C3%B6lkerung
	'Italien':		60262701,	# https://de.wikipedia.org/wiki/Italien
	'China':		1400050000,	# https://de.wikipedia.org/wiki/Volksrepublik_China
	'Spanien':		46722980,	# https://de.wikipedia.org/wiki/Spanien
	'Frankreich':		66993000,	# https://de.wikipedia.org/wiki/Frankreich
	'Schweiz':		8544527,	# https://de.wikipedia.org/wiki/Schweiz
	'Hessen':		6265809,	# https://de.wikipedia.org/wiki/Liste_der_deutschen_Bundesl%C3%A4nder_nach_Bev%C3%B6lkerung
	'Bayern':		13076721,	# https://de.wikipedia.org/wiki/Liste_der_deutschen_Bundesl%C3%A4nder_nach_Bev%C3%B6lkerung
	'Nordrhein-Westfalen':	17932651 ,	# https://de.wikipedia.org/wiki/Liste_der_deutschen_Bundesl%C3%A4nder_nach_Bev%C3%B6lkerung
	'Berlin':		3644826,	# https://de.wikipedia.org/wiki/Liste_der_deutschen_Bundesl%C3%A4nder_nach_Bev%C3%B6lkerung
	'Hamburg':		1841179,	# https://de.wikipedia.org/wiki/Liste_der_deutschen_Bundesl%C3%A4nder_nach_Bev%C3%B6lkerung
	'Österreich':		8858775,	# https://de.wikipedia.org/wiki/%C3%96sterreich
	'Polen':		38433558,	# https://de.wikipedia.org/wiki/Polen
	'Südkorea':		51629512,	# ... wikipedia!
	'Iran':			81800269,	# ...
	#'USA':			285620445,	# ToDo: USA fucks up the split(",") and leads to index problems
	'Norwegen':		5367580,
	'Großbritannien':	66435550,
	'Niederlande':		17290688,
	'Dänemark':		5806081 + 56584 + 48354,	# Festland + Grönland + Färöer
	'Portugal':		10600000,
	'Island':		356991,
	'Madagaskar':		26262368,
	'Luxemburg':		613894,
	}

# calculate the running infections for every location and normalize it by the population
results = []
for key in population.keys():
	results.append((key, round((extract_running_cases_for_location(key) / population[key] * 100),5)))

# sort by the amount of running infections
results.sort(key=lambda x:x[1], reverse=True)

# Output intro text
print("")
print("Vergleich der Covid19-Lage\n")
print("Dieses Tool soll helfen die Infektionslage und die momentane Last auf das Gesundheitssystem\neiner Region vergleichbar zu machen.")
print("Statt wie üblich nur über Infektionen, geheilte und verstorbene Patienten zu reden, betrachtet\ndieses Tool die aktuell ungelösten Infektionen.")
print("Die Definition ist dabei:")
print("ungelöste Infektionen = Infektionen - geheilte Patienten - verstorbene Patienten\n")
print("Da unterschiedliche Regionen unterschiedlich stark bevölkert sind, muss für die Vergleichbarkeit\neine Normalisierung statt finden.")
print("Dieses Tool normalisiert auf den Prozentsatz der Bevölkerung mit bestätigten laufenden Infektionen.")
print("Daraus ergibt sich folgende Rechnung für den Score einer Region:")
print("Score = round((extract_running_cases_for_location(key) / population[key] * 100),5)")
print("")
print("Als Datenquelle wird die Echtzeit-Karte der Berliner Morgenpost genutzt:\nhttps://interaktiv.morgenpost.de/corona-virus-karte-infektionen-deutschland-weltweit/")
print("Um die Server hinter dieser Karte nicht zu überlasten, sollten dieses Tool\nund daraus entstehende Arbeiten verantwortungsvoll und mit Bedacht genutzt werden.")
print("")

# Format and output the results
#print(datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S'))
#print("")
print('{0:23} {1:16}'.format("Region", "Bestätigter momentan infizierter\n\t\t\tAnteil der Bevölkerung"))
print("-" * 100)
for result in results:
	print('{0:23} {1:16}'.format(result[0],str(result[1]) + "%"))

# Output further ideas
print("")
print("Weiterführende Ideen:")
print("- Die Anzahl der verfügbaren Krankenhausbetten / Atemgeräte statt der Bevölkerungsanzahl.")
print("- Visualisierung der zeitlichen Entwicklung.")
print("- Bestimmen wessen Zahlen aktuell wie schnell wachsen.")
print("- Durchgeführte Tests / Bürger (in den letzten x Tagen?) in den Score aufnehmen um die Dunkelziffer annähern zu können. \n  Ein Land, das nicht flächendeckend testet, sollte nicht im Score belohnt werden.")
