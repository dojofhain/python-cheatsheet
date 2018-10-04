Styling (Aussehen)
------------------

Die meisten Widgets lassen sich in ihrem Aussehen beeinflussen. Dies kann entweder beim Erstellen passieren:

.. code-block:: python

    label = Label(master=fenster, background="red")

oder zu einem späteren Zeitpunkt über die ``config()`` Methode:

.. code-block:: python

    label.config(background="red")


Eigenschaften
"""""""""""""

Im folgenden sind die wichtigsten Eigenschaften aufgelistet, die für alle Widgets gesetzt werden können.

.. list-table::
    :widths: 3 2
    
    * - .. code-block:: python

            # Hintergrundfarbe setzen
            # Farben können durch ihren Namen angegeben werden
            widget.config(background="red")

      - .. figure:: styling_background.png

    * - .. code-block:: python

            # Vordergrundfarbe (Textfarbe) setzen
            # Farben können durch ihre RGB-Werte angegeben werden
            widget.config(foreground="#00AA00")

      - .. figure:: styling_foreground.png

    * - .. code-block:: python

            # Zeichensatz (Font) setzen
            # Das Tuple kann 3 Werte enthalten:
            # 1. Schriftart ("Courier", "Helvetica", "Times")
            # 2. Schriftgröße
            # 3. Schriftschnitt ("bold", "italic", "underline", "normal")
            widget.config(font=("Helvetica", 40, "bold"))

      - .. figure:: styling_font.png

    * - .. code-block:: python

            # Für mehrzeiligen Text kann die Ausrichtung gesetzt werden
            # mögliche Werte: "left", "center", "right"
            widget.config(justify="right")

      - .. figure:: styling_justify_right.png
