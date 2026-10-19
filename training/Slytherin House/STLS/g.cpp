#include <bits/stdc++.h>
#define ll long long
using namespace std;



int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin>>n;
    bool s;
    string a;
    
    
    for (int i=0;i<n;i++){
      stack<int> st;
      cin>>a;
      s=true;
      for (auto el:a) {
        if (el=='(' || el=='[' || el=='{') {
          st.push(el);
        } else if (((el==')' || el=='}' || el==']') && st.empty()) || (!st.empty() && ((el==')' && st.top()!='(') || (el=='}' && st.top()!='{') || (el==']' && st.top()!='[')))){
          s=false;
          break;
        }else {
          st.pop();
        }
      }

      if (s) {
      cout<<"YES"<<"\n";
      } else{
        cout<<"NO"<<"\n";
      }

    }

    

    return 0;
}