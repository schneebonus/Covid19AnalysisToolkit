# Covid19Compare
Normalize and compare covid19 data

## Example (2020-03-16:00:00)

python3 compare_covid.py 

```
Vergleich der Covid19-Lage

Dieses Tool soll helfen die Infektionslage und die momentane Last auf das Gesundheitssystem
einer Region vergleichbar zu machen.
Statt wie üblich nur über Infektionen, geheilte und verstorbene Patienten zu reden, betrachtet
dieses Tool die aktuell ungelösten Infektionen.
Die Definition ist dabei:
ungelöste Infektionen = Infektionen - geheilte Patienten - verstorbene Patienten

Da unterschiedliche Regionen unterschiedlich stark bevölkert sind, muss für die Vergleichbarkeit
eine Normalisierung statt finden.
Dieses Tool normalisiert auf den Prozentsatz der Bevölkerung mit bestätigten laufenden Infektionen.
Daraus ergibt sich folgende Rechnung für den Score einer Region:
Score = round((extract_running_cases_for_location(key) / population[key] * 100),5)

Als Datenquelle wird die Echtzeit-Karte der Berliner Morgenpost genutzt:
https://interaktiv.morgenpost.de/corona-virus-karte-infektionen-deutschland-weltweit/
Um die Server hinter dieser Karte nicht zu überlasten, sollten dieses Tool
und daraus entstehende Arbeiten verantwortungsvoll und mit Bedacht genutzt werden.

Region                  Bestätigter momentan infizierter
			Anteil der Bevölkerung
----------------------------------------------------------------------------------------------------
Island                  0.04482%        
Italien                 0.02945%        
Schweiz                 0.02554%        
Norwegen                0.02241%        
Spanien                 0.01496%        
Dänemark                0.01477%        
Südkorea                0.01468%        
Nordrhein-Westfalen     0.01153%        
Hamburg                 0.01065%        
Iran                    0.01054%        
Luxemburg               0.00945%        
Österreich              0.00895%        
Berlin                  0.00776%        
Deutschland             0.00693%        
Bayern                  0.00664%        
Frankreich              0.00659%        
Niederlande             0.00644%        
Hessen                  0.0045%         
Portugal                0.00229%        
Großbritannien          0.00166%        
China                   0.00077%        
Polen                   0.0003%         
Madagaskar              0.0%            

Weiterführende Ideen:
- Die Anzahl der verfügbaren Krankenhausbetten / Atemgeräte statt der Bevölkerungsanzahl.
- Visualisierung der zeitlichen Entwicklung.
- Bestimmen wessen Zahlen aktuell wie schnell wachsen.
- Durchgeführte Tests / Bürger (in den letzten x Tagen?) in den Score aufnehmen um die Dunkelziffer annähern zu können. 
  Ein Land, das nicht flächendeckend testet, sollte nicht im Score belohnt werden.
```
