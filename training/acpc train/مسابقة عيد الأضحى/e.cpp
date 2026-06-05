#include <bits/stdc++.h>
#define ll long long
using namespace std;

int n;
ll s;
vector<int> a;
map<pair<int,ll>,int> dp;

int solve(int indx, ll cs){
    if (indx==n){
        if (cs==s-1){
            return 1;
        }
        return 0;
    }
    if (dp.count({indx,cs})){
        return dp[{indx,cs}];
    }
    int ch1=solve(indx+1,cs+a[indx]);
    int ch2=solve(indx+1,cs);
    int res=ch1+ch2;
    dp[{indx,cs}]=res;
    return res;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin>>t;
    while (t--){
        cin>>n;
        for (int i=0;i<n;i++){
            int v;
            cin>>v;
            s=s+v;
        }
        int res=solve(0,0);
        cout<<res;
    }
}
