#include <bits/stdc++.h>
#define ll long long
using namespace std;



int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,n1,n2,res=0,tries=1000;

    cin>>n>>n1;
    deque<int> a(n1);

    for (int i=0;i<n1;i++) cin>>a[i];

    cin>>n2;

    deque<int> b(n2);
    for (int i=0;i<n2;i++) cin>>b[i];

    while (!a.empty() && !b.empty() && tries--){
      res+=1;
      if (a.front()>b.front()){
        a.push_back(b.front());
        a.push_back(a.front());
        a.pop_front();
        b.pop_front();
      } else {
        b.push_back(a.front());
        b.push_back(b.front());
        b.pop_front();
        a.pop_front();
      }
    }

    if (a.empty()) {
      cout<<res<<" "<<2;
    }else if (b.empty()) {
      cout<<res<<" "<<1;
    }else {
      cout<<-1;
    }

    return 0;
}