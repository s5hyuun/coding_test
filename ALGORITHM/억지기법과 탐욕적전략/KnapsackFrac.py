def KnapSackFrac(wgt, val, W):
    bestVal = 0
    for i in range(len(wgt)):
        if W <= 0:
            break
        if W >= wgt[i]:
            W -= wgt[i]
            bestVal += val[i]
        else:
            fraction = W / wgt[i]
            bestVal += val[i] * fraction
    return bestVal

weight = [12, 10, 8]
value = [120, 80, 60]
W = 18
print("Fractional Knapsack(18): ", KnapSackFrac(weight, value, W))