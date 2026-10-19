#include <bits/stdc++.h>
#define ll long long
using namespace std;

map<int,int>mp;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,q,cm,i,v;
    cin>>n>>q;

    vector<priority_queue<int>> a (n);

    while (q--) {
      cin>>cm>>i;

      if (cm==0) {
        cin>>v;
        a[i].push(v);
      }else if (cm==1) {
        if (!a[i].empty()) cout<<a[i].top()<<"\n";
      }else {
        if (!a[i].empty()) a[i].pop();
      }
    }

    

    return 0;
}