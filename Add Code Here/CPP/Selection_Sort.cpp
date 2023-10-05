#include <bits/stdc++.h>
using namespace std;
void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

// https://practice.geeksforgeeks.org/problems/selection-sort/1?

class Solution
{
    public:
    int select(int arr[], int i, int n)
    {
        // code here such that selectionSort() sorts arr[]
        int mini=i;
        for(int j=i+1;j<n;j++){
            if(arr[j]<arr[mini])
                mini=j;
        }
        return mini;
    }
     
    void selectionSort(int arr[], int n)
    {
        int mini;
       for(int i=0;i<n-1;i++){
           mini=select(arr,i,n);
           swap(arr[i],arr[mini]);
       }
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
    int arr[1000],n,T,i;
  
    scanf("%d",&T);
    
    while(T--){
        
    scanf("%d",&n);
    
    for(i=0;i<n;i++)
      scanf("%d",&arr[i]);
      
    Solution ob;  
    ob.selectionSort(arr, n);
    printArray(arr, n);
    }
    return 0;
}