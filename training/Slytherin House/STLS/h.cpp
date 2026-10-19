#include <bits/stdc++.h>
#define ll long long
using namespace std;

map<int,int>mp;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,v;
    cin>>n;

    stack<pair<int,int>> st;

    for (int i=0;i<n;i++){
      cin>>v;
      while (!st.empty() && st.top().first>=v) st.pop();

      if (!st.empty()) {
        cout<<st.top().second<<' ';
      }else {
        cout<<0<<' ';
      }

      st.push({v,i+1});
    }



    return 0;
}