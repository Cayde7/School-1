package OOAD;

public class VliegtuigType {
    private String code;
    private Integer capaciteit;
    private Fabrikant fabrikant;

    public VliegtuigType(Fabrikant fabrikant, String code, Integer capaciteit) {

    }

    public int geefCapaciteit(){
        return this.capaciteit;
    }
}
