import java.util.Arrays;

/**
 * Bubble Sort
 * Repeatedly steps through the array, swapping adjacent elements that are
 * out of order. Simple to implement, useful for demonstrating O(n^2)
 * sorting and early-exit optimization.
 *
 * Time: O(n^2) worst case, O(n) best case (already sorted)
 * Space: O(1)
 */
public class BubbleSort {
    public static void sort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false;
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            if (!swapped) break; // already sorted, stop early
        }
    }

    public static void main(String[] args) {
        int[] data = {5, 2, 9, 1, 5, 6};
        sort(data);
        System.out.println(Arrays.toString(data)); // [1, 2, 5, 5, 6, 9]
    }
}
