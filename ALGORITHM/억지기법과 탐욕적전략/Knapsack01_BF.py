# wgt : 물거들의 무게 리스트
# val : 물건들의 가치 리스트
# W : 배낭의 용량
def Knapsack01_BF(wgt, val, W):
    n = len(wgt)
    bestVal = 0
    bestLst = []
    for i in range(2 ** n): # 0 - 2^n-1
        s = [0] * n
        for d in range(n):
            s[d] = i % 2
            i = i // 2
        
        sumVal = 0
        sumWgt = 0
        for d in range(n):
            if s[d] == 1:
                sumWgt += wgt[d]
                sumVal += val[d]

            if sumVal <= W:
                if sumVal > bestVal:
                    bestVal = sumVal
                    bestLst = list(s)

    # print(bestVal, bestLst)
    return bestVal

if __name__ == '__main__':
    weight = [10, 20, 30, 25, 35]
    value = [60, 100, 120, 70, 85]
    W = 80

    print("Knapsack01-BruteForce: ", Knapsack01_BF(weight, value, W))