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

// https://practice.geeksforgeeks.org/problems/merge-sort/1?

class Solution
{
    public:
    void merge(int arr[], int l, int m, int r)
    {
         int i=l,j=m+1,k=l,b[100001];
         while(i<=m && j<=r){
             if(arr[i]<arr[j]){
                 b[k]=arr[i];
                 i++;
                 k++;
             }
             else{
                 b[k]=arr[j];
                 j++;
                 k++;
             }
         }
         while(i<=m){
             b[k]=arr[i];
             i++;
             k++;
         }
         while(j<=r){
             b[k]=arr[j];
             j++;
             k++;
         }
         for(int i=l;i<=r;i++)
            arr[i]=b[i];
    }
    public:
    void mergeSort(int arr[], int l, int r)
    {
        int mid;
        if(l<r){
            mid=l+(r-l)/2;
            mergeSort(arr,l,mid);
            mergeSort(arr,mid+1,r);
            merge(arr,l,mid,r);
        }
    }
};


int main()
{
    int n,T,i;

    scanf("%d",&T);

    while(T--){
    
    scanf("%d",&n);
    int arr[n+1];
    for(i=0;i<n;i++)
      scanf("%d",&arr[i]);

    Solution ob;
    ob.mergeSort(arr, 0, n-1);
    printArray(arr, n);
    }
    return 0;
}