#include <bits/stdc++.h> 
using namespace std; 

class Solution
{   
    public:
    //traversal of the matrix in a clockwise manner.
    vector<int> boundaryTraversal(vector<vector<int> > matrix, int n, int m) 
    {
         vector<int> v;
        map<pair<int,int>,bool> vis;
        int i,j;
        i=0,j=0;
        for(j=0;j<m;j++)
        {
            if(vis[{i,j}]==false)
            {v.push_back(matrix[i][j]);
            vis[{i,j}]=true;}
            
        }
        j=m-1;
        i=1;
        for(i=1;i<n;i++)
        {
            if(vis[{i,j}]==false)
            {v.push_back(matrix[i][j]);
            vis[{i,j}]=true;}
        }
        
        i=n-1;
        for(j=m-2;j>=0;j--)
        {
            if(vis[{i,j}]==false)
            {v.push_back(matrix[i][j]);
            vis[{i,j}]=true;}
        }
        
        j=0;
        for(i=n-2;i>0;i--)
        {
            if(vis[{i,j}]==false)
            {v.push_back(matrix[i][j]);
            vis[{i,j}]=true;}
        }
        return(v);
    
    }
};

int main() {
    int t;
    cin>>t;
    
    while(t--) 
    {
        int n,m;
        cin>>n>>m;
        vector<vector<int> > matrix(n); 

        for(int i=0; i<n; i++)
        {
            matrix[i].assign(m, 0);
            for( int j=0; j<m; j++)
            {
                cin>>matrix[i][j];
            }
        }

        Solution ob;
        vector<int> result = ob.boundaryTraversal(matrix, n, m);
        for (int i = 0; i < result.size(); ++i)
        cout<<result[i]<<" ";
        cout<<endl;
    }
    return 0;
}
