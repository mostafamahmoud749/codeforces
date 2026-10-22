#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll res=0;
    int n,q,l,r;
    cin>>n>>q;

    vector<int> b(n,0);
    vector<int> a(n+1,0);
    vector<ll> p(n+1,0);

    for (int i=0;i<n;i++){
      cin>>b[i];
    }

    for (int i=0;i<q;i++){
      cin>>l>>r;
      a[l-1]+=1;
      a[r]-=1;
    }

    for (int i=1;i<n+1;i++){
      p[i]=p[i-1]+a[i-1];
    }

    sort(p.rbegin(),p.rend());
    sort(b.rbegin(),b.rend());

    for (int i=0;i<n;i++){
      res+=(p[i]*b[i]);
    }

    cout<<res;
    return 0;
}