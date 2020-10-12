def minimumBribes(q):
    dp = [0]*len(q)
    while(sorted(q) != q):
        for i in range(len(q)-1):
            if q[i] > q[i+1]:
                dp[q[i]-1]+=1
                q[i], q[i+1] = q[i+1], q[i]
        if max(dp)>2:
            print("Too chaotic")
            return
    print(sum(dp))
