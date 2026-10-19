#include <bits/stdc++.h>
#define ll long long
using namespace std;

map<int,int>mp;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    stack<int> st;

    while (true) {
      string cm;
      int v;
      cin>>cm;
      if (cm=="push"){
        cin>>v;
        st.push(v);
        cout<<"ok"<<"\n";

      }else if (cm=="pop"){
        cout<<st.top()<<"\n";
        st.pop();
      }else if (cm=="back"){
        cout<<st.top()<<"\n";
      }else if (cm=="size"){
        cout<<st.size()<<"\n";
      }else if (cm=="clear"){
        while (!st.empty()) st.pop();
        cout<<"ok"<<"\n";
      }else if (cm=="exit"){
        cout<<"bye"<<"\n";
        return 0;
      }
    }

    return 0;
}