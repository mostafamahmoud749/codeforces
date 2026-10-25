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
      bool s=false;
      int n;
      cin>>n;

      vector<int> a(n,0);
      for (int i=0;i<n;i++) {
        cin>>a[i];
      }

      sort(a.begin(),a.end());

      for (int i=0;i<n-2;i++){
        if (a[i]==a[i+1] && a[i+1]==a[i+2]) {
          cout<<a[i]<<"\n";
          s=true;
          break;
        }
      }

      if (!s) cout<<-1<<"\n";

    }
    
    return 0;
}