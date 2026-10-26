#include <bits/stdc++.h>
#define ll long long
using namespace std;


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n,m;
    cin>>n>>m;

    vector<int> a(n,0);
    vector<int> b(m,0);

    for (int i=0;i<n;i++) {
      cin>>a[i];
    }
    
    for (int i=0;i<m;i++) {
      cin>>b[i];
    }

    int i=0,j=0;
    while (i<a.size() || j<b.size()) {
      if (j==b.size() || (i<a.size() && a[i]<b[j])) {
        i++;
      } else {
        cout<<i<<" ";
        j++;
      }
    }
    
    return 0;
}