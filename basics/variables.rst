Variablen
---------

Variablen können wir benutzen, um uns Dinge zu merken. Sie haben einen Namen und einen Wert.

>>> mein_name = "Sandra"

Hier haben wir eine Variable mit dem Namen ``mein_name`` angelegt. Sie hat jetzt den Wert ``Sandra``.
Um zu sehen, welchen Wert eine Variable hat, können wir die ``print()`` Funktion benutzen:

>>> print(mein_name)
Sandra

Den Wert einer Variable können wir jederzeit ändern:

>>> mein_name = "Markus"
>>> print(mein_name)
Markus

Der Name der Variable darf aus Buchstaben, Zahlen und dem Unterstrich (_) bestehen. Für normale Variablen solltest Du nur Kleinbuchstaben verwenden.

Alle Variablen haben einen Typ. Um den Typ einer Variable zu erfahren, können wir die ``type()`` Funktion benutzen:

>>> print(type(mein_name))
<class 'str'>

Strings (Texte)
^^^^^^^^^^^^^^^

String-Variablen ('str') können wir benutzen um Texte zu speichern. Den Text, den wir in die Variable speichern, müssen wir dabei in Anführungszeichen schreiben:

>>> mein_vorname = "Markus"
>>> mein_nachname = "Müller"

Wenn wir zwei String-Variablen verbinden wollen, können wir den ``+`` Operator verwenden:

>>> mein_name = mein_vorname + " " + mein_nachname
>>> print(mein_name)
Markus Müller


Integer (Ganzzahlen)
^^^^^^^^^^^^^^^^^^^^

Integer-Variablen ('int') werden benutzt um Ganzzahlen (also ohne Komma) zu speichern.

>>> zahl_1 = 3
>>> zahl_2 = 11
>>> print(type(zahl_1))
<class 'int'>

Mit Integer-Variablen können wir wie in der Mathematik rechnen:

>>> ergebnis = (zahl_1 + zahl_2) * 2
>>> print(ergebnis)
28

Allerdings werden für einige Operationen andere Zeichen verwendet. Für die Multiplikation der ``*`` statt ``•`` und für die Division ``/`` statt ``:``.

>>> 4 * 2
8
>>> 4 / 2
2.0

.. hint::
    Manchmal muß man eine Zahl in einen String umwandeln, dafür kann man die ``str()`` Funktion benutzen.

	>>> alter = 10
	>>> print("Ich bin " + str(alter) + " Jahre alt.")
	Ich bin 10 Jahre alt.


Float (Kommazahlen)
^^^^^^^^^^^^^^^^^^^

Float-Variablen ('float') können gebrochene Zahlen (also mit Komma) speichern. Die mathematischen Operationen funktionieren hier genauso wie bei den Ganzzahlen.

>>> float_1 = 11.23
>>> float_2 = 3.45
>>> print(type(float_1))
<class 'float'>
>>> float_1 / float_2
3.255072463768116

Bool
^^^^

Variablen vom Typ bool können nur zwei Werte annehmen True (richtig) oder False (falsch).

>>> ergebnis = (3 > 2)
>>> print(ergebnis)
True
>>> ergebnis = (5 < 4)
>>> print(ergebnis)
False
>>> print(type(ergebnis))
<class 'bool'>


Listen
^^^^^^

Sehr oft wollen wir mehrere Werte speichern, dafür können wir Listen verwenden. Die Werte schreiben wir dazu in eckige Klammern und trennen sie mit einem Komma:

>>> spieler = [ "Sandra", "Markus", "Jana", "Fritz" ]
>>> print(spieler)
['Sandra', 'Markus', 'Jana', 'Fritz']

Jetzt haben wir eine Variable mit dem Name ``spieler``, in der die 4 Spieler gespeichert sind. Wenn wir uns einen einzelnen Wert anschauen wollen, können wir die Position in eckigen Klammern schreiben:

>>> print(spieler[0])
Sandra
>>> print(spieler[2])
Jana
>>>

.. hint::
    Die Zählung der Position beginnt immer mit der 0. Für den ersten Spieler benutzen wir also die 0, für den zweiten die 1, usw.
