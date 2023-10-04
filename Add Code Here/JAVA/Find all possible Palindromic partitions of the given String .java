import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
 
public class Main
{
    public static void main(String[] args)
    {
        String input = "nitin";
        System.out.println("All possible palindrome partitions for " + input+ " are :");
        allPalPartitions(input);
    }
    
    private static void allPalPartitions(String input)
    {
        int n = input.length();
 
        ArrayList<ArrayList> allPart = new ArrayList<>();
 
        Deque currPart = new LinkedList();
 
        allPalPartitonsUtil(allPart, currPart, 0, n, input);
 
        for (int i = 0; i < allPart.size(); i++)
        {
            for (int j = 0; j < allPart.get(i).size(); j++)
            {
                System.out.print(allPart.get(i).get(j) + " ");
            }
            System.out.println();
        }
 
    }
 
    private static void allPalPartitonsUtil(ArrayList<ArrayList> allPart,
    Deque currPart, int start, int n, String input)
    {
        if (start >= n)
        {
            allPart.add(new ArrayList<>(currPart));
            return;
        }
 
        for (int i = start; i < n; i++)
        {
            if (isPalindrome(input, start, i))
            {
                currPart.addLast(input.substring(start, i + 1));
                allPalPartitonsUtil(allPart, currPart, i + 1, n, input);
                currPart.removeLast();
            }
        }
    }
 
    private static boolean isPalindrome(String input,int start, int i)
    {
        while (start < i)
        {
            if (input.charAt(start++) != input.charAt(i--))
                return false;
        }
        return true;
    }
}
