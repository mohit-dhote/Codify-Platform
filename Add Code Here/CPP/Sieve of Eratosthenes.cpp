
#include <bits/stdc++.h>

using namespace std;

int main()
{
    // Sieve of Eratosthenes
    //Given an integer n, return the number of prime numbers that are strictly less than n.
    int n;
    cin>>n;
    vector<bool>seen(n,true);
    int count=0;
    for(int i=2; i<n; i++)
    {
        if(seen[i])
        {
            count++;
            for(int j=i+i; j<n; j+=i)
            {
                seen[j]=false;
            }
        }
    }
    cout<<count;

    return 0;
}
