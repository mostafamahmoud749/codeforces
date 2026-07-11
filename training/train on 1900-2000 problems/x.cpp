#include <bits/stdc++.h>
#define ll long long
using namespace std;

int n,m,k;
int dp[11][11][11][11];
vector<vector<ll>> a;

int solve(int indx,int a,int b,int c){
    if (indx==10) {
        if (a==0 && b==0 && c==0) return 0;
        return -1e9;
    }
    if (dp[indx][a][b][c]!=-1) return dp[indx][a][b][c];

    int res=-1e9;

    if (a>0) {
        if (b>0) {
            if (c>0) {
                res=max(res,1+solve(indx+1,a-1,b-1,c-1));
            }
            res=max(res,solve(indx+1,a-1,b-1,c));
        }
        if (c>0) {
            res=max(res,solve(indx+1,a-1,b,c-1));
        }
        res=max(res,1+solve(indx+1,a-1,b,c));
    }
    
    if (b>0) {
        if (c>0) {
            res=max(res,solve(indx+1,a,b-1,c-1));
        }
        res=max(res,1+solve(indx+1,a,b-1,c));
    }
    if (c>0) {
        res=max(res,1+solve(indx+1,a,b,c-1));
    }
    res=max(res,solve(indx+1,a,b,c));
    
    return dp[indx][a][b][c] = res;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin>>t;
    while (t--){
        string a,b,c;
        cin>>a>>b>>c;

        int ac=0,bc=0,cc=0;
        for (char ch:a) if (ch=='1') ac++;
        for (char ch:b) if (ch=='1') bc++;
        for (char ch:c) if (ch=='1') cc++;

        for (int i=0;i<11;i++){
            for (int j=0;j<11;j++){
                for (int k=0;k<11;k++){
                    for (int l=0;l<11;l++){
                        dp[i][j][k][l] = -1;
                    }
                }
            }
        }
        int res=solve(0,ac,bc,cc);

        string ans="";
        for (int i=0;i<res;i++) ans+="1";
        for (int i=0;i<(10-res);i++) ans+="0";
        cout<<ans<<"\n";
    }
    return 0;
}