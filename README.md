# Coding-Challenge-Merging-Intervals

## Challenge

### Inhalt der Challenge

Es wird eine Funktion **MERGE** benötigt, welche eine Liste von Intervallen entgegennimmt und als Ergebnis wiederum eine Liste von Intervallen zurückgibst.
Im Ergebnis sollen alle sich überlappenden Intervalle gemerged sein. Alle nicht überlappenden Intervalle bleiben unberührt.

#### Beispiel

Input: [25,30] [2,19] [14,23] [4,8]  

Output: [2,23] [25,30]

### Rahmenbedingungen

Bei der Challenge sind folgende Rahmenbedingungen zu beachten:

- Bearbeitungsdauer: max 1-2 Tage
- Dokumentation
    - Bearbeitungszeit
    - Code 
    - Challenge
- Testing
- Lauffähiges Programm

### Kriterien

Bei der Challenge sind folgende Kriterien zu beachten:

- Laufzeit des Programms 
- Speicherverbrauch des Programms
- Robustheit sicherstellen, vor allem in Bezug auf sehr große Eingaben

### Ergebnisse

Die Challenge wurde mit **Python** durchgeführt. Die Dokumentation zur Umsetzung befinden sich im Ordner *python*.

- Bearbeitungszeit: ca. 7 Stunden
- Programmlaufzeit des Beispiels: 0.0006091000395826995 Sekunden
- Speicherverbrauch des Beispiels: 5284767 Bytes (~5,3 MB)
- Robustheit durch User Feedback, Exception Handling und Tests sicher gestellt

## Nutzung

Folgende Parameter können im Programm genutzt werden:

```
options:
  -h, --help            show this help message and exit
  --intervals INTERVALS [INTERVALS ...], -i INTERVALS [INTERVALS ...]
                        Add min 2 intervals to get merged (-i 2 6 -i 3 10)
  --example [EXAMPLE], -e [EXAMPLE]
                        Shows the challenge example
  --timer, -t           Returns execution time
  --memory, -m          Returns memory usage
```

Um das Beispiel aus der Challenge auszuführen:

```
>> python merge/merge.py -e -m -t


Status: merging intervals

Merged intervals:
[[2, 23], [25, 30]]

Status: done!

Runtime:
0.00879190000705421 seconds

Current memory heap:
9911673 bytes
```

Um beliebige Intervalle anzugeben:

```
>> python merge/merge.py -m -t -i 5 9 -i 12 18 -34 62 -30 37 -6 8


Status: merging intervals

Merged intervals:
[[5, 9], [12, 18], [30, 62]]

Status: done!

Runtime:
0.00787480000872165 seconds

Current memory heap:
9913645 bytes
```

Beispiel:

![usage](https://i.imgur.com/wE5wQD0.gif)