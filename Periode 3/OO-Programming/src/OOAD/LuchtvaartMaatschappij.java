package OOAD;

public class LuchtvaartMaatschappij {
    private String naam;
    private ArrayList<Vliegtuig> vliegtuigen;

    public String getLuchtvaartmaatschappij (){
        return this.naam;
    }

    public void luchtvaartmaatschappij(String naam){
        this.naam = naam;
    }

    public void addVliegtuig (Vliegtuig vt){
        vliegtuigen.add(vt);
    }

    public ArrayList<Vliegtuig>(){return this.Vliegtuigen;}

}
