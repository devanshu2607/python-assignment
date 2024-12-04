##57.	Write a dynamic programming solution for finding the longest common subsequence.

def lcs(a,b):
    m,n=len(a),len(b)
    dp=[[0]*(n+1)for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j]=dp[i-1][j-1]+1 if a[i-1]==b[j-1] else max(dp[i-1][j],dp[i][j-1])
    
        return dp[m][n]
    
print(lcs('ABCBDAB','BDCAB'))