#include <bits/stdc++.h>
#define ll long long
using namespace std;

int n;
vector<int> a;
map<pair<int,int>,int> dp;

int solve(int prev1,int prev2){
    if (dp.count({prev1,prev2})){
        return dp[{prev1,prev2}];
    }
    int indx=max({prev1,prev2})+1;
    if (indx==n){
        return 0;
    }
    int ch1=0,ch2=0;
    if ((prev1==-1 || a[prev1]!=a[indx]) && (prev2!=-1 && a[prev2]==a[indx])){
        ch1=1+solve(indx,prev2);
    }else if ((prev2==-1 || a[prev2]!=a[indx]) && (prev1!=-1 && a[prev1]==a[indx])){
        ch2+=1+solve(prev1,indx);
    }else if (prev1!=-1 && prev2!=-1 && a[prev1]==a[indx] && a[prev2]==a[indx]){
        ch1=solve(indx,prev2);
    }else {
        ch1=1+solve(indx,prev2);
        ch2+=1+solve(prev1,indx);
    }
    int res=max({ch1,ch2});
    dp[{prev1,prev2}]=res;
    return res;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin>>n;
    for (int i=0;i<n;i++){
        int v;
        cin>>v;
        if (i>1 && v==a[i-1] && v==a[i-2]){
            continue;
        }
        a.push_back(v);
    }
    int res;
    n=a.size();
    res=solve(-1,-1);
    cout<<res;
}