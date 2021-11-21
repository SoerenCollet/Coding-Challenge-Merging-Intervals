# Python Lösung

## Methode

Es wird nach TDD (Test Driven Development) entwickelt.

## Initialisierung

In diesem Projekt wird Python in der Version **3.10.0** verwendet.

Um das Projekt ausführen zu können, muss ein virtual environment mit folgendem Befehl ausgerollt werden:

```
>> cd python
>> python -m venv venv
```

Um das Virtual environment nutzen zu können, wird das entsprechende Activate-Script verwendet:
```
>> . venv/Scripts/activate
```

Jetzt können die benötigten Module installiert werden (Aktuelle Versionsstände stehen im File **requirements.txt**):
```
(venv) >> pip install -r requirements.txt
```

## Tests

Für das Testing wird in diesem Projekt **pytest** verwendet. Die Tests liegen im Verzeichnis **tests** ab.
Die Konfiguration der Tests wird im File **tests/pytest.ini** vorgenommen.

Die Tests können durch folgenden Befehl durchgeführt werden:
```
(venv) >> python -m pytest
```

Desweiteren wird das Linting des Codes mit **pylint** überprüft. Dies kann durch folgenden Befehl getestet werden:
```
(venv) >> python -m pylint python/merge
```

## Speicherverbrauch

Um den Speicherverbrauch des Programms zu überprüfen, wird das Modul **memory-profiler** verwendet.

Dazu ist es erforderlich, die Funktion, welche in das Monitoring des Speicherverbrauchs, 

***Anmerkung:*** 

**psutil**, welches im angedachten Modul **memory-profiler** verwendet wird, hat aktuell keinen Wheel für um ihn unter Windows mit Python **3.10.0** installieren zu können (siehe: https://issueexplorer.com/issue/giampaolo/psutil/1994).

## Überlegungen

### Versuch 1

Zuerst wird ein einfacher Test geschrieben, der überprüft, ob die Funktion **merge** das Beispiel der Challenge richtig zurückgeben kann.

Dabei ist zu beachten, dass die Intervalle scheinbar sortiert zurückgebeben werden müssen (sortiert nach kleinstem Startwert).
Da im Beispiel nur positive Intervalle verwendet wurden, wird zuerst der Code auf diesen Anwendungsfall hin entwickelt, später allerdings mit weiteren Tests auch darauf überprüft.

Es gibt in Python zwar Libraries für numerische Operationen (Pandas, NumPy), allerdings möchte ich zuerst die Methode ohne weitere Libraries versuchen um so die Ergebnisse, was Laufzeit und Performance angeht, später vergleichen zu können.

#### Lösungsansatz

Am Beispiel aus der Challenge habe ich versucht, einen Weg ohne zusätzliche Libraries zu probieren - daher lediglich mit Loops & Clauses.

Da die eigentliche Liste der **intervals** nicht veränderbar sein darf, habe ich den Parameter als _tuple_ deklariert.
Die Ergebnisse müssen daher in eine separate Liste geschrieben werden, die ich **result** genannt und als _list_ deklariert habe.

Damit ich nicht Werte aus einer Liste löschen muss, die mittendrin gespeichert sind und daher eine Verschiebung des Index nach sich ziehen würden, habe ich mich dafür entschieden, die eingehenden **intervals** in eine Liste **intervalsCopy** zu kopieren und diese aufsteigend zu sortieren.

Der kleinste Wert wird als erster Eintrag in **result** gespeichert und damit anfangend gegen die sortierten Intervalle aus der Kopie verglichen. Befindet sich der Anfangs- oder Endwert des Intervals in dem letzten Eintrag von **result** (daher: sie überlappen), wird das Intervall gemerged und als neuer Wert an die Liste angehängt.

Überschneidet sich das Interval nicht mit dem letzten Eintrag von **result**, wird dieser als neuer, letzter Eintrag angehängt.

Da das Ergebnis aus dem Beispiel auch sortiert zu sein scheint, wird nach dem Loop das Ergebnis entsprechend sortiert, bevor es zurückgegeben wird.

#### Vorgang

- Test 1: Beispiel aus der Challenge
    - Testfunktion, welche das Beispiel aus der Challenge überprüft
    - Funktion merge, um die Testfunktion zu bestehen
- Test 2: Richtiger Parametertyp
    - Testfunktion, welche einen Error wirft, wenn _intervals_ keine _list_ ist
    - Funktion merge erweitern um einen TypeError raise
- Test 3: Negative Intevalle
    - Testfunktion, welche negative Intervalle merged
    - Funktion testen und gegebenenfalls erweitern
    - Funktion erweitern, sodass Argumente per CLI übergeben werden können

#### Ergebnis 

- Test 1: Beispiel aus der Challenge
    - Funktion **merge** liefert nach Eingabe von dem in der Challenge beschriebenen Beispiel das richtige Ergebnis:

        ```
        IN: [[25,30],[2,19],[14,23],[4,8]]
        OUT: [[2,23],[25,30]]
        ```
- Test 2: Richtiger Parametertyp
    - Funktion **merge** wirft den gewünschten Fehler aus, wenn etwas anderes als eine _list_ als Parameter für **intervals** verwendet wird:
        ```
        TypeError: Intervals is not a list!
        ```
        Allerdings muss aktuell noch das Argument im File angegeben werden, statt als Argument in der CLI.
        
- Test 3: Negative Intervalle
    - Funktion **merge** kann ohne weitere Modifikation negative Intervalle verarbeiten und mergen.
    - Argumente können jetzt per CLI übergeben werden