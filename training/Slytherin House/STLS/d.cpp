#include <bits/stdc++.h>
#define ll long long
using namespace std;

map<string,int> mp={
  {"Bessie", 0},
  {"Elsie", 0},
  {"Daisy", 0},
  {"Gertie", 0},
  {"Annabelle", 0},
  {"Maggie", 0},
  {"Henrietta", 0}
};

int main(){
    freopen("notlast.in", "r", stdin);
    freopen("notlast.out", "w", stdout);

    ios::sync_with_stdio(0);
    cin.tie(0);
    string c;
    int n,v,mn;
    cin>>n;

    vector<pair<int,string>> a;

    for (int i=0;i<n;i++){
      cin>>c>>v;
      mp[c]+=v;
    }

    for (auto [key,value]:mp) {
      a.push_back({value,key});
    }

    sort(a.begin(),a.end());
    
    mn=a[0].first;

    for (int i=1;i<a.size();i++){
      if (a[i].first==mn) {
        continue;
      } else if (i+1<a.size() && a[i].first==a[i+1].first){
        cout<<"Tie";
        return 0;
      } else {
        cout<<a[i].second;
        return 0;
      }
    }
    cout<<"Tie";

    return 0;
}