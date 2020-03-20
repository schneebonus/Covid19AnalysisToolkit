# Covid19Compare
Normalize, compare and predict covid19 data.

### Sources:

- https://interaktiv.morgenpost.de/corona-virus-karte-infektionen-deutschland-weltweit/ (CSV API)
- https://soziales.hessen.de/gesundheit/infektionsschutz/coronavirus-sars-cov-2/taegliche-uebersicht-der-bestaetigten-sars-cov-2-faelle-hessen (Crawler)

## Calculate growth of corona in germany and predict nect day

python3 growing_germany.py

```
2020-02-28          55 Infektionen           +111.54% zum Vortag                                                                     
2020-02-29          68 Infektionen           +23.64% zum Vortag                                                                      
2020-03-01          119 Infektionen          +75.0% zum Vortag                                                                       
2020-03-02          152 Infektionen          +27.73% zum Vortag                                                                      
2020-03-03          190 Infektionen          +25.0% zum Vortag                                                                       
2020-03-04          264 Infektionen          +38.95% zum Vortag                                                                      
2020-03-05          402 Infektionen          +52.27% zum Vortag                                                                      
2020-03-06          641 Infektionen          +59.45% zum Vortag                                                                      
2020-03-07          797 Infektionen          +24.34% zum Vortag                                                                      
2020-03-08          905 Infektionen          +13.55% zum Vortag                                                                      
2020-03-09          1141 Infektionen         +26.08% zum Vortag                                                                      
2020-03-10          1567 Infektionen         +37.34% zum Vortag                                                                      
2020-03-11          1968 Infektionen         +25.59% zum Vortag                                                                      
2020-03-12          2747 Infektionen         +39.58% zum Vortag                                                                      
2020-03-13          3677 Infektionen         +33.86% zum Vortag                                                                      
2020-03-14          4587 Infektionen         +24.75% zum Vortag                                                                      
2020-03-15          5815 Infektionen         +26.77% zum Vortag                                                                      
2020-03-16          7274 Infektionen         +25.09% zum Vortag                                                                      
2020-03-17          9362 Infektionen         +28.7% zum Vortag                                                                       
2020-03-18          12329 Infektionen        +31.69% zum Vortag                                                                      
2020-03-19          15322 Infektionen        +24.28% zum Vortag                                                                      
                                                                                                                                     
Durchschnittliches tägliches Wachstum der letzten 7 Tage: 27.88%                                                                     
Eine Verdopplung fand im Schnitt alle 2.5 Tage statt                                                                                 
Prognose für den nächsten Tag: 19593 bestätigte Infektionen        
```

## Compare percentage of invected citizens

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

## Grab infection data for Hessen, Germany

python3 grab_hessen.py

```
Kreis/Stadt,bestätigte Fälle                                                                                                         
Gesamt,740                                                                                                                           
SK Frankfurt am Main,95                                                                                                              
LK Fulda,62                                                                                                                          
LK Schwalm-Eder-Kreis,52                                                                                                             
LK Hochtaunuskreis,40                                                                                                                
LK Main-Kinzig-Kreis,40                                                                                                              
LK Gießen,39                                                                                                                         
LK Limburg-Weilburg,32                                                                                                               
LK Offenbach,32                                                                                                                      
LK Kassel,29                                                                                                                         
SK Kassel,29                                                                                                                         
LK Main-Taunus-Kreis,28                                                                                                              
LK Marburg-Biedenkopf,27                                                                                                             
LK Bergstraße,26                                                                                                                     
LK Wetteraukreis,26                                                                                                                  
LK Groß-Gerau,25                                                                                                                     
LK Lahn-Dill-Kreis,23                                                                                                                
LK Rheingau-Taunus-Kreis,21                                                                                                          
LK Waldeck-Frankenberg,21                                                                                                            
SK Wiesbaden,20                                                                                                                      
LK Darmstadt-Dieburg,17                                                                                                              
LK Hersfeld-Rotenburg,16                                                                                                             
SK Darmstadt,14                                                                                                                      
LK Vogelsbergkreis,13                                                                                                                
LK Odenwaldkreis,8                                                                                                                   
SK Offenbach,4                                                                                                                       
LK Werra-Meißner-Kreis,1  
```
