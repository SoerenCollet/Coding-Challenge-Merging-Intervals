# Python Lösung

## Methode

Es wird nach TDD (Test Driven Development) entwickelt.

## Überlegungen

### Versuch 1

Zuerst wird ein einfacher Test geschrieben, der überprüft, ob die Funktion **merge** das Beispiel der Challenge richtig zurückgeben kann.

Dabei ist zu beachten, dass die Intervalle scheinbar sortiert zurückgebeben werden müssen (sortiert nach kleinstem Startwert).
Da im Beispiel nur positive Intervalle verwendet wurden, wird zuerst der Code auf diesen Anwendungsfall hin entwickelt.

Es gibt in Python zwar Libraries für numerische Operationen (Pandas, NumPy), allerdings möchte ich zuerst die Methode ohne weitere Libraries versuchen um so die Ergebnisse, was Laufzeit und Performance angeht, später vergleichen zu können.