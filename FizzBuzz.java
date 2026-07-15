/**
 * FizzBuzz
 * Print numbers 1..n, replacing multiples of 3 with "Fizz", multiples of 5
 * with "Buzz", and multiples of both with "FizzBuzz".
 *
 * A classic warm-up for control flow and modulo logic.
 */
public class FizzBuzz {
    public static void run(int n) {
        for (int i = 1; i <= n; i++) {
            if (i % 15 == 0) {
                System.out.println("FizzBuzz");
            } else if (i % 3 == 0) {
                System.out.println("Fizz");
            } else if (i % 5 == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println(i);
            }
        }
    }

    public static void main(String[] args) {
        run(20);
    }
}
