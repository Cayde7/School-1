package Practicum.Practicum3A;

import jdk.jfr.Description;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class VoetbalclubTest {

    // Eis 1: als de clubnaam null of leeg ("") is, moet de naam "FC" gebruikt worden.
    @Test
    @DisplayName("Check empty club name")
    void testLegeNaam() {
        // Create new club
        Voetbalclub vcu = new Voetbalclub("");

        // Check if club name is FC
        assertEquals("FC", vcu.getNaam());
    }

    @Test
    @DisplayName("Processing of game results")
    @Description("Check if the results are processed correctly")
    void testVerwerkenResultaat() {
        // Create new club
        Voetbalclub vcu = new Voetbalclub("FC Utrecht");

        vcu.verwerkResultaat('w');// Process and check win result
        assertEquals(3, vcu.aantalPunten());
        vcu.verwerkResultaat('g');// Process and check draw result
        assertEquals(4, vcu.aantalPunten());
        vcu.verwerkResultaat('v'); // Process and check loss result
        assertEquals(4, vcu.aantalPunten());
        vcu.verwerkResultaat('x');// Check wrong ch input
        assertEquals(4, vcu.aantalPunten());
        // Check if the string representation is correct
        assertEquals("FC Utrecht 3 1 1 1 4", vcu.toString());

        // Repeats the same test with a new club multiple times
        Voetbalclub vcg = new Voetbalclub("FC Groningen");
        vcg.verwerkResultaat('w'); // Process and check win result
        assertEquals(3, vcg.aantalPunten());
        vcg.verwerkResultaat('g'); // Process and check draw result
        assertEquals(4, vcg.aantalPunten());
        vcg.verwerkResultaat('v'); // Process and check loss result
        assertEquals(4, vcg.aantalPunten());
        vcg.verwerkResultaat('x'); // Check wrong ch input
        assertEquals(4, vcg.aantalPunten());
        vcg.verwerkResultaat('w'); // Process and check win result 2
        assertEquals(7, vcg.aantalPunten());
        vcg.verwerkResultaat('g'); // Process and check draw result 2
        assertEquals(8, vcg.aantalPunten());
        vcg.verwerkResultaat('v'); // Process and check loss result 2
        assertEquals(8, vcg.aantalPunten());
        vcg.verwerkResultaat('x'); // Check wrong ch input 2
        assertEquals(8, vcg.aantalPunten());
        // Check if the string representation is correct
        assertEquals("FC Groningen 6 2 2 2 8", vcg.toString());

    }
}