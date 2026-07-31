#include <bits/stdc++.h>
#define ll long long
using namespace std;


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,m,r,c,x,y;
    cin>>n>>m>>r>>c>>x>>y;

    vector<string> a(n);
    for (int i=0;i<n;i++){
        cin>>a[i];
    }

    vector<vector<bool>> visited(n,vector<bool>(m,false));

    deque<tuple<int,int,int,int>> q;
    q.push_front({r-1,c-1,x,y});

    vector<pair<int,int>> dir={{1,0},{-1,0},{0,1},{0,-1}};

    while (!q.empty()) {
        auto [i,j,crl,crr]=q.front();
        q.pop_front();
        if (visited[i][j]) continue;

        visited[i][j]=true;
        for (auto u:dir){
            int rl,rr,ni,nj;
            rl=crl;
            rr=crr;
            ni=i+u.first;
            nj=j+u.second;

            if (0<=ni && ni<=n-1 && 0<=nj && nj<=m-1 && a[ni][nj]!='*' && not visited[ni][nj]){
                if (ni!=i){
                    q.push_front({ni,nj,rl,rr});
                }else {
                    if (nj<j && (rl-1)>=0){
                        rl-=1;
                        q.push_back({ni,nj,rl,rr});
                    }else if (nj>j && (rr-1)>=0) {
                        rr-=1;
                        q.push_back({ni,nj,rl,rr});
                    }
                }
            }
        }
    }

    int res=0;

    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            if (visited[i][j]) res+=1;
        }
    }
    cout<<res;
    
    return 0;
}
