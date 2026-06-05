#include <bits/stdc++.h>
#define ll long long
using namespace std;

ll dp[10][200005];

ll solve(int num,int cm){
    if (dp[num][cm]!=-1){
        return dp[num][cm];
    }
    if (cm+num<10){
        return dp[num][cm]=1;
    }else{
        ll res=(solve(1,cm-(10-num))+solve(0,cm-(10-num)))%1000000007;
        return dp[num][cm]=res;
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    memset(dp,-1,sizeof(dp));
    int t;
    cin>>t;
    while (t--){
        string n;
        int m;
        cin>>n>>m;
        ll res=0;
        for (int i=0;i<n.size();i++){
            res=(res+solve(n[i]-'0',m))%1000000007;
        }
        cout<<res<<"\n";
    }
}
