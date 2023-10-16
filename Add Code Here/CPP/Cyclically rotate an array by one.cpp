class Solution {
public:
  vector<vector<int>> rotateGrid(vector<vector<int>>& grid, int k) {
    int y = grid.size(), x = grid[0].size();
    int yend = y - 1, xend = x - 1;
    int limit = min(y>>1, x>>1), n = (yend<<1) + (xend<<1);
    vector<int> rot(n+n);
       
    for(int i = 0; i != limit; i++, n -= 8, xend--, yend--){
      int tk = k % n;
      if(tk){
        int k1 = 0, k2 = n;
        for(int r =    i; r < yend;  r++) rot[k1++] = rot[k2++] = grid[r][i];
        for(int c =    i; c < xend;  c++) rot[k1++] = rot[k2++] = grid[yend][c];
        for(int r = yend; r >    i;  r--) rot[k1++] = rot[k2++] = grid[r][xend];
        for(int c = xend; c >    i;  c--) rot[k1++] = rot[k2++] = grid[i][c];
        tk = n - tk;
        for(int r =    i; r < yend;  r++) grid[r][i]    = rot[tk++];
        for(int c =    i; c < xend;  c++) grid[yend][c] = rot[tk++];
        for(int r = yend; r >    i;  r--) grid[r][xend] = rot[tk++];
        for(int c = xend; c >    i;  c--) grid[i][c]    = rot[tk++];
      }
    }
    
    return grid;
  }
};
