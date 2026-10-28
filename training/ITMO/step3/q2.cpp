#include <bits/stdc++.h>
#define ll long long
using namespace std;


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll cur=0,s,res=0;
    int n,l=0;
    cin>>n>>s;

    vector<int> a(n);
    for (int i=0;i<n;i++) cin>>a[i];

    for (int r=0;r<n;r++) {
      cur+=a[r];
      while (cur>s) {
        cur-=a[l];
        l++;
      }
      ll x=r-l+1;
      res+=(x*(x+1))/2;
    }

    cout<<res;
    
    return 0;
}