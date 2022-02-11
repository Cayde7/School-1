package Practicum.Practicum1;

public class Main {
    public static void main(String[] args) {

        // OPDR 1
        System.out.println("--------------------\nOpdracht 1 - print list of numbers 1-10 with for loop\n");
        for (int i = 1; i < 11; i++) {  // List of numbers 1-10
            System.out.println("Count is: " + i);  // Prints number
        }

        // OPDR 2
        System.out.println("--------------------\nOpdracht 2 - print list of numbers 1-10 with while loop\n");
        int count = 1;  // counting number
        while (count < 11) {  // count to 10
            System.out.println("Count is: " + count);  // Prints number
            count++;  // Equivalent to Python's count += 1
        }

        // OPDR 3
        System.out.println("--------------------\nOpdracht 3 - print list of random numbers (0.0-1.0) 10 times\n");
        for (int i = 1; i < 11; i++) {  // List of numbers 1-10
            System.out.println("Count is: " + Math.random());  // Prints rnumber 1.0-10.0
        }

        // OPDR 4
        System.out.println("--------------------\nOpdracht 4 - print an answer with all numbers below and equal to 39 added up (780 total)\n");
        int loopcount = 39;
        int counter = 1;
        int answer = 0;
        while (counter <= loopcount) {
            answer += counter;
            counter++;
        }
        System.out.println("Antwoord: " + answer);

        // OPDR 5
        System.out.println("--------------------\nOpdracht 5 - print a saw pattern with the letter S\n");
        for (int i = 1; i < 5; i++) {  // List of numbers
            if (i % 2 == 1) {
                System.out.println("s");
            } else {
                System.out.println("ss");
            }
        }
    }
}
