#very poor space complexity but yes works 

if __name__ == '__main__':
    m=[]
    for _ in range(int(input())):
        g=[]
        name = input()
        score = float(input())
        g=[name,score]
        m.append(g)
  
    r=[]
    for k in range(len(m)):
        r.append(m[k][1])
    
    r=list(set(r))
    r.sort()
    h=[]
    for t in m:
        if (t[1]==r[1]):
            h.append(t[0])
    h.sort()
   
    for x in h:
        print(x)
      
