#include <bits/stdc++.h>
#define ll long long
using namespace std;

map<int,int>mp;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int d,q,cm,v;
    cin>>q;

    deque<int> dq;

    while (q--) {
      cin>>cm>>d;

      if (cm==0) {
        cin>>v;
        if (d==0) {
          dq.push_front(v);
        }else {
          dq.push_back(v);
        }
      }else if (cm==1) {
        cout<<dq[d]<<"\n";
      }else {
        if (d==0) {
          dq.pop_front();
        }else {
          dq.pop_back();
        }
      }
    }

    

    return 0;
}