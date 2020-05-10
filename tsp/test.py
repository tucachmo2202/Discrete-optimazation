n=4
dist= [[0,90,42,25],
        [90,0,30,34],
        [42,30,0,10],
        [25,34,10,0]]

isAll = (1<<n) -1

dp = []
trace = []
for i in range(1<<n):
    dp.append([-1]*n)
    trace.append([0]*n)

def tsp(mask, pos):
    # i+=1
    if(mask == isAll):
        return dist[pos][0]

    if(dp[mask][pos] != -1):
        return dp[mask][pos]

    # i += 1

    ans = 1000000000
    ghi = -1
    for city in range(n):
        if((mask&(1<<city)) == 0):
            newAns = dist[pos][city] + tsp(mask|(1<<city), city)
            # way[city] = i
            if newAns < ans:
                ans = newAns
                trace[mask][pos] = city

    # i+=1
    # print(ghi)
    # way[pos] = ghi
    dp[mask][pos] = ans
    return ans

# if __name__ == '__main__':
print("Min Distance = ", tsp(1,0))
print(dp)
taken = [0]*n
# taken[0] = 1
S, j = 0, 0
for i in range(0,n):
    taken[i] = trace[S][j]
    j = taken[i]
    S = S | (1<<j)

print(taken)