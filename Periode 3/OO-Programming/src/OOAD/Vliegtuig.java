package OOAD;

public class Vliegtuig {
    private String naam;
    private LocalDate datumInGebruik;
    private Luchtvaartmaatschappij lvm;
    private VliegtuigType VliegtuigType;

    public Vliegtuig(Luchtvaartmaatschappij lvm) {
        this.lvm = lvm;
    }

    private void zetVliegtuigType (VliegtuigType type) {
        this.vliegtuigType = type;

    }

    private LocalDate geefDatumInGebruik() {
        return this.datumInGebruik;
    }

    public void bewaar(){
        //... database
    }

}
