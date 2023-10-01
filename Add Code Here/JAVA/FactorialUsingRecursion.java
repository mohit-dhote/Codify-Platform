import java.util.Scanner;
public class FactorialUsingRecursion {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        System.out.print("Enter a number: ");
        System.out.print("The factorial of " + n + "is : " );
        System.out.println(Fact(n)); 
    }

    static int Fact (int n){
        if(n==1){
            return 1;
        }
        else{
            // System.out.println(n);
            return (n * Fact(n-1));
        }
    }
}
