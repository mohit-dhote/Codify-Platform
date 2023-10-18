//Problem: Finding the Longest Increasing Subsequence (LIS)
//Description:
//Given an unsorted array of integers, find the length of longest increasing subsequence.


#include <iostream>
#include <vector>
using namespace std;

int longestIncreasingSubsequence(vector<int>& arr) {
    int n = arr.size();
    vector<int> dp(n, 1);

    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (arr[i] > arr[j] && dp[i] < dp[j] + 1) {
                dp[i] = dp[j] + 1;
            }
        }
    }

    int maxLen = 0;
    for (int i = 0; i < n; i++) {
        if (dp[i] > maxLen) {
            maxLen = dp[i];
        }
    }

    return maxLen;
}

int main() {
    vector<int> arr = {10, 22, 9, 33, 21, 50, 41, 60, 80};
    int lisLength = longestIncreasingSubsequence(arr);

    cout << "Length of Longest Increasing Subsequence: " << lisLength << endl;

    return 0;
}
