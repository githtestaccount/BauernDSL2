def kauf(viehzeug, anzahl, preis):
    gesamtpreis = str(int(preis)*int(anzahl))
    print("Du kaufst Dir " + anzahl + " " + viehzeug + "e für " + gesamtpreis + " Euro.")

def verkauf(viehzeug, anzahl, preis):
    gesamtpreis = str(int(preis)*int(anzahl))
    print("Du verkaufst " + anzahl + " " + viehzeug + "e für " + gesamtpreis + " Euro.")
