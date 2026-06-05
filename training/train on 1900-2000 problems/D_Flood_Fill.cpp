#include <bits/stdc++.h>
#define ll long long
using namespace std;

vector<int> a;
int dp[5005][5005];

int solve(int l, int r){
    if (l>=r){
        return 0;
    }
    if (dp[l][r]!=-1){
        return dp[l][r];
    }
    int ch1=1+solve(l+1,r);
    int ch2=1+solve(l,r-1);
    int ch3=1e9;
    if (a[l]==a[r]){
        ch3=1+solve(l+1,r-1);
    }
    int res=min({ch1,ch2,ch3});
    dp[l][r]=res;
    return res;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    memset(dp,-1,sizeof(dp));
    int n;
    cin>>n;
    int prev=-1;
    for (int i=0;i<n;i++){
        int v;
        cin>>v;
        if (v!=prev){
            a.push_back(v);
            prev=v;
        }
    }
    int res;
    res=solve(0,a.size()-1);
    cout<<res;
}
