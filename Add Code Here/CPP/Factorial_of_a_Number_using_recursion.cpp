#include <iostream>
using namespace std;

//using recursion
int fact1(int n)
{
    if (n == 0) 
        return 1;

    return fact1(n - 1) * n;
}

//using loops
int fact2(int n)
{
    int i, f=1;
    for (i = 1; i <= n; i++)
        f *= i;
    return f;
}


int main()
{
    cout << "Factorial of a number" << endl;
    
    //using recursion
    cout << "Using recursion : " <<  fact1(5) << endl;
    
    //using loop
    cout << "Using loop : " <<  fact2(5) << endl;
}
