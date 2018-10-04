Das Modul ``tkinter`` können wir benutzen, um grafische Bedienoberflächen zu programmieren.


Fenster
-------

Als erstes erzeugen wir ein Fenster, in dem wir die Elemente unseres Programs anordnen können.


.. code-block:: python
    :linenos:

    from tkinter import *           # das modul tkinter wird importiert

    fenster = Tk()                  # ein Fenster wird erzeugt
    fenster.title("Hallo Welt")     # wir setzen den Titel des Fensters

    fenster.mainloop()              # wir starten die Anwendung

.. image:: window.png
    :align: right

So ungefähr sieht das Ergebnis aus: 

|br|

