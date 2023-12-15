#include <bits/stdc++.h>
#define MAXM 1e9

using namespace std;

int main()
{
    //freopen("inp8.txt", "r", stdin);
    //freopen("out8.txt", "w", stdout);
    int d;
    cin >> d;
    assert(1 <= d && d <= 10);
    for (int dd = 1; dd <= d; dd++) {
        int n;
        cin >> n;
        assert(1 <= n && n <= 16);
        vector < pair <long long int, long long int> > a;
        for (int i = 0; i < n; i++) {
            long long int x, y;
            cin >> x >> y;
            assert(1 <= x && x <= MAXM);
            assert(1 <= y && y <= MAXM);
            a.push_back(make_pair(x, y));
        }
        long long int  w;
        int c;
        cin >> w >> c;
        //cout << w << " " << c << endl;
        assert(1 <= w && w <= MAXM);
        assert(1 <= c && c <= 20);
        int p = 1 << n;
        long long maxm_price = -1;
        for (int i = 1; i < p; i++) {
            int ctr = 0;
            long long price, weight;
            price = weight = 0;
            for (int j = 0; j < n; j++) {
                if (i&1<<j) {
                    ctr++;
                    price += a[j].first;
                    weight += a[j].second;
                }
            }
            if (ctr <= c && weight <= w && price > maxm_price) {
                maxm_price = price;
            }
        }
        cout << "For Day #" << dd << ":\n";
        cout << maxm_price << endl;
    }
    return 0;
}