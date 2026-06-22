#include <bits/stdc++.h>
#define ll long long
using namespace std;

vector<vector<int>> a;
int n,m;
int t;
map<pair<int,int>,int> dp;

int solve(int indx,int curs){
    if (curs==t) return 0;
    if (indx==n){
        if (curs==t) return 0;
        return 1e9;
    }
    if (dp.count({indx,curs})) return dp[{indx,curs}];
    int ch1=1e9,ch2=1e9;
    ch1=solve(indx+1,curs);
    int newcurs=curs;
    for (int i=0;i<a[indx].size();i++){
        newcurs|=(1<<(a[indx][i]-1));
    }
    ch2=1+solve(indx+1,newcurs);
    return dp[{indx,curs}]=min(ch1,ch2);
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin>>n>>m;
    a.resize(n);
    for (int i=0;i<n;i++){
        int r;
        cin>>r;
        a[i].resize(r);
        for (int j=0;j<r;j++){
            cin>>a[i][j];
        }
    }
    t=(1<<m)-1;
    int v=solve(0,0);
    if (v!=1e9){
        cout<<v<<"\n";
    }else{
        cout<<-1<<"\n";
    }
}


// #include <bits/stdc++.h>
// #define ll long long
// using namespace std;

// vector<vector<int>> a;
// int n,m;
// map<pair<int,set<int>>,int> dp;

// int solve(int indx,set<int> s){
//     if (s.size()==m) return 0;
//     if (indx==n){
//         if (s.size()==m) return 0;
//         return 1e9;
//     }
//     if (dp.count({indx,s})) return dp[{indx,s}];
//     int ch1=1e9,ch2=1e9;
//     ch1=solve(indx+1,s);
//     set<int> news=s;
//     news.insert(a[indx].begin(),a[indx].end());
//     ch2=1+solve(indx+1,news);
//     return dp[{indx,s}]=min(ch1,ch2);
// }

// int main()
// {
//     ios::sync_with_stdio(0);
//     cin.tie(0);
//     cin>>n>>m;
//     a.resize(n);
//     for (int i=0;i<n;i++){
//         int r;
//         cin>>r;
//         a[i].resize(r);
//         for (int j=0;j<r;j++){
//             cin>>a[i][j];
//         }
//     }
//     set<int>s;
//     int v=solve(0,s);
//     if (v!=1e9){
//         cout<<v<<"\n";
//     }else{
//         cout<<-1<<"\n";
//     }
// }
