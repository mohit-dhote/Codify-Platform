#include <bits/stdc++.h>

int findMajorityElement(int arr[], int n) {
	// Write your code here.
		int ele;
	int cnt=0;
	for(int i=0;i<n;i++)
	{
		if(cnt==0)
		{
			ele=arr[i];
			++cnt;
		}
		else if(ele==arr[i])
		++cnt;
		else
		--cnt;

	}
	cnt=0;
	for(int i=0;i<n;i++)
	{
     if(ele==arr[i])
	 ++cnt;
	}
	if(cnt>=n/2+1)
	return ele;
	return -1;
}