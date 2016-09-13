import math
if __name__=="__main__":
    num = int(raw_input())
    allpnum = set(filter(lambda x: not [x % i for i in range(2, int(math.sqrt(x))+1) if x%i == 0], range(2, num+1)))
    total = 0
    conts = set([])
    for i in allpnum:
        if num-i in allpnum and num not in conts:
            total +=1
            conts.add(i)
    print total