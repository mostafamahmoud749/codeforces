#include <bits/stdc++.h>
#define ll long long
using namespace std;

int n;
vector<int> a;
vector<int> dp;
vector<vector<int>> p;


bool solve(int indx){
    if (dp[indx]!=-1){
        return dp[indx];
    }
    if (indx>n) return false;
    if (indx==n) return true;
    bool ch1=false,ch2=false;
    if (indx+a[indx]<n) ch1=solve(indx+a[indx]+1);
    int r=0;
    for (int i=0;i<p[indx].size();i++){
        ch2=solve(p[indx][i]);
        if (ch2) break;
    }

    return dp[indx]=(ch1||ch2);
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin>>t;
    while (t--){
        a.clear();
        cin>>n;
        for (int i=0;i<n;i++){
            int v;
            cin>>v;
            a.push_back(v);
        }
        dp.assign(n+1,-1);
        p.assign(n+1,vector<int>());
        for (int i=0;i<n;i++){
            if (i-a[i]>=0 && i-a[i]<=n){
                p[i-a[i]].push_back(i+1);
            }
        }
        bool res=solve(0);
        if (res){
            cout<<"YES"<<"\n";
        }else{
            cout<<"NO"<<"\n";
        }
    }
}






// #include <bits/stdc++.h>
// #define ll long long
// using namespace std;

// int n;
// vector<int> a;
// vector<vector<int>> dp;

// bool solve(int indx,int r){
//     if (dp[indx][r]!=-1){
//         return dp[indx][r];
//     }
//     if (r>=n || indx>n) return false;
//     if (indx==n && r==0) return true;
//     bool ch1=false,ch2=false,ch3=false;
//     if (r==0 && indx+a[indx]<n) ch1=solve(indx+a[indx]+1,0);
//     ch2=solve(indx,r+1);
//     if (r>=indx && a[r]==r-indx) ch3=solve(r+1,0);

//     return dp[indx][r]=(ch1||ch2||ch3);
// }

// int main(){
//     ios::sync_with_stdio(0);
//     cin.tie(0);
//     int t;
//     cin>>t;
//     while (t--){
//         a.clear();
//         cin>>n;
//         for (int i=0;i<n;i++){
//             int v;
//             cin>>v;
//             a.push_back(v);
//         }
//         dp.assign(n+1,vector<int>(n+1,-1));
//         bool res=solve(0,0);
//         if (res){
//             cout<<"YES"<<"\n";
//         }else{
//             cout<<"NO"<<"\n";
//         }
//     }
// }
