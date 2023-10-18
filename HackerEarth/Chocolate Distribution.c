#include <bits/stdc++.h>
#define MAX 100005
using namespace std;
long long int last_modulo[MAX];
int main()
{
	int testcase ;
	scanf("%d" , &testcase);
	int arr[MAX];
	long long int ans = 0;
	while(testcase--)
	{
		ans = 0;
		int n , m ;
		scanf("%d %d" , &n , &m);
		memset( last_modulo , -1 , sizeof(last_modulo) );
		last_modulo[0] = 0;
		for( int i = 0 ; i < n ; i++ )
			scanf("%d" , &arr[i] );

		long long int sum = 0;
		for( int i = 0 ; i < n ; i++ )
		{
			sum += arr[i];
			int tmp = sum % m ;
			if( last_modulo[ tmp ] == -1 )
			{
				last_modulo[tmp] = sum ;
			}
			else
			{
				ans = max( ans , sum - last_modulo[tmp] );
			}
		}
		printf("%d\n",ans / m  );
	}
	return 0;
}