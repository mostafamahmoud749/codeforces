#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> a;
    int n;
    cin>>n;

    for (int i=0;i<n;i++) {
        int v;
        cin>>v;
        a.push_back(v);
    }

    sort(a.begin(),a.end());
    a.erase(unique(a.begin(),a.end()),a.end());

    cout<<a.size();

    return 0;
}