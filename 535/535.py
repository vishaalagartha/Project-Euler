from math import sqrt, floor

#start on term 8
nMax = pow(10, 12)

n = 8
currSum = 15
prevMax = 4
while n<nMax:
    numUncircled = prevMax-1
    #need to include all terms behind previous 1 for next 1 to show up
    a = int(sqrt(prevMax))
    numCircled = int(a * (prevMax-float(1)/6*(2*a+5)*(a-1)))
    #sum of floor of sqrts

    prevMax = numUncircled+numCircled+1
    n+=prevMax
    currSum+=(prevMax*(prevMax+1))/2
    print n, currSum
    print nMax-n
