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

      vector<int> a(n,0);
      for (int i=0;i<n;i++) {
        cin>>a[i];
      }
      bool s=true;

      for (int i=0;i<n;i+=2) {
        if (a[i]%2!=a[0]%2) {
          s=false;
          break;
        }
      }

      for (int i=1;i<n;i+=2) {
        if (!s || a[i]%2!=a[1]%2) {
          s=false;
          break;
        }
      }

      s?cout<<"YES"<<"\n" : cout<<"NO"<<"\n";

    }
    
    return 0;
}