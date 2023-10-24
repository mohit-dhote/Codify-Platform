#include <iostream>
using namespace std;


//using recursion
double e1(int x, int n)
{
    static double p = 1, f = 1;
    double r;

    if (n == 0)
        return 1;
    
    r = e1(x, n - 1);
    p *= x;
    f *= n;
 
    return r + p / f;
}

//using recursion - horner's rule
double e2(int x, int n)
{
    //cout << n << " in\n"; - thanks to boiiii#8502 14.06.23
    static double s;
    if (n == 0)
        return s;
    s = 1 + x * s / n;
    return e2(x, n - 1);
}

//using loop
double e3(int x, int n)
{
    double s = 1;
    int i;
    double num = 1;
    double den = 1;

    for (i = 1; i <= n; i++)
    {
        num *= x;
        den *= i;
        s += num / den;
    }
    return s;
}


int main()
{
    //using recursion
    printf("%lf \n", e1(2, 10));

    //using recursion - horner's rule
    printf("%lf \n", e2(2, 10));

    //using loop
    printf("%lf \n", e3(2, 10));
    return 0;
}
