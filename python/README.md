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
(venv) >> python -m pytest -v
```

Desweiteren wird das Linting des Codes mit **pylint** überprüft. Dies kann durch folgenden Befehl getestet werden:
```
(venv) >> python -m pylint python/merge
```

## Laufzeit

Für die Ermittlung der Laufzeit des Codes wird der *Default Timer* von **timeit** verwendet.

## Speicherverbrauch

Um den Speicherverbrauch des Programms zu überprüfen, wird das Modul **guppy3** verwendet.

~~Um den Speicherverbrauch des Programms zu überprüfen, wird das Modul **memory-profiler** verwendet.~~

***Anmerkung:*** 

**psutil**, welches im angedachten Modul **memory-profiler** verwendet wird, hat aktuell keinen Wheel für um ihn unter Windows mit Python **3.10.0** installieren zu können (siehe: https://issueexplorer.com/issue/giampaolo/psutil/1994). Daher wird die Alternative **guppy3** verwendet.

## Überlegungen

### Versuch

Zuerst wird ein einfacher Test geschrieben, der überprüft, ob die Funktion **merge** das Beispiel der Challenge richtig zurückgeben kann.

Dabei ist zu beachten, dass die Intervalle scheinbar sortiert zurückgebeben werden müssen (sortiert nach kleinstem Startwert).
Da im Beispiel nur positive Intervalle verwendet wurden, wird zuerst der Code auf diesen Anwendungsfall hin entwickelt, später allerdings mit weiteren Tests auch darauf überprüft.

Es gibt in Python zwar Libraries für numerische Operationen (Pandas, NumPy), allerdings möchte ich die Funktion ohne das Einbinden weiterer Libraries (für die Funktion merge) versuchen.

#### Lösungsansatz

Am Beispiel aus der Challenge habe ich versucht, einen Weg ohne zusätzliche Libraries zu probieren - daher lediglich mit Loops & Clauses.

Da die eigentliche Liste der **intervals** nicht veränderbar sein darf, habe ich den Parameter als _tuple_ deklariert.
Die Ergebnisse müssen daher in eine separate Liste geschrieben werden, die ich **result** genannt und als _list_ deklariert habe.

Damit ich nicht Werte aus einer Liste löschen muss, die mittendrin gespeichert sind und daher eine Verschiebung des Index nach sich ziehen würden, habe ich mich dafür entschieden, die eingehenden **intervals** in eine Liste **intervalsCopy** zu kopieren und diese aufsteigend zu sortieren.

Der kleinste Wert wird als erster Eintrag in **result** gespeichert und damit anfangend gegen die sortierten Intervalle aus der Kopie verglichen. Befindet sich der Anfangs- oder Endwert des Intervals in dem letzten Eintrag von **result** (daher: sie überlappen), wird das Intervall gemerged und als neuer Wert an die Liste angehängt.

Überschneidet sich das Intervall nicht mit dem letzten Eintrag von **result**, wird dieser als neuer, letzter Eintrag angehängt.

Da das Ergebnis aus dem Beispiel auch sortiert zu sein scheint, wird nach dem Loop das Ergebnis entsprechend sortiert, bevor es zurückgegeben wird.

#### Vorgang

- **Test 1**: Beispiel aus der Challenge
    - Testfunktion, welche das Beispiel aus der Challenge überprüft
    - Funktion merge, um die Testfunktion zu bestehen

- **Test 2**: Richtiger Parametertyp
    - Testfunktion, welche einen Error wirft, wenn _intervals_ keine _list_ ist
    - Funktion merge erweitern um einen TypeError raise

- **Test 3**: Negative Intevalle
    - Testfunktion, welche negative Intervalle merged
    - Funktion testen und gegebenenfalls erweitern
    - Funktion erweitern, sodass Argumente per CLI übergeben werden können

- **Test 4**: 2 Werte pro Intervall
    - Testfunktion, welche überprüft, ob ein Errror ausgegeben wird, wenn das Intervall nicht exact 2 Werte beinhaltet
    - Funktion wird aktuell fehl schlagen, weshalb der Error abgefangen werden muss
    - Fehlermeldung entsprechend nach dem Typ des Fehlers (ValueError)

- **Test 5**: Startwert größer als Endwert
    - Testfunktion, welche überprüft, ob ein Errror ausgegeben wird, wenn der Startwert größer als der Endwert ist
    - Funktion wird aktuell fehl schlagen, weshalb der Error abgefangen werden muss
    - Fehlermeldung entsprechend nach dem Typ des Fehlers (ValueError)

- **Test 6**: Mindestens 2 Intervalle
    - Testfunktion, welche überprüft, ob ein Errror ausgegeben wird, wenn nicht mindestens 2 Intervalle übergeben wurden
    - Funktion wird durchlaufen, aber damit nicht die gewünschte Funktion erfüllen
    - Fehlermeldung entsprechend nach dem Typ des Fehlers (ValueError)

- **Test 7**: Große Anzahl an Intervallen
    - Testfunktion, welche überprüft, ob die Funktion eine große Anzahl (1000000) an Intervallen abarbeiten kann
    - Überprüfen, wie die Durchlaufzeit ist und gegebenenfalls Maßnahmen ergreifen, um die Zeit zu verkürzen

- **Test 8**: Großer Intervallbereich
    - Testfunktion, welche überprüft, ob die Funktion Intervalle mit großem Bereich (z.B [1,10000000000]) abarbeiten kann
    - Überprüfen, wie die Durchlaufzeit ist und gegebenenfalls Maßnahmen ergreifen, um die Zeit zu verkürzen

#### Ergebnis 

- **Test 1**: Beispiel aus der Challenge
    - Test schlägt zuerst fehl, da die Funktionalität bisher nicht implementiert wurde -> Funktion **merge** wird erstellt
    - Funktion **merge** liefert nach Eingabe von dem in der Challenge beschriebenen Beispiel das richtige Ergebnis:

        ```
        IN: [[25,30],[2,19],[14,23],[4,8]]
        OUT: [[2,23],[25,30]]
        ```
- **Test 2**: Richtiger Parametertyp
    - Test schlägt zuerst fehl, da der Fehler nicht abgefangen wird -> TypeError wird geraised und gehandelt
    - Funktion **merge** wirft den gewünschten Fehler aus, wenn etwas anderes als eine _list_ als Parameter für **intervals** verwendet wird:
        ```
        TypeError: Intervals is not a list!
        ```
    - ~~Da der Error schon im try-catch Block gehandelt wird, wird nicht der raise übergeben, weshalb die Fehlermeldung von pytest statt dem eigentlichen Raise überprüft wird (```with raises(TypeError)```), was für alle anderen Error Handler auch gilt~~
    - Try-Catch-Block wurde in den Run gelegt, sodass Funktion **merge** Fehler autark übersenden kann. Somit kann auch der entsprechende *Type/ValueError raise* in pytest abgefangen werden, statt dem User Feedback
    - Allerdings muss aktuell noch das Argument im File angegeben werden, statt als Argument in der CLI
        
- **Test 3**: Negative Intervalle
    - Funktion **merge** kann ohne weitere Modifikation negative Intervalle verarbeiten und mergen.
    - Argumente können jetzt per CLI übergeben werden

- **Test 4**: 2 Werte pro Intervall
    - Test schlägt zuerst fehl, da der Fehler nicht abgefangen wird -> ValueError wird geraised und gehandelt
    - Funktion **merge** wirft den gewünschten Fehler aus, wenn Intervalle nicht exakt 2 Werte besitzen:
        ```
        ValueError: Please provide valid intervals!
        An interval has exact 2 values.
        ```

- **Test 5**: Startwert größer als Endwert
    - Test schlägt zuerst fehl, da der Fehler nicht abgefangen wird -> ValueError wird geraised und gehandelt
    - Funktion **merge** wirft den gewünschten Fehler aus, wenn der Startwert größer als der Endwert ist:
        ```
        ValueError: Please provide valid intervals!
        The starting interval should not be higher then the ending interval.
        ```

- **Test 6**: Mindestens 2 Intervalle
    - Test läuft durch, allerdings wurde die Funktion, dass mehrere Intervalle gemerged werden sollen, nicht erfüllt -> ValueError wird geraised und gehandelt
    - Funktion **merge** wirft den gewünschten Fehler aus, wenn nicht mindestens 2 Intervalle übergeben wurden:
        ```
        ValueError: Please provide at least 2 intervals to merge!
        ```

- **Test 7**: Große Anzahl an Intervallen
    - Der Testlauf dauert 10 Sekunden mit einer Anzahl von 1000000 Intervallen
    - Speicherverbrauch steigt nicht an während der Laufzeit
    - Der User benötigt ein Feedback, damit er weiß, dass das Programm noch lauffähig ist. Daher wurde ein Spinner integriert, der durch einen context manager verwaltet wird. So ist der Status des aktuellen Laufs für den User nachvollziehbarer und damit die Robustheit des Programms erhöht
    ![Merging many intervals](https://i.imgur.com/G9dlvxL.gif)

- **Test 8**: Großer Intervallbereich
    - Der Test läuft unter einer Sekunde erfolgreich durch
    - Speicherverbrauch steigt nicht unerwartet an