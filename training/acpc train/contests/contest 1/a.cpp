#include <bits/stdc++.h>
#define ll long long
using namespace std;


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    deque<char> q;
    string n;
    cin>>n;
    int c=0;
    for (int i=n.size()-1;i>=0;i--){
      if (c==3) {
        q.push_back(',');
        c=0;
      }
      c+=1;
      q.push_back(n[i]);
    }
    reverse(q.begin(),q.end());
    for (int i=0;i<q.size();i++) cout<<q[i];
    return 0;
}