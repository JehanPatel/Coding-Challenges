#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <math.h>

#define ll long long int
#define maxN 100000
#define maxVal 100000000
#define minVal -100000000
#define mod 1000000007LL
#define LCM 2520

#define gcd(a,b) __gcd(a,b)

using namespace std;

ll l,r;
ll val[10];
ll d[13];
ll dp[13][2525][515];

ll powmod(ll a,ll b)
{
	ll x=1,y=a;
	while(b>0)
	{
		if(b%2)
			x=(x*y)%LCM;
		y=(y*y)%LCM;
		b=b/2;
	}
	return x;
}

void pre()
{
	ll i;
	val[0]=0;
	for(i=1;i<10;i++)
		val[i]=powmod(i,i);
}

ll compute(ll i,ll sum,ll mark,bool z)
{
	ll j;
	if(i==-1)
	{
		ll c=0,p=0;
		for(j=1;j<=9;j++)
			if(mark&(1<<(j-1)))
			{
				p++;
				if(sum%j==0)
					c++;
			}
		if(c==p)
			return 1;
		return 0;
	}
	if(!z&&dp[i][sum][mark]!=-1)
		return dp[i][sum][mark];
	ll ans=0,e=9,f;
	if(z)
		e=d[i];
	for(j=0;j<=e;j++)
	{
		f=mark;
		if(j)
			f=(f|(1<<(j-1)));
		ans=ans+compute(i-1,(sum+val[j])%LCM,f,(z&(j==e)));
	}
	if(!z)
		dp[i][sum][mark]=ans;
	return ans;
}

ll solve(ll n)
{
	ll l=0;
	while(n>0)
	{
		d[l++]=n%10;
		n/=10;
	}
	memset(dp,-1,sizeof(dp));
	return compute(l-1,0,0,true);
}

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
    #endif
    ll t;
    scanf("%lld",&t);
    pre();
    while(t--)
    {
    	scanf("%lld%lld",&l,&r);
    	printf("%lld\n",(solve(r)-solve(l-1)));
    }
    return 0;
}