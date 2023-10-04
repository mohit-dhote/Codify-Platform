#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;

/* Function to print an array */
void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

// https://practice.geeksforgeeks.org/problems/quick-sort/1?

class Solution
{
    public:
    //Function to sort an array using quick sort algorithm.
    void quickSort(int arr[], int low, int high)
    {
        int index;
        
        if(low<high){
            index=partition(arr,low,high);
            quickSort(arr,low,index-1);
            quickSort(arr,index+1,high);
        }
        
    }
    
    public:
    int partition (int arr[], int low, int high)
    {
        int i=low,j=high,pivot=arr[low];
        while(i<j){
            while(arr[i]<=pivot)
                i++;
            while(arr[j]>pivot)
                j--;
            if(i<j)
                swap(arr[i],arr[j]);
        }
        swap(arr[low],arr[j]);
        return j;
    }
};

int main()
{
    int arr[1000],n,T,i;
    scanf("%d",&T);
    while(T--){
    scanf("%d",&n);
    for(i=0;i<n;i++)
      scanf("%d",&arr[i]);
      Solution ob;
    ob.quickSort(arr, 0, n-1);
    printArray(arr, n);
    }
    return 0;
}