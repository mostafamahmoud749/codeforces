#include <bits/stdc++.h>
#define ll long long
using namespace std;



int main(){
ios::sync_with_stdio(0);
    cin.tie(0);

    int n,k,l=0,res=1e9;
    cin>>n;

    vector<ll> a(n);
    for (int i=0;i<n;i++) cin>>a[i];

    stack<pair<ll,ll>> A;
    stack<pair<ll,ll>> B;
    ll g=0;
    for (int r=0;r<n;r++){
      g=gcd(a[r],A.empty()?0:A.top().second);
      A.push({a[r],g});
      g=gcd(g,B.empty()?0:B.top().second);

      while (g==1) {
        res=min(res,r-l+1);
        if (B.empty()){
          while (!A.empty()) {
            pair<ll,ll> x;
            x=A.top();
            A.pop();
            x.second=gcd(x.first,B.empty()?0:B.top().second);
            B.push(x);
          }
        }
        B.pop();
        l++;

        ll ga=A.empty()?0 : A.top().second;
        ll gb=B.empty()?0 : B.top().second;

        g=gcd(ga,gb);
      }
    }

    res!=1e9?cout<<res:cout<<-1;
    return 0;
}