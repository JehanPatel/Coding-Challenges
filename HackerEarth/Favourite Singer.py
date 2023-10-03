from collections import Counter
def count(N,S):
    S_count=Counter(S)
    maxC=max(S_count.values())
    favS = [Singer for Singer, count in S_count.items() if count == maxC]
    return len(favS)
def main():
    N = int(input())
    S = list(map(int,input().split()))
    result=count(N,S)
    print(result)
if __name__=="__main__":
    main()