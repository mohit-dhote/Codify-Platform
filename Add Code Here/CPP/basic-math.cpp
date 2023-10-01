#include<iostream>
using namespace std;
// Function to add two or more numbers
    double add(int a[], int len){
        double sum = 0;
        for(int i = 0; i < len; i++){
            sum += a[i];
        }
        return sum;
    }
    // Function to subtract between two or more numbers
    double sub(int a[], int len){
        double sum = 0;
        for(int i = 0; i < len; i++){
            sum -= a[i];
        }
        return sum;
    }
    // Function to multiply two or more numbers
    double mul(int a[], int len){
        double sum = 1;
        for(int i = 0; i < len; i++){
            sum *= a[i];
        }
        return sum;
    }
    // Function to divide between two or more numbers
    float div(int a[], int len){
        float sum = 1;
        for(int i = 0; i < len; i++){
            sum /= a[i];
        }
        return sum;
    }
    // Function to find average of two or more numbers
    float avg(int a[], int len){
        float sum = 0;
        for(int i = 0; i < len; i++){
            sum += a[i];
        }
        return sum/len;
    }
int main(){
int a[5] = {1,2,3,5,9};
//cout << add(a, 5) << "\n" << sub(a, 5) << "\n" << mul(a, 5) << "\n" << div(a, 5) << "\n" << avg(a, 5) << endl; For test only
return 0;
}
