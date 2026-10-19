#include <bits/stdc++.h>
#define ll long long
using namespace std;

map<int,int>mp;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    string a;
    cin>>a;

    int max=0,cnt=0,ccnt=0;
    stack<int> st;
    st.push(-1);

    for (int i=0;i<a.size();i++) {
      if (a[i]=='('){
        st.push(i);
      }else {
        st.pop();
        if (st.empty()) {
          st.push(i);
        } else {
          ccnt=i-st.top();

          if (ccnt>max){
            max=ccnt;
            cnt=1;
          } else if (ccnt==max){
            cnt+=1;
          }
        }
      }
    }
    if (max==0) cnt=1;
    cout<<max<<' '<<cnt;
    

    return 0;
}