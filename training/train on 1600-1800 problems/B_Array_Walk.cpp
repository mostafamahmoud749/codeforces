#include <bits/stdc++.h>
#define ll long long
using namespace std;

int n,k,z;
ll dp[100005][6][2];
vector<int> a;

ll solve(int r,int l,int s){
    if(r+l==k) return 0;
    if (dp[r][l][s]!=-1) return dp[r][l][s];
    ll ch1=-1e9,ch2=-1e9;
    if (r-l+1<n) ch1=a[r-l+1]+solve(r+1,l,0);
    if (r-l-1>=0 && s!=1 && l<z) ch2=a[r-l-1]+solve(r,l+1,1);
    ll res=max(ch1,ch2);
    return dp[r][l][s]=res;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin>>t;
    while (t--){
        cin>>n>>k>>z;
        a.resize(n);
        for(int i=0;i<n;i++){
            cin>>a[i];
        }
        for (int i=0;i<=k;i++) {
            for (int j=0;j<=z;j++) {
                dp[i][j][0]=-1;
                dp[i][j][1]=-1;
            }
        }
        cout<<a[0]+solve(0,0,0)<<"\n";
    }
    return 0;
}
