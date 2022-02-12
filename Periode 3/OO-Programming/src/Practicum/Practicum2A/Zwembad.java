package Practicum.Practicum2A;

// Zwembad z1 = new Zwembad(2.0, 5.5, 1.5); constructor met parameters nodig
// Zwembad z2 = new Zwembad( ); constructor zonder parameters met default waardes nodig
public class Zwembad {
    private double breedte = 0.0;
    private double lengte = 0.0;
    private double diepte = 0.0;

    /**
     * @param breedte zet de breedte van het zwembad
     * @param lengte zet de lengte van het zwembad
     * @param diepte zet de diepte van het zwembad
     */
    public Zwembad(double breedte, double lengte, double diepte) {
        this.breedte = breedte; // 'this' is een verwijzing naar het huidige object
        this.lengte = lengte;
        this.diepte = diepte;
    }

    /**
     * deze methode maakt een nieuw zwembad aan met default waarden 0.0
     */
    public Zwembad() {
        breedte = 0.0;
        lengte = 0.0;
        diepte = 0.0;
    }

    /**
     * @return de breedte van het zwembad
     */
    public double getBreedte() {
        return breedte;
    }

    /**
     * @return de breedte van het zwembad
     */
    public double getLengte() {
        return lengte;
    }

    /**
     * @return de breedte van het zwembad
     */
    public double getDiepte() {
        return diepte;
    }

    /**
     * @param breete zet de breedte van het zwembad
     */
    public void setBreedte(double breete) {
        this.breedte = breete;
    }

    /**
     * @param lengte zet de lengte van het zwembad
     */
    public void setLengte(double lengte) {
        this.lengte = lengte;
    }

    /**
     * @param diepte zet de diepte van het zwembad
     */
    public void setDiepte(double diepte) {
        this.diepte = diepte;
    }

    /**
     * @return de oppervlakte van het zwembad
     */
    public double inhoud() {
        return lengte * breedte * diepte;
    }

    /**
     * @return informatie over het zwembad
     */
    public String toString() {
        return "Dit zwembad is " + breedte + " meter breed, " + lengte + " meter lang, en " + diepte + " meter diep";
    }
}