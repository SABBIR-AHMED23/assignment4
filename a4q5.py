import numpy as np
#Supply & Demand
supply=[80,60,40,20]
demand=[60,60,30,40,10]
#Cost matrix
cost=np.array([
   [4,3,1,2,6],
   [5,2,3,4,5],
   [3,5,4,2,5],
   [2,4,4,5,3]
],dtype=float)

def northwest_corner(s,d):
    s,d=s[:],d[:]
    alloc=np.zeros((len(s),len(d)),dtype=int)
    i=j=0
    while i<len(s) and j<len(d):
        m=min(s[i],d[j])
        alloc[i][j]=m
        s[i]-=m
        d[j]-=m
        if s[i]==0: i+=1
        elif d[j]==0: j+=1
    return alloc

def least_cost(s,d,c):
    s,d=s[:],d[:]
    c=c.copy()
    alloc=np.zeros_like(c)
    while np.any(s) and np.any(d):
        i,j=divmod(np.argmin(c),c.shape[1])
        m=min(s[i],d[j])
        alloc[i][j]=m
        s[i]-=m
        d[j]-=m
        if s[i]==0: c[i,:]=np.inf
        elif d[j]==0: c[:,j]=np.inf
    return alloc

def total_cost(a,c):
    return np.sum(a*c)

nw=northwest_corner(supply,demand)
lc=least_cost(supply,demand,cost)

print('North-West Corner:\n',nw)
print('Cost:',total_cost(nw,cost))
print('\nLeast Cost Method:\n',lc)
print('Cost:',total_cost(lc,cost))
