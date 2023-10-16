import java.util.Scanner;

public class GnomeSort {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of elements: ");
        int n = scanner.nextInt();

        int[] arr = new int[n];
        System.out.println("Enter " + n + " elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }

        gnomeSort(arr);

        System.out.println("Sorted array:");
        printArray(arr);
    }

    // Function to print an array
    static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    // Function to perform Gnome Sort
    static void gnomeSort(int[] arr) {
        int n = arr.length;
        int index = 0;

        while (index < n) {
            if (index == 0) {
                index++;
            }

            if (arr[index] >= arr[index - 1]) {
                index++;
            } else {
                int temp = arr[index];
                arr[index] = arr[index - 1];
                arr[index - 1] = temp;
                index--;
            }
        }
    }
}
