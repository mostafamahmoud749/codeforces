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
      int n;
      cin>>n;

      string a;
      cin>>a;
      bool s=true;

      for (int i=0;i<n;i++) {
        if (a[i]=='W') continue;
        bool r=false,b=false;
        while (i<n) {

          if (a[i]=='R') r=true;
          if (a[i]=='B') b=true;

          if ((a[i]=='W'||i==n-1) && !(r && b)) {
            s=false; 
            break;
          }

          if (a[i]=='W') {
            break;
          }
          i+=1;
        }
        if (!s) break;
      }

      s? cout<<"YES"<<"\n" : cout<<"NO"<<"\n";

    }
    
    return 0;
}