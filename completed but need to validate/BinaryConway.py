class BinaryConway:
    def say(self,term):
        crnt=[1]
        j=0
        for i in range(1,len(term)):
            if term[i]=='1':
                if term[i-1]=='1':
                    crnt[j]+=1
                else: #if term[i-1]=='0'
                    j+=1
                    crnt.append(1)
            else:  #if term[i]=='0':
                if term[i-1]=='0':
                    crnt[j]+=1
                else: #if term[i-1]=='1'
                    j+=1
                    crnt.append(1)
            
        ret=""
        w='10'
        for i in range(len(crnt)):
            ret+=str(bin(crnt[i])[2:])+w[i%2]
            
        return ret
        
obj = BinaryConway()
print(obj.say("1"))
print(obj.say("11"))
print(obj.say("101"))
print(obj.say("111011"))
print(obj.say("11110101"))
print(obj.say("1111111"))
print(obj.say("1111111100000000"))
