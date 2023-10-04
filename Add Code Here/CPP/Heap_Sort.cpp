#include <bits/stdc++.h>
using namespace std;

// https://practice.geeksforgeeks.org/problems/heap-sort/1?

class Solution
{
    public:
    //Heapify function to maintain heap property.
    void heapify(int arr[], int n, int i)  
    {
      // Your Code Here
        int largest=i;
        int left=2*i;
        int right=(2*i)+1;
        
        if(left<=n && arr[left]>arr[largest])
            largest=left;
        if(right<=n && arr[right]>arr[largest])
            largest=right;
        
        if(largest!=i){
            swap(arr[largest],arr[i]);
            heapify(arr,n,largest);
        }
    }

    
    public:
    //Function to sort an array using Heap Sort.
    void heapSort(int arr[], int n)
    {
        //code here
        int b[n+1];
        for(int i=1;i<=n;i++)
            b[i]=arr[i-1];
        
        for(int i=n/2;i>=1;i--)
            heapify(b,n,i);
        
        for(int i=n;i>=1;i--){
            swap(b[i],b[1]);
            heapify(b,i-1,1);
        }
        
        for(int i=1;i<=n;i++)
            arr[i-1]=b[i];
    }
};


/* Function to print an array */
void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}


int main()
{
    int arr[1000000],n,T,i;
    scanf("%d",&T);
    while(T--){
    scanf("%d",&n);
    for(i=0;i<n;i++)
      scanf("%d",&arr[i]);
    Solution ob;
    ob.heapSort(arr, n);
    printArray(arr, n);
    }
    return 0;
}