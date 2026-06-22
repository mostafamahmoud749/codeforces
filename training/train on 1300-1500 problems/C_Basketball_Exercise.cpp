
#include <bits/stdc++.h>
#define ll long long
using namespace std;

int n;
ll dp[100005][2];
vector<int> a;
vector<int> b;

ll solve(int indx,int s){
    if (indx==n) return 0;
    if  (dp[indx][s]!=-1) return dp[indx][s];
    ll ch1,ch2;
    if (s==0){
        ch1=b[indx]+solve(indx+1,1);
        ch2=solve(indx+1,0);
    }else{
        ch1=a[indx]+solve(indx+1,0);
        ch2=solve(indx+1,1);
    }
    return dp[indx][s]=max(ch1,ch2);
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin>>n;
    a.resize(n);
    b.resize(n);
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    for(int i=0;i<n;i++){
        cin>>b[i];
    }
    for (int i=0;i<n;i++) {
        dp[i][0]=-1;
        dp[i][1]=-1;
    }
    cout<<max(solve(0,0),solve(0,1))<<"\n";
    return 0;
}
