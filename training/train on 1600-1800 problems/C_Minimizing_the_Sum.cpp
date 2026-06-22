#include <bits/stdc++.h>
#define ll long long
using namespace std;

int n,k;
ll dp[300005][11];
vector<int> a;

ll solve(int indx,int curk){
    if (indx==n) return 0;
    if (dp[indx][curk]!=-1) return dp[indx][curk];
    ll res=0;
    int curmin=a[indx];
    ll cursum=0;
    for (int i=indx;i<min(n,indx+curk+1);i++) {
        curmin=min(curmin,a[i]);
        cursum+=a[i];
        res=max(res,cursum-((ll)(i-indx+1)*curmin)+solve(i+1,curk-(i-indx)));
    }
    return dp[indx][curk]=res;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin>>t;
    while (t--){
        cin>>n>>k;
        a.resize(n);
        for (int i=0;i<=n;i++){
            for (int j=0;j<=k;j++){
                dp[i][j]=-1;
            }
        }
        for(int i=0;i<n;i++){
            cin>>a[i];
            }
            cout<<accumulate(a.begin(),a.end(),0LL)-solve(0,k)<<"\n";
    }
    return 0;
}
