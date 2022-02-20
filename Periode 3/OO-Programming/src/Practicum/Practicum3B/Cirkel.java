package Practicum.Practicum3B;

// ┌────────────────────────┐
// │ Cirkel                 │
// ├------------------------┤
// │ -radius : int          │
// │ -xPositie : int        │
// │ -yPositie : int        │
// ├------------------------┤
// │ +Cirkel(int, int, int) │
// │ +toString() : String   │
// └────────────────────────┘

public class Cirkel {
    private Integer radius;
    private Integer xPositie;
    private Integer yPositie;

    public Cirkel(Integer radius, Integer xPositie, Integer yPositie) {
        if (radius <= 0) {
            throw new IllegalArgumentException("Radius moet groter dan 0 zijn!");
        }
        this.radius = radius;
        this.xPositie = xPositie;
        this.yPositie = yPositie;
    }

    public String toString() {
        return "cirkel (" + xPositie + ", " + yPositie + ") met radius: " + radius;
    }



}
