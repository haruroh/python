def qzSumOfContinuousNum(_from, _to):
    return int((_from + _to) * ((_to + 1) - _from) / 2) 
 
def qzComputeSumOfMultiples(_from, _to, _n):
    revFrom = (_from - (_from % _n)) + 1
    revTo   = _to - (_to % _n)
    print(revFrom, revTo, (_to % _n), _to, _n)
   
    sum = qzSumOfContinuousNum(revFrom, revTo)   
    
    midNum = int((revFrom + revTo) / 2)
    count  = int( ( ( (revTo -revFrom)/_n) + 1) )
    innerCount = _n - 1
    print(midNum, count, innerCount)
   
    if (revFrom + revTo) % 2 == 1:
        sum = sum - (midNum * (count * innerCount));
    else:
        sum = sum - ( (midNum * (count * innerCount)) - (count * int((innerCount / 2))))
    print(sum)
    return sum
   
    
 
sum3  = qzComputeSumOfMultiples(1, 10, 3)
 
sum5  = qzComputeSumOfMultiples(1, 10, 5)
 
sum15 = qzComputeSumOfMultiples(1, 10, 15)
 
print(sum3 + sum5 - sum15)