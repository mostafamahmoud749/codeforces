#include <bits/stdc++.h>
#define ll long long
using namespace std;

bool s=false;

void solve(string& cur,int n0,int n1,int n2){
  if (n0==0 && n1==0 && n2==0) {
    s=true;
    return;
  }

  if (cur.empty()){
    cur.push_back('0');
    solve(cur,n0,n1,n2);
    if (s) return ;
    cur.pop_back();

    cur.push_back('1');
    solve(cur,n0,n1,n2);
    if (s) return ;
    cur.pop_back();
  }

  if (!cur.empty() && (cur.back()=='0')){
    cur.push_back('0');
    if (n0>0) solve(cur,n0-1,n1,n2);
    if (s) return ;
    cur.pop_back();

    cur.push_back('1');
    if (n1>0) solve(cur,n0,n1-1,n2);
    if (s) return ;
    cur.pop_back();
  }

  if (!cur.empty() && (cur.back()=='1')){
    cur.push_back('0');
    if (n1>0) solve(cur,n0,n1-1,n2);
    if (s) return ;
    cur.pop_back();

    cur.push_back('1');
    if (n2>0) solve(cur,n0,n1,n2-1);
    if (s) return ;
    cur.pop_back();
  }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t;
    cin>>t;
    while (t--)
    {
      s=false;
      string cur;

      int n0,n1,n2;
      cin>>n0>>n1>>n2;

      solve(cur,n0,n1,n2);

      cout<<cur<<"\n";
    }
    
    return 0;
}