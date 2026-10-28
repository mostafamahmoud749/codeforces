#include <bits/stdc++.h>
#define ll long long
using namespace std;



int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll p,turns=0,s=0,ts=0;
    int n,l=0,res=1e9,indx=0;
    cin>>n>>p;

    vector<ll> a(n);
    for (int i=0;i<n;i++) {
      cin>>a[i];
      ts+=a[i];
    }

    turns=(p-1)/ts;
    p-=turns*ts;
    turns*=n;

    for (int r=0;r<n*2;r++) {
      s+=a[r%n];
      while (s-a[l%n]>=p) {
        s-=a[l%n];
        l++;
      }
      if (s>=p && r-l+1<res) {
        indx=l;
        res=r-l+1;
      }
    }

    cout<<(indx%n)+1<<" "<<turns+res;



    return 0;
}