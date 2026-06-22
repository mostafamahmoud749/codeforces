#include <bits/stdc++.h>
#define ll long long
using namespace std;

int n;
ll dp[200005][4];
vector<int> a;

ll solve(int indx,int d){
    if (indx>=n) return 0;
    if (dp[indx][d]!=-1) return dp[indx][d];
    ll ch1=-1e18,ch2=-1e18,ch3=-1e18;
    // even elements didnt flip yet
    if (d==0){
        ch1=a[indx]+solve(indx+2,0);
        // start flipping
        if (indx+1<n) {
            ch2=a[indx]+solve(indx+1,1);// start flip on odd
            ch3=solve(indx,3);// start flip on even
        }
    }else if (d==1){
        // odd elements fliped
        if (indx+1<n) ch1=a[indx]+solve(indx+2,1);//conintue
        ch2=solve(indx+1,2);//end
    }else if(d==2){
        // returned to even element done with the flip
        ch1=a[indx]+solve(indx+2,2);
    }else if(d==3) {
        if (indx+1<n) {
            ch1=a[indx+1]+solve(indx+2,3);// Continue flip
            ch2=a[indx+1]+solve(indx+2,2);// End flip
        }
    }
    return dp[indx][d]=max({ch1,ch2,ch3});
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin>>t;
    while (t--){
        cin>>n;
        a.resize(n);
        for(int i=0;i<n;i++){
            cin>>a[i];
        }
        for (int i=0;i<n;i++) {
            dp[i][0]=-1;
            dp[i][1]=-1;
            dp[i][2]=-1;
            dp[i][3]=-1;
        }
        cout<<solve(0,0)<<"\n";
    }
    return 0;
}