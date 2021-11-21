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

Sie können über folgenden Befehl ausgeführt werden:
```
(venv) >> python -m pytest python/tests
```

## Speicherverbrauch

Um den Speicherverbrauch des Programms zu überprüfen, wird das Modul **memory-profiler** verwendet.

Dazu ist es erforderlich, die Funktion, welche in das Monitoring des Speicherverbrauchs, 

## Überlegungen

### Versuch 1

Zuerst wird ein einfacher Test geschrieben, der überprüft, ob die Funktion **merge** das Beispiel der Challenge richtig zurückgeben kann.

Dabei ist zu beachten, dass die Intervalle scheinbar sortiert zurückgebeben werden müssen (sortiert nach kleinstem Startwert).
Da im Beispiel nur positive Intervalle verwendet wurden, wird zuerst der Code auf diesen Anwendungsfall hin entwickelt.

Es gibt in Python zwar Libraries für numerische Operationen (Pandas, NumPy), allerdings möchte ich zuerst die Methode ohne weitere Libraries versuchen um so die Ergebnisse, was Laufzeit und Performance angeht, später vergleichen zu können.

#### Vorgang

- Test 1: Beispiel aus der Challenge
    - Testfunktion, welche das Beispiel aus der Challenge überprüft
    - Funktion merge, um die Testfunktion zu bestehen
- Test 2: Richtiger Parametertyp
    - Testfunktion, welche einen Error wirft, wenn _intervals_ keine _list_ ist
    - Funktion merge erweitern um einen TypeError raise

#### Ergebnis 

- Test 1: Beispiel aus der Challenge
    - Funktion **merge** liefert nach Eingabe von dem in der Challenge beschriebenen Beispiel das richtige Ergebnis:

        ```
        IN: [25,30],[2,19],[14,23],[4,8]]
        OUT: [[2,23],[25,30]]
        ```
- Test 2: Richtiger Parametertyp
    - Funktion **merge** wirft den gewünschten Fehler aus, wenn etwas anderes als eine _list_ als Parameter für **intervals** verwendet wird:
        ```
        TypeError: Intervals is not a list!
        ```
        Allerdings muss aktuell noch das Argument im File angegeben werden, statt als Argument in der CLI.