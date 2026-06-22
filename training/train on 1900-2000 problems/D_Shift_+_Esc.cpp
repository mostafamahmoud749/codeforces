#include <bits/stdc++.h>
#define ll long long
using namespace std;

int n,m,k;
ll dp[201][201][205];
vector<vector<ll>> a;

ll solve(int i,int j,int sh){
    if (i>n || j>m) return 1e18;
    if (i==n || j==m) {
        if (i==n-1 && j==m) return 0;
        if (i==n && j==m-1) return 0;
        return 1e18;
    }
    if (dp[i][j][sh]!=-1) return dp[i][j][sh];
    ll ch1=1e18,ch2=1e18,ch3=1e18;
    if (sh!=202){
        int curj=((j+sh)%m);
        ch1=a[i][curj]+solve(i+1,j,202);
        ch2=a[i][curj]+solve(i,j+1,sh);
    }
    
    if (sh==202) {
        for (int x=0;x<m;x++){
            int curj=((j+x)%m);
            ch1=x*k+a[i][curj]+solve(i+1,j,202);
            ch2=x*k+a[i][curj]+solve(i,j+1,x);
            ch3=min({ch3,ch1,ch2});
        }
    }
    return dp[i][j][sh]=min({ch1,ch2,ch3});
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin>>t;
    while (t--){
        cin>>n>>m>>k;
        a.resize(n);
        memset(dp,-1,sizeof(dp));
        for(int i=0;i<n;i++){
            a[i].resize(m);
            for(int j=0;j<m;j++){
                cin>>a[i][j];
            }
        }
        cout<<solve(0,0,202)<<"\n";
    }
    return 0;
}
