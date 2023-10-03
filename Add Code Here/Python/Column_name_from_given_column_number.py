# GFG problem
# Link: https://practice.geeksforgeeks.org/problems/column-name-from-a-given-column-number4244/1

# Solution

class Solution:
    def colName (self, columnNumber):
        title = ""
        while columnNumber:
            # Calculate the remainder when dividing by 26 (number of letters in the English alphabet).
            remainder = (columnNumber - 1) % 26
            # Convert the remainder to the corresponding uppercase letter (A-Z).
            title = chr(65 + remainder) + title
            # Update columnNumber to the quotient when divided by 26.
            columnNumber = (columnNumber - 1) // 26
        return title

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends
