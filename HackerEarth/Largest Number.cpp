#include<bits/stdc++.h>
#define int long long int
using namespace std;

int solve(int n, int k)
{
    for (int j = 0; j < k; j++) {
        int ans = 0;
        int i = 1;
        while (n / i > 0) {
            int temp = (n / (i * 10))
                           * i
                       + (n % i);
            i *= 10;
            ans = max(ans, temp);
        }
        n = ans;
    }
    return n;
}

signed main(){
    int n, k;
    cin >> n >> k;
    assert(1 <= n and n <= 1000000000000000000);
    assert(1 <= k and k <= 3);

    int d = 0;
    int m = n;
    while(m)
    {
        d++;
        m /= 10;
    }

    assert(d >= k);

    cout << solve(n, k) << endl;
}