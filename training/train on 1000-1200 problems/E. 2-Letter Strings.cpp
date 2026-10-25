#include <bits/stdc++.h>
#define ll long long
using namespace std;

map<pair<char,char>,int> mp;

main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t;
    cin>>t;
    vector<char> chr={'a','b','c','d','e','f','g','h','i','j','k'};

    while (t--)
    {
      mp.clear();
      ll res=0;
      int n;
      cin>>n;

      

      for (int i=0;i<n;i++) {
        string a;
        cin>>a;
        for (auto i:chr) {
          res+=mp[{a[0],i}];
        }
        for (auto i:chr) {
          res+=mp[{i,a
            [1]}];
        }
        res-=2*mp[{a[0],a[1]}];
        mp[{a[0],a[1]}]+=1;
      }

      cout<<res<<"\n";
      
    }
    
    return 0;
}