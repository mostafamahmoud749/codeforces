#include <bits/stdc++.h>
#define ll long long
using namespace std;

map<int,int>mp;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,v;
    ll res=0;
    cin>>n;
    vector<int> a (n);
    vector<int> b (n);
    vector<int> c (n);

    for (int i=0;i<n;i++) cin>>a[i];
    for (int i=0;i<n;i++) cin>>b[i];
    for (int i=0;i<n;i++) {
      cin>>v;

      mp[b[v-1]]++;
    }

    for (int i=0;i<n;i++) res+=(mp[a[i]]);

    cout<<res;

    return 0;
}