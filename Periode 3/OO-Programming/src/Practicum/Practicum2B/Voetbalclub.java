package Practicum.Practicum2B;

public class Voetbalclub {
    private String naam;
    private int aantalGewonnen;
    private int aantalGelijk;
    private int aantalVerloren;

    // Constructor
    public Voetbalclub(String naam) {
        this.naam = naam;
    }

    /**
     * @param ch de te verwerken resultaat,
     *           verwerkt het resultaat van een wedstrijd en zet de punten bij de voetbalclub in de juiste variabelen
     */
    public void verwerkResultaat(char ch) {
        if (ch == 'w')
            aantalGewonnen = aantalGewonnen + 1;
        if (ch == 'g')
            aantalGelijk = aantalGelijk + 1;
        if (ch == 'v')
            aantalVerloren = aantalVerloren + 1;
    }

    /**
     * @return het aantal punten dat de voetbalclub heeft
     */
    public int aantalPunten() {
        int punten = 0;
        punten += 3 * aantalGewonnen;
        punten += aantalGelijk;
        return punten;
    }

    /**
     * @return het aantal gespeelde wedstrijden
     */
    public int aantalGespeeld() {
        return aantalGewonnen + aantalGelijk + aantalVerloren;
    }

    /**
     * @return string met naam van de voetbalclub, gespeeld, gewonnen, gelijk, verloren en punten van de voetbalclub
     */
    public String toString() {
        // Naam gespeeld gewonnen gelijk verloren punten
        return naam + " " + aantalGespeeld() + " " + aantalGewonnen + " " + aantalGelijk + " " + aantalVerloren + " " + aantalPunten();
    }
}
