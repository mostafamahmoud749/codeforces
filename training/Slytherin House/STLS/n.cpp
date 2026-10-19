#include <bits/stdc++.h>
#define ll long long
using namespace std;

map<int,int>mp;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,t,v;

    cin>>n;
    queue<int> q;

    while (n--) {
      cin>>t;

      if (t==1) {
        cin>>v;
        q.push(v);
      }else if (t==2 && !q.empty()) {
        q.pop();
      }else if (t==3) {
        if (q.empty()){
          cout<<"Empty!"<<"\n";
        }else {
          cout<<q.front()<<"\n";
        }
      }
    }

    return 0;
}