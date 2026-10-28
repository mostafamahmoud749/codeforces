#include <bits/stdc++.h>
#define ll long long
using namespace std;



int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> freq(1e5,0);

    ll res=0;
    int n,k,l=0,cur=0;
    cin>>n>>k;

    vector<int> a(n);
    for (int i=0;i<n;i++) cin>>a[i];

    for (int r=0;r<n;r++) {
      freq[a[r]]+=1;
      if (freq[a[r]]==1) cur+=1;

      while (cur>k) {
        freq[a[l]]-=1;
        if (freq[a[l]]==0) cur-=1;
        l++;
      }
      res+=r-l+1;
    }

    cout<<res;
    
    return 0;
}