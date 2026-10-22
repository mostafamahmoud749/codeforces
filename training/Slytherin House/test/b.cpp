#include <bits/stdc++.h>
#define ll long long
using namespace std;

map<string,int> mp;
map<int,vector<string>,greater<int>> ppl;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string name;
    int n,s,cur,mx=-1e9;
    cin>>n;

    for (int i=0;i<n;i++){
      cin>>name>>s;
      mp[name]+=s;
      
      ppl[mp[name]].push_back(name);
      
    }
    
    for (auto& [name,score]:mp){
      mx=max({mx,score});
    }
    cout<<ppl[mx][0];
    

    return 0;
}