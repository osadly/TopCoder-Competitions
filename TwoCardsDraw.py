# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import math

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

class TwoCardsDraw:
    def primeChance(self, cards):
        cnt=0
        cards=list(cards)
        for e1 in cards:
            for e2 in cards:
                strR=str(e1)+str(e2)
                #print(int(strR))
                if(isPrime(int(strR))):
                    cnt+=1
                
        return float(cnt)/float(len(cards))/float(len(cards))

obj = TwoCardsDraw()

t1=tuple([50,99,50,50,50,50,50,50,50,50,50,50,99,50,50,50,50,50,50,50,50,50,50,50,99,50,99,50,50,50,50,50,50,50,50,50,50,99,33])
x=obj.primeChance(t1)
print(x)
        
