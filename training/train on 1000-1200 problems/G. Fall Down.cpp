#include <bits/stdc++.h>
#define ll long long
using namespace std;

main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t;
    cin>>t;
    while (t--)
    {
      int n,m;
      cin>>n>>m;

      vector<vector<char>> a (n,vector<char> (m));

      for (int i=0;i<n;i++) {
        for (int j=0;j<m;j++) {
          cin>>a[i][j];
        }
      }

      for (int j=0;j<m;j++) {
        int curs=0;
        for (int i=0;i<n;i++) {
          if (a[i][j]=='*') {
            curs+=1;
            a[i][j]='.';
          }

          if (a[i][j]=='o') {
            int ci=i-1;
            while (curs>0) {
              a[ci][j]='*';
              curs-=1;
              ci-=1;
            }
          }
        }
        int ci=n-1;
        while (curs>0) {
          a[ci][j]='*';
          curs-=1;
          ci-=1;
        }
      }

      for (int i=0;i<n;i++) {
        for (int j=0;j<m;j++) {
          cout<<a[i][j];
        }
        cout<<"\n";
      }
      
    }
    
    return 0;
}