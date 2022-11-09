class Scramble:
  def scrambleWord(self, text):
    n=len(text)
    if(n<=3):
      return text
    p1=text[0]
    #print(p1)
    p4=text[n-1]
    #print(p4)
    t=text[1:n-1]
    t=''.join(sorted(t))
    #print(t)
    p2,p3="",""
    
    for i in range(n-2):
      if i%2==0:
        p2+=t[i]
      else:
        p3+=t[i]

    p3=p3[::-1]
    return p1+p2+p3+p4
