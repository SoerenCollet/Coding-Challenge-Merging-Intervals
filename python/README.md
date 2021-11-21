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

## Überlegungen

### Versuch 1

Zuerst wird ein einfacher Test geschrieben, der überprüft, ob die Funktion **merge** das Beispiel der Challenge richtig zurückgeben kann.

Dabei ist zu beachten, dass die Intervalle scheinbar sortiert zurückgebeben werden müssen (sortiert nach kleinstem Startwert).
Da im Beispiel nur positive Intervalle verwendet wurden, wird zuerst der Code auf diesen Anwendungsfall hin entwickelt.

Es gibt in Python zwar Libraries für numerische Operationen (Pandas, NumPy), allerdings möchte ich zuerst die Methode ohne weitere Libraries versuchen um so die Ergebnisse, was Laufzeit und Performance angeht, später vergleichen zu können.