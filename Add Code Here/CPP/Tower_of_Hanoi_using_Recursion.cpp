#include <iostream>
using namespace std;

void TOH(int n, int A=1, int B=2, int C=3)
{
    if (n>0)
    {
        TOH(n - 1, A, C, B);
        printf("(%d,%d)\n", A, C);
        TOH(n - 1, B, A, C);
    }
}

int main()
{
    cout << "Tower of Hanoi!\n\n";
    TOH(4);

}
