#include <bits/stdc++.h>
#define ll long long
using namespace std;

vector<int> a;
map<vector<int>,int> dp;

int solve(vector<int> a){
    if (dp.count(a)){
        return dp[a];
    }
    int s=0;
    for (int i=0;i<a.size()-1;i++){
        if (a[i]==a[i+1]){
            s=1; 
            break;
        }
    }
    if (s==0) return dp[a]=a.size();
    int res=1e9;
    for (int i=0;i<a.size()-1;i++){
        if(a[i]==a[i+1]){
            int e=a[i+1];
            a[i]++;
            a.erase(a.begin()+i+1);
            res=min({solve(a),res});
            a[i]--;
            a.insert(a.begin()+i+1,e);
        }
        
    }
    return dp[a]=res;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin>>n;
    for (int i=0;i<n;i++){
        int v;
        cin>>v;
        a.push_back(v);
    }
    int res=solve(a);
    cout<<res<<"\n";
}
