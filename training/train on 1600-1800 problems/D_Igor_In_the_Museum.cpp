#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,m,x;
    cin>>n>>m>>x;

    vector<vector<char>> a(n, vector<char>(m));
    for (int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cin>>a[i][j];
        }
    }

    vector<vector<bool>> visited(n, vector<bool>(m, false));
    vector<vector<int>> res(n, vector<int>(m, -1));

    for (int y=0;y<x;y++){
        int i,j;
        cin>>i>>j;
        
        i--;
        j--;

        if (res[i][j]!=-1) {
            cout<<res[i][j]<<"\n";
            continue;
        }

        queue<pair<int,int>> q;
        q.push({i,j});
        visited[i][j]=true;
        int cres=0;
        vector<pair<int,int>> path={{i,j}};

        while (!q.empty()) {
            pair<int,int> curr = q.front();
            q.pop();
            i = curr.first;
            j = curr.second;

            if (i<n-1 and a[i+1][j]=='*') {
                cres+=1;
            }
            if (i>0 and a[i-1][j]=='*') {
                cres+=1;
            }
            if (j<m-1 and a[i][j+1]=='*') {
                cres+=1;
            }
            if (j>0 and a[i][j-1]=='*') {
                cres+=1;
            }


            if (i<n-1 and a[i+1][j]=='.' and not visited[i+1][j]) {
                q.push({i+1,j});
                visited[i+1][j]=true;
                path.push_back({i+1,j});
            }
            if (i>0 and a[i-1][j]=='.' and not visited[i-1][j]) {
                q.push({i-1,j});
                visited[i-1][j]=true;
                path.push_back({i-1,j});
            }
            if (j<m-1 and a[i][j+1]=='.' and not visited[i][j+1]) {
                q.push({i,j+1});
                visited[i][j+1]=true;
                path.push_back({i,j+1});
            }
            if (j>0 and a[i][j-1]=='.' and not visited[i][j-1]) {
                q.push({i,j-1});
                visited[i][j-1]=true;
                path.push_back({i,j-1});
            }
        }
        
        for (auto p:path) {
            res[p.first][p.second]=cres;
        }
        cout<<cres<<"\n";
    }
    return 0;
}