#include <bits/stdc++.h>
#define ll long long
using namespace std;


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int t;
    cin>>t;
    while (t--)
    {
        int n,ta=0,tb=0,preva=0,prevb=0,turn=0;
        cin>>n;

        deque<int> a(n,0);
        for (int i=0;i<n;i++){
          cin>>a[i];
        }

        while (!a.empty()) {
          int cur=0;
          

          if (turn%2==0) {
            while (!a.empty() && cur<=prevb){
              cur+=a.front();
              ta+=a.front();
              a.pop_front();
            }
            preva=cur;

          } else{
            while (!a.empty() && cur<=preva){
              cur+=a.back();
              tb+=a.back();
              a.pop_back();
            }
            prevb=cur;
          }
          turn+=1;
        }
        cout<<turn<<" "<<ta<<" "<<tb<<"\n";
    }
    
    return 0;
}