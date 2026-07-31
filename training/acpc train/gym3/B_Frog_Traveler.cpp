#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin>>n;

    vector<int> a(n+1);
    vector<int> b(n+1);

    a[0]=0;
    for (int i=1;i<n+1;i++){
        cin>>a[i];
    }
    for (int i=1;i<n+1;i++){
        cin>>b[i];
    }
    
    vector<int> parent(n+1,-1);
    vector<int> prev(n+1,-1);
    vector<int> l(n+1,-1);
    l[n]=0;


    queue<int> q;
    q.push(n);

    while (!q.empty()) {
        int v;
        v=q.front();
        q.pop();

        int jumps=a[v];

        if (l[0]!=-1) break;

        for (int i=1;i<=jumps;i++){
            int slip=b[v-i];
            if (l[v-i+slip]==-1){
                l[v-i+slip]=l[v]+1;
                q.push(v-i+slip);
                parent[v-i+slip]=v-i;
                prev[v-i+slip]=v;
            }
        }
    }
    cout<<l[0]<<"\n";
    vector<int> res;
    int cur=0;

    if (l[0]!=-1){
        while (parent[cur]!=-1){
            res.push_back(parent[cur]);
            cur=prev[cur];
        }
        for (int i=res.size()-1;i>=0;i--){
            cout<<res[i]<<" ";
        }
    }
    return 0;
}