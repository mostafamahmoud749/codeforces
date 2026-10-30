#include <bits/stdc++.h>
#define ll long long
using namespace std;

int n;
vector<vector<vector<char>>> res;
vector<pair<int,int>> dir={{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};

void solve(vector<vector<char>>& a, int done) {
    if (done==n) {
      res.push_back(a);
      for (int i=0;i<n;i++)
        for (int j=0;j<n;j++)
          if (res.back()[i][j]=='*') res.back()[i][j]='.';
      return;
    }

  int i=done;
  for (int j=0;j<n;j++) {
    if (a[i][j]=='.') {
      vector<pair<int,int>> changed;
      a[i][j]='Q';
      int cur=n+1;

      while (cur--){
        for (auto [ii,ij]:dir) {
          int ci=i+(ii*cur);
          int cj=j+(ij*cur);

          if (0<=ci && ci<n && 0<=cj && cj<n && a[ci][cj]=='.') {
            a[ci][cj]='*';
            changed.push_back({ci,cj});
          }
        }
      }

      solve(a,done+1);

      for (auto [ci,cj]:changed)
        a[ci][cj]='.';
      a[i][j]='.';
    }
  }
  return;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin>>n;

    vector<vector<char>> a(n,vector<char>(n,'.'));
    solve(a,0);

    for (int i=0;i<res.size();i++) {
      if (i) cout<<"\n";
      for (int j=0;j<n;j++) {
        for (char c:res[i][j]) cout<<c;
        cout<<"\n";
      }
    }
    return 0;
}