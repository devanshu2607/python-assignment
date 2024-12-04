##58.	Create a program to visualize dynamic programming approaches for the Fibonacci sequence.

def fibonacci_memo(n,memo={}):
    if n <=1:
        return n
    if n not in memo:
        memo[n]=fibonacci_memo(n-1,memo)+fibonacci_memo(n-2,memo)
        print(f"memo: fib({n})={memo[n]}")
        return memo[n]
    
    def fibonacci_tab(n):
        table=[0,1]
        for i in range(2,n+1):
          table.append(table[i-1]+table[i-2])
          print(f"tab: fib({i})+{table[i]}")
        return table[n]
    
    n=6
    print("using memorization:")
    fibonacci_memo(n)

    print("\n using tabulation:")
    fibonacci_tab(n)
