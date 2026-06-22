#include <bits/stdc++.h>
#define ll long long
using namespace std;

int n;
bool dp[2005][2005][1005];
vector<int> a;

bool solve(int la,int lb,int ac){
    int curindx=max(la,lb)+1;
    if (ac>n/2 || (curindx-1)-ac>2) return false;
    if (curindx==n) {
        if (ac==n/2) return true;
        return false;
    }
    if (dp[la][lb][ac]!=-1) return dp[la][lb][ac];
    bool ch1=false,ch2=false;
    if (lb!=-1 && a[curindx]<a[la] && a[curindx]<a[lb]) return false;
    if (lb!=-1 && a[curindx]>a[la] && a[curindx]>a[lb]) {
        ch1=solve(curindx,lb,ac+1);
        ch2=solve(la,curindx,ac);
    }
    if (a[curindx]>a[la] && lb==-1){
        ch1=solve(curindx,lb,ac+1);
        ch2=solve(la,curindx,ac);
    }
    if (a[curindx]>a[la]) {
        ch2=solve(la,curindx,ac);
    }
    if (a[curindx]>a[lb]) {
        ch1=solve(curindx,lb,ac+1);
    }
    return dp[la][lb][ac]=ch1|ch2;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin>>t;
    while (t--){
        cin>>n;
        memset(dp,-1,sizeof(dp));
        a.resize(n);
        for(int i=0;i<n;i++){
            cin>>a[i];
        }
        cout<<solve(0,-1,0)<<"\n";
    }
    return 0;
}
