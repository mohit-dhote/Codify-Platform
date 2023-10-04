// Given two linked lists, the task is to complete the function findIntersection(), that returns the intersection of two linked lists. Each of the two linked list contains distinct node values.

// Example 1:

// Input:
// LinkedList1: 9->6->4->2->3->8
// LinkedList2: 1->2->8->6
// Output: 6 2 8

// Problem Link: https://practice.geeksforgeeks.org/problems/intersection-of-two-linked-list/1
// Code:

class Solution
{
    public static Node findIntersection(Node head1, Node head2)
    {
        // add your code here
        // return the head of intersection list\
        Node intersection=new Node(2);
        Node run=intersection;
        
        HashSet<Integer> set=new HashSet<>();
        Node temp=head2;
        while(temp!=null){
            set.add(temp.data);
            temp=temp.next;
        }
        
        Node temp2=head1;
        while(temp2!=null){
            if(set.contains(temp2.data)){
                temp=new Node(temp2.data);
                run.next=temp;
                run=temp;
            }
                temp2=temp2.next;
        }
        
            return intersection.next;
    }
}
