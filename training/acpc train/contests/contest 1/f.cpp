#include <bits/stdc++.h>
#define ll long long
using namespace std;

set<ll> st;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t;
    cin>>t;
    while (t--) {
      int n;
      cin>>n;

      vector<int> a(n,0);

      for (int i=0;i<n;i++) {
        cin>>a[i];
      };
      sort(a.begin(),a.end());

      if (a[0]+a[1]<=a[a.size()-1]) {
        cout<<1<<" "<<2<<" "<<a.size()<<"\n";
      } else {
        cout<<-1<<"\n";
      }
      

    }
    
    return 0;
}