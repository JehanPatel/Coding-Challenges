#include <bits/stdc++.h>
using namespace std;
#define ll long long
ll a[1000005];
int main()
{
	freopen("input1.txt","r",stdin);
	freopen("output1.txt","wb",stdout);
    
    for(ll i=1;i<=1000000;i++){
        ll r=1;
        for(ll j=1;j<=20;j++){
            r=r*2;
            if(r>i){
                break;
            }
        }
        ll z= (i*r)-1;
        a[i]=z;
        //cout<<a[i]<<endl;
    }
    ll t,x;
    cin>>t;
    while(t--)
    {
        cin>>x;
        ll id = lower_bound(a+1,a+1000000+1,x)-a;
        cout<<(x-id+1)<<endl;
    }
}