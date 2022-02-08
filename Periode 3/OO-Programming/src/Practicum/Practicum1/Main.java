package Practicum.Practicum1;

public class Main {
    public static void main(String[] args) {

        // OPDR 1
        for (int i = 1; i < 11; i++) {  // List of numbers 1-10
            System.out.println("Count is: " + i);  // Prints number
        }

        // OPDR 2
        int count = 1;  // counting number
        while (count < 11) {  // count to 10
            System.out.println("Count is: " + count);  // Prints number
            count++;  // Equivalent to Python's count += 1
        }

        // OPDR 3
        for (int i = 1; i < 11; i++) {  // List of numbers 1-10
            System.out.println("Count is: " + Math.rint(Math.random() * 10));  // Prints rnumber 1.0-10.0
        }

        // OPDR 4
        int loopcount = 39;
        int counter = 1;
        int answer = 0;
        while (counter <= loopcount) {
            answer += counter;
            counter++;
        }
        System.out.println("Antwoord: " + answer);

        // OPDR 5
        for (int i = 1; i < 5; i++) {  // List of numbers
            if (i % 2 == 1) {
                System.out.println("s");
            } else {
                System.out.println("ss");
            }
        }
    }
}
