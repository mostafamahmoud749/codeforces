#include <bits/stdc++.h>
#define ll long long
using namespace std;

vector<int> a;

int solve(int l,int r,int h){
    int ch1=r-l+1;
    int s=a[l];
    for (int i=l;i<=r;i++){
        if (a[i]<s) s=a[i];
    }
    int ch2=s-h;
    int i=l;
    for (int j=l;j<=r;j++){
        if (a[j]==s){
            if (i<=j-1) ch2+=solve(i,j-1,s);
            i=j+1;
        }
    }
    if (i<=r) ch2+=solve(i,r,s);
    return min({ch1,ch2});
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin>>n;
    for (int i=0;i<n;i++){
        int v;
        cin>>v;
        a.push_back(v);
    }
    int res=solve(0,n-1,0);
    cout<<res<<"\n";
}
