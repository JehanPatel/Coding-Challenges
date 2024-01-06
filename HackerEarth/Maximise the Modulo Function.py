def solve(k, n,m):
 
    pre = [0]
    for c in n:
        pre += [(pre[-1] * 10 + int(c))%k]
    ans = pre[-1]%k
    suf = 0
    cur_pow = 1
    for i in range(m - 1, -1, -1):
        ans = max(ans, (pre[i] * cur_pow%k + suf) % k)
        suf += cur_pow * int(n[i])
        suf = suf%k
        cur_pow = cur_pow * 10%k
            
 
        
    return ans
if __name__ == "__main__":
    T = int(input().strip())
    for problem in range(1, T + 1):
        n,k = map(int, input().split())
        A = input()
        print(solve(k, A,n))