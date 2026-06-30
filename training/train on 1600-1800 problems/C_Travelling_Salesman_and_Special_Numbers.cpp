#include <bits/stdc++.h>
#define ll long long
using namespace std;

int c[1001][1001];
int mod=1e9+7;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string n;
    int k;
    cin>>n;
    cin>>k;
    int l=n.length();
    if (k==0) {
        cout<<1;
    }else if (k==1){
        cout<<l-1;
    }else{

        for (int i=0; i<=1000; i++) {
            c[i][0]=1;
            for (int j=1; j<=i; j++) {
                c[i][j]=(c[i-1][j-1] + c[i-1][j])% mod;
            }
        }

        vector<ll>a (l+1,0);
        for (int i=1;i<l+1;i++) {
        ll res=0;
        int ones=0;
        for (int j=0;j<l;j++) {
            if (n[j]=='1') {
                int need=i-ones;
                if (need>=0 && need<=l-1-j) {
                    res=(res+c[l-1-j][need]);
                }
                ones++;
            }
        }
        if (ones==i) res=(res+1);
        a[i-1]=res;
        }
        vector<int> dp(l+1,0);
        ll res=0;
        for (int i=2;i<l+1;i++){
            dp[i]=1+dp[__builtin_popcount(i)];
            if (dp[i]+1==k){
                res=(ll)(res+a[i-1])%mod;
            }
        }
        cout<<res;
    }
    return 0;
}