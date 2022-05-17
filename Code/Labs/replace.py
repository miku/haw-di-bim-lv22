
text = """
Ueber einen kurzen Aufenthalt in Berlin, wohin er 1778 den Herzog von
Weimar begleitete, schrieb Goethe an Merk: "Ich war nur wenige Tage in
Berlin, und guckte nur drein, wie das Kind in den Schön-Raritäten-Kasten.
Aber du weißt, wie ich im Anschauen lebe; es sind mir tausend Lichter
aufgegangen. Und dem alten Fritz bin ich recht nahe worden; da hab' ich
sein Wesen gesehen, sein Gold, Silber, Marmor, Affen, Papageien und
zerrissene Vorhänge, und habe über den großen Menschen seine eignen
Lumpenhunde räsonniren hören. Die Generäle, die ich halbdutzendweise bei
Tisch mir gegenüber gehabt, machen mir den jetzigen König gegenwärtiger.
Mit Menschen hab' ich sonst gar nichts zu verkehren gehabt, und habe in
preußischen Staaten kein laut Wort hervorgebracht, daß sie nicht könnten
drucken lassen, dafür ich gelegentlich als stolz u.s.w. ausgeschrieen
worden bin."
"""

articles = ["Berlin", "Weimar", "Gold", "Marmor"]
base = "https://de.wikipedia.org/wiki/"

for line in text.split('\n'):
    updated = line
    for name in articles:
        updated = updated.replace(name, f"[{name}]({base}{name})")
    print(updated)

