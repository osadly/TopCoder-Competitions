import math
class FloatingPoint:
    def representations(self, number, mantissa, exponent):
        ret=0
        if number%2==1:
            if float(math.log(number,2)) < float(mantissa):
                return 1
            else:
                return 0
            
        exp = int(math.pow(2,exponent))
        for i in range(exp+1):
            x=number/math.pow(2,i)
            y=int(x)
            #print("1)",exp, x,y)
            if y >= 1 and float(y)-x==0.0:
                #print("2)",float(math.log(y,2)),float(mantissa))
                if float(math.log(y,2)) < float(mantissa):
                    print(number,y,math.pow(2,i))
                    ret+=1
                    
        return ret
